"""
Database initialization script.
Run this from the project root to create all database tables.
"""
from app.db.database import engine, Base
from app.models.task import Task
from app.models.meeting import Meeting
from app.models.reminder import Reminder


def create_tables():
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")
    print("   - tasks")
    print("   - meetings")
    print("   - reminders")


if __name__ == "__main__":
    create_tables()
