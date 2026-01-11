from sqlalchemy import Column, Integer, Text, DateTime
from datetime import datetime
from app.db.database import Base


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    transcript = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)