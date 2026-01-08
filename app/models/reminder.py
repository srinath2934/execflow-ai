from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime 
from app.db.database import Base 


class Reminder(Base):
    __tablename__="reminders"
    
    id = Column(Integer,primary_key=True,index=True)
    task_id =Column (Integer,ForeignKey("tasks.id"))
    reminder_time = Column(DateTime,default=datetime.utcnow)

    