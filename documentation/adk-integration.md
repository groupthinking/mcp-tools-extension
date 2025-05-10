# MCP Playground + Google ADK Agents Integration

This document provides detailed information on the integration between Open Protocol's MCP (Model Context Protocol) and Google's Agent Development Kit (ADK).

## Architecture Overview

### Agent Hierarchy

The ADK microservice implements a multi-agent system with the following hierarchy:

1. **Report Writer (Gemini 2.0 Flash)** - Top-level agent for producing comprehensive reports
   - Uses Search Planner and Search Assistant

2. **Search Planner (Gemini 2.5 Pro Experimental)** - Strategizes research approach  
   - Uses Search Assistant

3. **Search Assistant (Gemini 2.0 Flash)** - Performs targeted searches
   - Uses Web Searcher and Summarizer

4. **Web Searcher (Gemini 2.0 Flash)** - Agent specialized in web search operations

5. **Summarizer (Gemini 2.0 Flash)** - Agent specialized in concise summarization

### Data Flow

1. User submits topic to MCP Playground with `use_adk: true`
2. MCP forwards request to ADK microservice
3. Report Writer coordinates the agent hierarchy:
   - Search Planner develops research strategy
   - Search Assistant implements search strategy using Web Searcher
   - Summarizer consolidates information
   - Report Writer compiles final report
4. Comprehensive report returned to MCP, then to user

## Implementation Details

### ADK Microservice Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/generate_report` | POST | Generates a comprehensive report on the provided topic |

### Request Format

```json
{
  "topic": "Topic for report generation"
}
```

### Response Format

```json
{
  "report": "Comprehensive report text..."
}
```

## Error Handling

The ADK microservice implements robust error handling:

1. **Service Unavailability**
   - MCP will fallback to standard processing if ADK service is unreachable
   - Errors are logged for monitoring

2. **Processing Errors**
   - Detailed error messages are returned to aid debugging
   - HTTP status codes indicate the nature of failures

## Performance Considerations

- **Response Time**: The agent hierarchy may take 30-60 seconds for comprehensive reports
- **Rate Limiting**: The ADK service implements rate limiting based on Gemini API quotas
- **Caching**: Frequently requested topics are cached to improve response times

## Security Model

The ADK microservice follows a security-first approach:

1. **Authentication**
   - API key validation for all requests
   - Per-client rate limiting

2. **Data Privacy**
   - No persistent storage of user queries or responses
   - All data transmission over HTTPS
   - Minimal logging with PII scrubbing

## Monitoring

The ADK service includes comprehensive monitoring:

1. **Health Checks**
   - `/health` endpoint reports service status
   - Internal agent availability monitoring

2. **Performance Metrics**
   - Request duration tracking
   - Error rate monitoring
   - Agent utilization statistics

## Future Enhancements

1. **Additional Agent Types**
   - Code generation specialist
   - Visual content creator
   - Multi-lingual support

2. **Advanced Integration**
   - Streaming responses
   - Progress updates for long-running tasks
   - Interactive query refinement

3. **Enhanced MCP Integration**
   - Two-way context sharing
   - Hybrid MCP-ADK processing pipelines 