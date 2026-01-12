from app.db.database import SessionLocal
from app.models.meeting import Meeting
from typing import List, Dict, Any

PREVIEW_LENGTH = 200


def get_all_meetings() -> List[Dict[str, Any]]:
    """
    Retrieve all meetings from the database.
    
    Returns:
        List[Dict]: List of meetings with id, created_at, and transcript_preview
    """
    db = SessionLocal()
    
    try:
        # Query all meetings, ordered by most recent first
        meetings = db.query(Meeting).order_by(Meeting.created_at.desc()).all()
        
        # Format the response
        meeting_list = []
        for meeting in meetings:
            # Generate transcript preview (first 200 characters)
            preview = meeting.transcript[:PREVIEW_LENGTH]
            if len(meeting.transcript) > PREVIEW_LENGTH:
                preview += "..."
            
            meeting_list.append({
                "id": meeting.id,
                "created_at": meeting.created_at.isoformat() if meeting.created_at else None,
                "transcript_preview": preview
            })
        
        return meeting_list
    
    finally:
        db.close()
