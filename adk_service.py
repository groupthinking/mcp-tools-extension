from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool, google_search
from google.adk.runners import Runner

app = FastAPI()

web_searcher = LlmAgent(model="gemini-2.0-flash", tools=[google_search])
summarizer = LlmAgent(model="gemini-2.0-flash")
search_assistant = LlmAgent(
    model="gemini-2.0-flash",
    tools=[agent_tool.AgentTool(agent=web_searcher), agent_tool.AgentTool(agent=summarizer)]
)
search_planner = LlmAgent(
    model="gemini-2.5-pro-exp-03-25",
    tools=[agent_tool.AgentTool(agent=search_assistant)]
)
report_writer = LlmAgent(
    model="gemini-2.0-flash",
    tools=[agent_tool.AgentTool(agent=search_planner), agent_tool.AgentTool(agent=search_assistant)]
)

runner = Runner(agent=report_writer)

class Query(BaseModel):
    topic: str

@app.post("/generate_report")
def generate_report(query: Query):
    try:
        result = runner.run(query.topic)
        return {"report": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 