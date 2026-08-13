# langchain-agent-project

A hands-on Python project demonstrating how to build an AI agent with LangChain, an OpenAI language model, and custom tools.

The project focuses on the fundamental architecture of an agent: an LLM acts as the reasoning engine, while tools extend the agent's capabilities so it can perform actions instead of only generating text.

## 🧠 Overview

This project implements a simple ReAct-style agent using LangChain's agent framework.

The agent receives a natural-language request, determines which tool is required, executes the tool, and uses the result to produce the final answer.

For example:

Question: What is 15 multiplied by 8 and divided by 3?

The agent can determine that it needs to:

1. Multiply 15 × 8
2. Divide the result by 3
3. Return 40

The project uses LangChain's create_agent API to connect the model and tools.

## 🏗️ Architecture

The project follows a simple separation of responsibilities:

```text
                        ┌──────────────────────┐
                        │      User Input      │
                        └──────────┬───────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │    LangChain Agent   │
                        │                      │
                        │     ReAct Pattern    │
                        └──────────┬───────────┘
                                   │
                         ┌─────────┴─────────┐
                         │                   │
                         ▼                   ▼
                ┌────────────────┐   ┌────────────────┐
                │   multiply     │   │     divide     │
                │     Tool       │   │      Tool      │
                └────────────────┘   └────────────────┘
                         │                   │
                         └─────────┬─────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │     Final Answer     │
                        └──────────────────────┘
```

### Main components

- **Model** — OpenAI `gpt-5.6`
- **Agent** — LangChain agent created with `create_agent`
- **Tools** — Custom multiplication and division functions
- **Configuration** — Environment variables loaded with `python-dotenv`
- **Tests** — `pytest` tests for the mathematical tools

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Application language |
| LangChain | Agent orchestration and tool integration |
| LangChain OpenAI | OpenAI model integration |
| OpenAI | LLM / reasoning engine |
| LangGraph | Agent runtime infrastructure used by LangChain |
| python-dotenv | Environment variable management |
| pytest | Automated testing |

The project's dependencies are defined in `requirements.txt`.

---

## 📁 Project Structure

```text
langchain-agent-project/
│
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   └── react_agent.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   └── math_tools.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── testes/
│   ├── __init__.py
│   └── test_agent.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

The repository separates the agent, configuration, tools, application entry point, and tests into dedicated modules.

---

## ⚙️ How It Works

### 1. Configuration

The project loads the OpenAI API key from an environment variable using `python-dotenv`.

```python
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

The application validates that the API key is available before starting.

### 2. Model

The agent uses OpenAI's `gpt-5.6` model through `ChatOpenAI`.

```python
model = ChatOpenAI(
    model="gpt-5.6",
    api_key=OPENAI_API_KEY
)
```

### 3. Tools

Two custom tools are available to the agent:

```python
@tool
def multiply(a: float, b: float) -> float:
    return a * b
```

and:

```python
@tool
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b
```

These functions are converted into LangChain tools using the `@tool` decorator.

### 4. Agent

The tools are registered with the agent:

```python
tools = [
    multiply,
    divide
]

agent = create_agent(
    model=model,
    tools=tools
)
```

This allows the LLM to decide when it needs to invoke one of the available tools.



