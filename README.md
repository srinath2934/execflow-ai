# ExecFlow AI

**ExecFlow AI** is an AI-powered execution assistant that converts meeting transcripts into structured, actionable tasks with owners, deadlines, and automated reminders.

This repository currently implements the **backend foundation**: API scaffolding and database schema, designed to scale from local development to cloud deployment.

---

## 🚀 Project Vision

In many teams, meeting action items are lost or forgotten. **ExecFlow AI** solves this by:

*   📥 Accepting raw meeting transcripts
*   🧠 Extracting tasks using AI
*   📋 Structuring execution plans
*   ⏰ Scheduling reminders automatically

> **Note**: This repo represents the MVP backend architecture.

---

## 🧱 Current Implementation Status

### ✅ Day 1 – API Foundation
*   FastAPI application setup
*   Health check and ping endpoints
*   Clean modular project structure

### ✅ Day 2 – Database Layer
*   SQLAlchemy ORM setup
*   SQLite database for local development
*   Schema designed for cloud migration (PostgreSQL-ready)

---

## 🗂️ Project Structure

```plaintext
execflow-ai/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── api/                 # API routes
│   ├── core/                # Configuration
│   ├── db/                  # Database connection
│   ├── models/              # Database models
│   │   ├── meeting.py
│   │   ├── task.py
│   │   └── reminder.py
│   ├── services/            # Business & AI logic (WIP)
│   └── utils/               # Helper utilities
│
├── execflow.db              # SQLite database (local)
├── create_tables.py         # DB table creation script
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🗄️ Database Schema

### **Meetings**
*   `id` (Primary Key)
*   `transcript`
*   `created_at`

### **Tasks**
*   `id` (Primary Key)
*   `description`
*   `owner`
*   `deadline`
*   `meeting_id` (Foreign Key)

### **Reminders**
*   `id` (Primary Key)
*   `task_id` (Foreign Key)
*   `remind_at`

### **Relationships**
`Meeting` → `Tasks` → `Reminder`

---

## ⚙️ Tech Stack

*   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
*   **Server**: Uvicorn (ASGI)
*   **ORM**: SQLAlchemy (Database abstraction)
*   **Database**: SQLite (Local development)
*   **Language**: Python 3.12

---

## ▶️ How to Run Locally

1.  **Create virtual environment**
    ```bash
    python -m venv excevenv
    ```

2.  **Activate environment**
    ```bash
    # Windows
    excevenv\Scripts\activate
    
    # Mac/Linux
    source excevenv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create database tables**
    ```bash
    python create_tables.py
    ```

5.  **Run the API server**
    ```bash
    uvicorn app.main:app --reload
    ```

6.  **Open API docs**
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 API Endpoints (Current)

| Method | Endpoint | Purpose |
| :--- | :--- | :--- |
| `GET` | `/ping` | API connectivity check |
| `GET` | `/health` | Service health check |

---

## 🔮 Roadmap

*   **Day 3**: Save meetings and tasks via API
*   **Day 4**: AI-based task extraction (LLM integration)
*   **Day 5**: Reminder scheduling logic
*   **Future**: Cloud database + deployment

---

## 🧠 Design Philosophy

*   **Local-first development**: Easy to start, easy to test.
*   **Clean separation of concerns**: Modular architecture.
*   **Cloud-ready**: Built to scale.
*   **MVP-focused**: No overengineering.

---

## 📄 License

MIT License
