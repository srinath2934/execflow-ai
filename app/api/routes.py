from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.transcript_processor import create_meeting_from_transcript
from app.services.meeting_service import get_all_meetings
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


@router.get("/meetings")
def list_meetings():
    """Get all meetings with preview."""
    meetings = get_all_meetings()
    return {
        "meetings": meetings,
        "count": len(meetings)
    }
