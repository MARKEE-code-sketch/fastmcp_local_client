🚀 MCP Multi-Server Client
LangChain + FastMCP + Ollama Integration

A production-style MCP client that connects to local and remote MCP servers, loads tools dynamically, and executes them via an LLM agent.

✨ What This Project Does

This client:

🔌 Connects to multiple MCP servers

🧠 Loads tools dynamically from MCP endpoints

🤖 Uses an LLM (Ollama/HuggingFace) to decide tool usage

🌐 Supports local (stdio) and remote (HTTP) MCP

🔐 Loads API keys securely from .env

⚙️ Executes tool calls automatically

🧭 Architecture Overview
        +---------------------+
        |     LLM Agent       |
        |  (Ollama / HF)      |
        +----------+----------+
                   |
                   v
        +---------------------+
        |  LangChain MCP      |
        |   Multi Client      |
        +----------+----------+
                   |
        +----------+----------+
        |                     |
        v                     v
 Local MCP Server      Remote FastMCP Server
 (stdio transport)     (HTTP transport)

📁 Project Structure
.
├── client1.py          # MCP client implementation
├── .env                # API keys (not committed)
├── README.md

🧱 Step 1 — Install Requirements
pip install langchain langchain-core \
langchain-mcp-adapters \
langchain-ollama \
langchain-huggingface \
python-dotenv

🔐 Step 2 — Setup Environment Variables

Create a .env file:

FASTMCP_API_KEY=sk-fmcp-xxxxxxxxxxxxxxxx


This is required for remote FastMCP authentication.

🖥️ Step 3 — Configure MCP Servers
🧪 Local MCP Server (stdio)
"demo_server": {
    "transport": "stdio",
    "command": r"C:\Users\mrina\.local\bin\uv.exe",
    "args": [
        "run",
        "python",
        r"C:\Users\mrina\Desktop\MCP\fastmcp-demo-server\main.py"
    ],
}

☁️ Remote FastMCP Server (HTTP)
"expense_tracker": {
    "transport": "http",
    "url": "https://cooperative-lavender-gazelle.fastmcp.app/mcp",
    "headers": {
        "Authorization": f"Bearer {os.getenv('FASTMCP_API_KEY')}"
    }
}
