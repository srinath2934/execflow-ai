from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.transcript_processor import create_meeting_from_transcript 
router = APIRouter()

class MeetingRequest(BaseModel):
    transcript: str


@router.post("/meetings")
def create_meeting(request: MeetingRequest):
    if not request.transcript.strip():
        raise HTTPException(status_code=400, detail="Transcript is required")
    
    meeting_id = create_meeting_from_transcript(request.transcript)


    return {
        "message": "Meeting saved successfully",
        "meeting_id": meeting_id
    }
