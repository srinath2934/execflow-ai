from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="ExecFlow AI")

# Include API routes
app.include_router(router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok"}
