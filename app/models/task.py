from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    owner = Column(String, nullable=True)  # Changed to nullable=True since LLM might not always find owner
    deadline = Column(String, nullable=True)  # Storing as string for flexibility (e.g., "2026-01-15" or "next week")
    meeting_id = Column(Integer, ForeignKey("meetings.id"), nullable=False)  # Link to meeting
    created_at = Column(DateTime, default=datetime.utcnow)