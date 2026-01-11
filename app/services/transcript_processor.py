from app.db.database import SessionLocal
from app.models.meeting import Meeting
from app.services.ai_task_extractor import extract_tasks_from_transcript

MIN_TRANSCRIPT_LENGTH = 100

def create_meeting_from_transcript(transcript: str) -> int:
    """
    Create a meeting from a transcript and extract tasks from it.
    
    Args:
        transcript (str): The meeting transcript text
        
    Returns:
        int: The meeting ID
    """
    cleaned_transcript = transcript.strip()

    # Validate transcript length
    if len(cleaned_transcript) < MIN_TRANSCRIPT_LENGTH:
        raise ValueError("Transcript is too short to be a valid meeting")

    # Save the meeting to database
    db = SessionLocal()

    meeting = Meeting(transcript=cleaned_transcript)
    db.add(meeting)
    db.commit()
    db.refresh(meeting)

    meeting_id = meeting.id
    db.close()

    # Extract tasks from the transcript (NEW - Day 4)
    print(f"\n[INFO] Starting task extraction for meeting {meeting_id}")
    try:
        print("[INFO] Calling extract_tasks_from_transcript...")
        task_count = extract_tasks_from_transcript(cleaned_transcript, meeting_id)
        print(f"[SUCCESS] Extracted {task_count} tasks from meeting {meeting_id}")
    except Exception as e:
        print(f"[ERROR] Task extraction failed for meeting {meeting_id}")
        print(f"[ERROR] Error type: {type(e).__name__}")
        print(f"[ERROR] Error message: {e}")
        import traceback
        traceback.print_exc()
        # Don't fail the entire operation if task extraction fails
        # The meeting is still saved, just without tasks

    return meeting_id   