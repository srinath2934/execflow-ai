# Database Architecture & Visual Documentation

## 1. Entity-Relationship Diagram (ERD)

```mermaid
erDiagram
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

    TASK ||--o{ REMINDER : "has (1:N)"
```

### Relationship Explanation
- **`TASK ||--o{ REMINDER`**: One-to-Many relationship
  - One Task can have zero, one, or multiple Reminders
  - Each Reminder must belong to exactly one Task (Foreign Key constraint)

---

## 2. Database Architecture Flow

```mermaid
graph TB
    subgraph "Data Input Layer"
        A[Meeting Transcript] --> B[meetings table]
    end
    
    subgraph "Processing Layer"
        B --> C[AI Task Extractor]
        C --> D[tasks table]
    end
    
    subgraph "Scheduling Layer"
        D --> E[Reminder Service]
        E --> F[reminders table]
    end
    
    subgraph "Output Layer"
        F --> G[Notifications]
        D --> H[Task Management API]
    end
    
    style A fill:#e1f5ff
    style B fill:#b3e5fc
    style C fill:#81d4fa
    style D fill:#4fc3f7
    style E fill:#29b6f6
    style F fill:#03a9f4
    style G fill:#039be5
    style H fill:#0288d1
```

---

## 3. Table Creation Logic

```mermaid
sequenceDiagram
    participant Script as create_tables.py
    participant Base as SQLAlchemy Base
    participant Models as Model Classes
    participant Engine as Database Engine
    participant DB as SQLite Database

    Script->>Base: Import declarative_base()
    Script->>Models: Import Task, Meeting, Reminder
    Models->>Base: Register with Base.metadata
    Script->>Base: Call create_all(bind=engine)
    Base->>Engine: Generate CREATE TABLE SQL
    Engine->>DB: Execute SQL statements
    DB-->>Engine: Confirm table creation
    Engine-->>Script: ✅ Tables created
```

---

## 4. Data Relationships Graph

```mermaid
graph LR
    subgraph "Independent Entities"
        M[meetings]
        T[tasks]
    end
    
    subgraph "Dependent Entity"
        R[reminders]
    end
    
    T -->|task_id FK| R
    
    style M fill:#4caf50
    style T fill:#2196f3
    style R fill:#ff9800
```

---

## 5. Schema Details

### `tasks` Table
- **Purpose**: Central entity for action items
- **Fields**:
  - `id`: Primary Key (auto-increment)
  - `description`: Full task content (Text)
  - `owner`: Assignee name (String)
  - `created_at`: Timestamp (auto-generated)

### `meetings` Table
- **Purpose**: Raw transcript storage
- **Fields**:
  - `id`: Primary Key (auto-increment)
  - `transcript`: Meeting content (Text)
  - `created_at`: Timestamp (auto-generated)

### `reminders` Table
- **Purpose**: Time-based task alerts
- **Fields**:
  - `id`: Primary Key (auto-increment)
  - `task_id`: Foreign Key → `tasks.id`
  - `reminder_time`: Alert trigger time (DateTime)

---

## 6. Initialization Process

### Step 1: Registry Pattern
- `Base = declarative_base()` creates a metadata catalog
- All models inherit from `Base`

### Step 2: Model Registration
- Importing model classes executes their definitions
- `class Task(Base):` automatically registers with `Base.metadata`

### Step 3: Schema Generation
- `Base.metadata.create_all(bind=engine)` inspects registered models
- Generates SQL `CREATE TABLE` statements
- Executes only for missing tables (preserves existing data)
