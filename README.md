# fastmcp_local_client
MCP Multi-Server Client (LangChain + FastMCP)

A Python client for connecting to multiple MCP servers (local + remote) and invoking tools through an (local) LLM agent.

This project demonstrates how to:

connect to local MCP servers via stdio

connect to remote MCP servers over HTTP

load API keys securely using .env

integrate MCP tools with LangChain agents

execute tool calls dynamically using an LLM (Ollama / HuggingFace)

Features

Multi-server MCP connectivity

Local server execution using uv run

Remote FastMCP server integration

Environment-based API key loading

LangChain agent with tool binding

Automatic tool execution loop

Works with:

Ollama models

HuggingFace endpoints

FastMCP deployments

Project Structure
.
├── client1.py
├── .env
├── README.md

Requirements

Install dependencies:

pip install langchain langchain-core langchain-mcp-adapters \
langchain-ollama langchain-huggingface python-dotenv asyncio


You also need:

Python 3.10+

Ollama installed (for local LLM)

FastMCP server deployed (local or remote)

Environment Setup

Create a .env file:

FASTMCP_API_KEY=sk-fmcp-xxxxxxxxxxxx


This key is used for authenticating remote MCP servers.

MCP Server Configuration

Inside client1.py, define servers:

Local MCP server (stdio)
"demo_server": {
    "transport": "stdio",
    "command": r"C:\Users\mrina\.local\bin\uv.exe",
    "args": [
        "run",
        "python",
        r"C:\Users\mrina\Desktop\MCP\fastmcp-demo-server\main.py"
    ],
}

Remote FastMCP server (HTTP)
"expense_tracker": {
    "transport": "http",
    "url": "https://cooperative-lavender-gazelle.fastmcp.app/mcp",
    "headers": {
        "Authorization": f"Bearer {os.getenv('FASTMCP_API_KEY')}"
    }
}

Running the Client

Activate environment:

python client1.py


The client will:

Connect to MCP servers

Fetch available tools

Bind tools to LLM

Send prompt to model

Execute tool calls if requested

Return final response

Example Prompt
add a new expense- Cab ride to Amazon office, 110 rs spent, choose category from the resource.


Agent decides:

whether to respond directly

or invoke MCP tool
