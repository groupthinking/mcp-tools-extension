# MCP Playground + Google ADK Agents Integration

This integration connects Open Protocol's MCP (Model Context Protocol) with Google's Agent Development Kit (ADK) Gemini models, creating a powerful AI agent system.

## Overview

The integration combines:
- **MCP** (TypeScript): For handling Open Protocol context management
- **Google ADK** (Python): For agent-based workflows using Gemini models

## Components

### ADK Microservice
- FastAPI service that exposes Google ADK capabilities
- Uses a hierarchy of specialized agents for different tasks
- Exposes a `/generate_report` endpoint for complex topic research

### MCP Integration
- TypeScript client for connecting to the ADK service
- Integration with the existing MCP Playground
- Flag-based routing to choose between ADK and standard MCP

## Getting Started

### Prerequisites
- Node.js 16+ and npm
- Python 3.11
- Docker and Docker Compose (for containerized deployment)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/groupthinking/Open_Pro.git
cd Open_Pro
```

2. **Install dependencies:**
```bash
# MCP (TypeScript)
npm install

# ADK (Python)
pip install -r requirements.txt
```

3. **Set up environment:**
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Running Locally

**Start the ADK service:**
```bash
uvicorn adk_service:app --host 0.0.0.0 --port 8000
```

**Start the MCP service:**
```bash
npm start
```

### Docker Deployment

**Using Docker Compose:**
```bash
docker-compose up -d
```

## Testing

Use the included test script:
```bash
./test-script.sh
```

This will test both standard MCP functionality and ADK integration.

## Security Notes

- Environment-specific configuration for sensitive data
- API key-based authentication for the ADK microservice
- HTTPS recommended for all production endpoints

## Architecture

```
User request → MCP Playground (checks use_adk flag)
 ├→ ADK Microservice (if flagged) → Gemini-based report generation
 └→ MCP internal handling (if not flagged)
```

## Contributing

Contributions are welcome! Please follow the existing code style and add tests for new features. 