# AI Agent Project

A sample AI Agent project built with LangChain and LangGraph frameworks, implementing the ReAct (Reasoning and Acting) pattern to create an intelligent agent capable of calling tools and interacting with users.

## Overview

This project demonstrates how to build an AI agent that can:
- Understand user queries through natural language processing
- Use the ReAct pattern for reasoning and tool selection
- Execute specific tools based on user requests
- Provide interactive conversational experience

## Features

- **LangChain Integration**: Utilizes LangChain for language model interactions
- **LangGraph Framework**: Implements agent workflows using LangGraph
- **ReAct Pattern**: Reasoning and Acting pattern for intelligent decision making
- **Tool Integration**: Custom tools for specific functionalities
- **Local Model Support**: Uses Ollama with Mistral model for local inference
- **Interactive CLI**: Command-line interface for user interaction

## Current Tools

1. **Greeting Tool**: Provides personalized greetings to users
2. **Calculator Tool**: Performs basic arithmetic operations (addition)

## Architecture

```
User Input → LangGraph Agent → ReAct Processing → Tool Selection → Tool Execution → Response
```

The agent uses the ReAct pattern to:
1. **Observe** the user input
2. **Think** about what action to take
3. **Act** by calling appropriate tools
4. **Observe** the results and provide response

## Prerequisites

- Python 3.8+
- Ollama installed locally with Mistral model
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MelikaMirdamadi/AI_Agent_Project.git
cd AI_Agent_Project
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirement.txt
```

4. Install and setup Ollama:
```bash
# Download Ollama from https://ollama.ai/
# Pull the Mistral model
ollama pull mistral
```

5. Create a .env file (if needed for additional configurations)

## Usage

1. Start the AI agent:
```bash
python main.py
```

2. Interact with the agent:
```
Hello, welcome, I'm AI assistant, ask me your question , and type 'exit' to quit

You: Hello, my name is John
AI: [Agent will use greeting tool and respond]

You: What is 5 + 3?
AI: [Agent will use calculator tool and respond]

You: exit
Goodbye!
```

## Project Structure

```
AI_Agent_Project/
├── main.py           # Main application file
├── requirement.txt   # Python dependencies
├── Readme.txt       # Project documentation
└── .env             # Environment variables (optional)
```

## Dependencies

Key dependencies include:
- `langchain-core`: Core LangChain functionality
- `langgraph`: Graph-based agent framework
- `langchain-ollama`: Ollama integration for LangChain
- `python-dotenv`: Environment variable management

## Extending the Project

To add new tools:

1. Define a new tool using the `@tool` decorator:
```python
@tool
def your_tool_name(param: type) -> str:
    """
    Description of what your tool does
    """
    # Your tool implementation
    return result
```

2. Add the tool to the tools list in main():
```python
tools = [greeting, calculator, your_tool_name]
```

## Technical Details

- **Model**: Mistral via Ollama (local inference)
- **Agent Type**: ReAct agent with tool calling capabilities
- **Framework**: LangGraph prebuilt agent executor
- **Streaming**: Real-time response streaming for better user experience

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Future Enhancements

- [ ] Add more utility tools (weather, web search, file operations)
- [ ] Implement memory for conversation history
- [ ] Add configuration file for model selection
- [ ] Create web interface using Streamlit or FastAPI
- [ ] Add logging and error handling
- [ ] Implement tool validation and safety checks

## Troubleshooting

**Error: "Expected a Runnable, callable or dict"**
- Ensure you're using `ChatOllama` from `langchain_ollama` instead of direct `ollama.chat()`

**Model not found error**
- Make sure Ollama is running and Mistral model is pulled: `ollama pull mistral`

**Import errors**
- Verify all dependencies are installed: `pip install -r requirement.txt`

## License

This project is open source and available under the MIT License.

## Contact

For questions or suggestions, please open an issue in the GitHub repository. 
