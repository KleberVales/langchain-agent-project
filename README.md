# langchain-agent-project

A hands-on Python project demonstrating how to build an AI agent with LangChain, an OpenAI language model, and custom tools.

The project focuses on the fundamental architecture of an agent: an LLM acts as the reasoning engine, while tools extend the agent's capabilities so it can perform actions instead of only generating text.

## 🧠 Overview

This project implements a simple ReAct-style agent using LangChain's agent framework.

The agent receives a natural-language request, determines which tool is required, executes the tool, and uses the result to produce the final answer.

For example:

Question: What is 15 multiplied by 8 and divided by 3?
