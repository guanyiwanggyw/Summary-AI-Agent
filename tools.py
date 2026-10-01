from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime

def save_as_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    formatted_text = f"--- RESEARCH OUTPUT ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data succesfully saved to {filename}"

save_tool = Tool(
    name="save_as_txt",
    func=save_as_txt,
    description="Saves structured research data to a .txt file",
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the internet for information",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)