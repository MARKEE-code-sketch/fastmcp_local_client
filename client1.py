import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import ToolMessage
import os

load_dotenv()

SERVERS = {
    "demo_server": {
        "transport": "stdio",
        "command": r"C:\Users\mrina\.local\bin\uv.exe",
        "args": [
            "run",
            "python",
            r"C:\Users\mrina\Desktop\MCP\fastmcp-demo-server\main.py"
        ],
    },
    "expense_tracker": {
  "transport": "http",
  "url": "https://cooperative-lavender-gazelle.fastmcp.app/mcp",
   "headers": {
            "Authorization": f"Bearer {os.getenv('FASTMCP_API_KEY')}"
    }
}
}



async def main():
    client = MultiServerMCPClient(SERVERS)
    tools = await client.get_tools()
 
    named_tools={}
    for tool in tools:
        named_tools[tool.name]=tool

    llm = ChatOllama(
    model="llama3.1",
    temperature=0)

    agent_llm=llm.bind_tools(tools)

    prompt = """
You may answer directly using your own knowledge.
Only use tools if necessary.If no tool is needed, respond with plain text and no JSON.
add a new expense- Cab ride to Amazon office, 110 rs spent, choose category from the resource.
"""

    response = await agent_llm.ainvoke(
        prompt
    )

     # Execute the tool if the model requested it
    if response.tool_calls:
        for call in response.tool_calls:
            tool_name=call["name"]
            tool_args=call["args"]
            tool_id=call["id"]
            tool_result=await named_tools[tool_name].ainvoke(tool_args)
            print(tool_result)

            tool_message=ToolMessage(content=tool_result,tool_name=tool_name,tool_call_id=tool_id)
            final=await agent_llm.ainvoke([prompt,response,tool_message])
            print(f"final_result:{final.content}")
    else:
        print(response.content)

   

if __name__=='__main__':
    asyncio.run(main())