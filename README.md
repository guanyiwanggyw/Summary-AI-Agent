# Summary AI Agent

An interactive research assistant built with LangChain and the Google Gemini API. It can answer research questions, use web and Wikipedia search tools, return a structured response, and append results to a text file.

## Features

- Uses `gemini-3.8-flash` through LangChain's Google GenAI integration.
- Searches the web with DuckDuckGo and looks up articles with Wikipedia.
- Formats responses with the `ResearchResponse` schema: `topic`, `summary`, `sources`, and `tools_used`.
- Saves research to `research_output.txt` when the save tool is selected by the agent.

## Requirements

- Python 3.10 or newer.
- A Gemini API key. Google AI Studio free-tier keys are subject to model availability, quotas, and rate limits.
- Internet access for Gemini, DuckDuckGo, and Wikipedia requests.

## Setup (Windows PowerShell)

From the project directory, create and activate a virtual environment, then install the pinned dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a `.env` file in the project directory and add your key:

```text
GOOGLE_API_KEY=your-gemini-api-key
```

Keep `.env` private and do not commit or share your API key.

## Run

```powershell
python main.py
```

Enter a research question when prompted. The agent prints the structured response in the terminal. To save it, ask the agent to save the research; saved entries are appended to `research_output.txt` in the current working directory.

## Tools

- `search`: DuckDuckGo web search.
- `WikipediaQueryRun`: Wikipedia lookup, configured to return one result with a short excerpt.
- `save_as_txt`: Appends research text and a timestamp to `research_output.txt`.

The agent decides whether a tool is appropriate for a query, so mentioning the desired action (for example, “search the web” or “save this to a file”) can make your intent clearer. Tool results depend on the external services being available.

## Configuration

The model is set in `main.py` with `ChatGoogleGenerativeAI(model="gemini-3.8-flash")`. If that model is unavailable to your API key or temporarily overloaded, replace it with a model ID enabled for your Gemini API project. Model availability and free-tier limits can change.
