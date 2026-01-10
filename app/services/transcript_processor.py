from app.db.database import SessionLocal
from app.models.meeting import Meeting 

MIN_TRANSCRIPT_LENGTH = 100 

def create_meeting_from_transcript(transcript: str) -> int: 
    cleaned_transcript= transcript.strip()


    if len(cleaned_transcript) < MIN_TRANSCRIPT_LENGTH:
        raise ValueError("Transcript is too short to be a valid meeting")

    db = SessionLocal()

    meeting=Meeting(transcript=cleaned_transcript)
    db.add(meeting)
    db.commit()
    db.refresh(meeting)

    db.close()

    return meeting.id   