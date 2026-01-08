from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey 
from datetime import datetime
from app.db.database import Base 

class Task(Base):
    __tablename__ = "tasks" 

    id = Column(Integer,primary_key=True,index=True)
    description = Column (Text,nullable=False)
    owner  = Column(String,nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow)


    