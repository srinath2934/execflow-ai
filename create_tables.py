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

"""
Database Entity-Relationship Diagram (ERD)
------------------------------------------

The following Mermaid diagram represents the schema created by this script:

```mermaid
erDiagram
    %% Entities
    TASK {
        int id PK "Unique identifier"
        text description "Task details"
        string owner "Owner of the task"
        datetime created_at "Creation timestamp"
    }

    MEETING {
        int id PK "Unique identifier"
        text transcript "Meeting content"
        datetime created_at "Creation timestamp"
    }

    REMINDER {
        int id PK "Unique identifier"
        int task_id FK "Reference to TASK"
        datetime reminder_time "Scheduled time"
    }

    %% Relationships
    TASK ||--o{ REMINDER : "has (1:N)"
```
"""
