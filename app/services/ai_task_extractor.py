import json 
import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq 
from langchain_core.prompts import PromptTemplate
from app.db.database import SessionLocal 
from app.models.task import Task

# Load environment variables
load_dotenv() 


#  load prompt template 

def load_prompt_template(): 
    """ Load the task extraction prompt template from a file """
    prompt_path = os.path.join(os.path.dirname(__file__), "..", "..", "prompts", "task_extraction_prompt.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


def extract_tasks_from_transcript(transcript: str, meeting_id: int) -> int:
    """
    Extract tasks from a meeting transcript using an LLM.
    
    Args:
        transcript (str): The meeting transcript text
        meeting_id (int): The ID of the meeting in the database
        
    Returns:
        int: Number of tasks extracted and saved
    """
    
    # Step 1: Initialize the LLM (Groq)
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",  # Updated to current active model (Jan 2026)
        temperature=0  # Deterministic output for structured extraction
    )
    
    # Step 2: Build the prompt
    prompt_template_text = load_prompt_template()
    prompt = PromptTemplate(
        input_variables=["transcript"],
        template=prompt_template_text
    )
    
    # Step 3: Create the full prompt with the transcript
    formatted_prompt = prompt.format(transcript=transcript)
    
    # Step 4: Call the LLM
    try:
        response = llm.invoke(formatted_prompt)
        raw_output = response.content.strip()
        
        # Debug: Print raw LLM output (optional, remove in production)
        print("=== LLM Raw Output ===")
        print(raw_output)
        print("======================")
        
    except Exception as e:
        print(f"Error calling LLM: {e}")
        return 0
    
    # Step 5: Parse the JSON response
    try:
        # Clean up any markdown code blocks if present
        if raw_output.startswith("```json"):
            raw_output = raw_output.replace("```json", "").replace("```", "").strip()
        elif raw_output.startswith("```"):
            raw_output = raw_output.replace("```", "").strip()
        
        tasks_data = json.loads(raw_output)
        
        # Validate it's a list
        if not isinstance(tasks_data, list):
            print("LLM output is not a JSON array")
            return 0
            
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON from LLM output: {e}")
        return 0
    
    # Step 6: Save tasks to the database
    db = SessionLocal()
    task_count = 0
    
    try:
        for task_data in tasks_data:
            # Validate required fields
            description = task_data.get("description")
            if not description:
                continue  # Skip tasks without description
            
            owner = task_data.get("owner")
            if not owner or owner.lower() == "unassigned":
                owner = None  # Store as NULL in database
            
            deadline = task_data.get("deadline")
            
            # Create Task object
            task = Task(
                description=description,
                owner=owner,
                deadline=deadline,
                meeting_id=meeting_id
            )
            
            db.add(task)
            task_count += 1
        
        # Commit all tasks at once
        db.commit()
        print(f"Successfully extracted and saved {task_count} tasks")
        
    except Exception as e:
        db.rollback()
        print(f"Error saving tasks to database: {e}")
        task_count = 0
    finally:
        db.close()
    
    return task_count
