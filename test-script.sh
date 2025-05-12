#!/bin/bash

echo "Testing MCP-ADK Integration"
echo "--------------------------"

# Test MCP Playground without ADK
echo -e "\nTesting standard MCP response:"
curl -X POST http://localhost:5000/api/playground \
-H "Content-Type: application/json" \
-d '{"topic": "Future of Model Context Protocol", "use_adk": false}'

# Test MCP Playground with ADK
echo -e "\n\nTesting ADK integration:"
curl -X POST http://localhost:5000/api/playground \
-H "Content-Type: application/json" \
-d '{"topic": "Latest trends in AI startups", "use_adk": true}'

echo -e "\n" 