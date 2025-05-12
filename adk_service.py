from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI()

# Simpler ADK simulation for testing Docker setup
class Query(BaseModel):
    topic: str

@app.get("/")
def read_root():
    return {"status": "ADK service is running"}

@app.get("/docs")
def read_docs():
    return {"status": "ADK service documentation"}

@app.post("/generate_report")
def generate_report(query: Query):
    try:
        logger.info(f"Received topic: {query.topic}")
        # For testing, just return a mock response
        return {
            "report": f"This is a simulated report about: {query.topic}\n\nThe integration is working properly.",
            "status": "success"
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 