from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize the Langchain tool
ddg = DuckDuckGoSearchRun()

@tool("Internet Search Tool")
def search_tool(query: str) -> str:
    """Search the internet for news, trends, and information."""
    return ddg.run(query)
