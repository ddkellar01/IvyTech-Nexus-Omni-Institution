from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="IvyTech Nexus Professors Swarm API", version="2.0.0")

class SymposiumRequest(BaseModel):
    topic: str
    initiator: str

@app.get("/health")
def health_check():
    return {"status": "operational", "system": "IvyTech-Nexus-Professors-Swarm"}

@app.post("/api/v1/symposium")
def trigger_symposium(req: SymposiumRequest):
    return {
        "status": "Success",
        "topic": req.topic,
        "message": f"Symposium initiated across autonomous professor nodes by {req.initiator}."
    }
