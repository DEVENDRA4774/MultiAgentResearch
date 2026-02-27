# 🚀 Multi-Agent AI Research Assistant

Welcome! This folder contains a high-level overview of the Multi-Agent Research Assistant project. This project was built to demonstrate an understanding of **Agentic AI**—one of the most advanced technical trends of 2026.

## 🌟 The Elevator Pitch

Instead of a single AI model answering a prompt, this system orchestrates a **"Crew"** of specialized AI agents that collaborate and converse with one another to solve complex research requests. 

This mirrors modern software engineering pipelines:
1. **The Researcher:** Autonomously scours the live internet using the DuckDuckGo search engine to find raw data on a given topic.
2. **The Content Synthesizer:** Takes the unstructured data from the researcher and distills it into an executive summary.
3. **The Fact-Checker & Auditor:** Reviews the summary, performs independent web searches to verify the claims, flags any "Fake News," and produces a final cited report.

## 💡 Key Technologies Demonstrated

* **CrewAI Framework:** Used for defining Agents, assigning them Roles/Goals, and managing the sequential process flow.
* **Large Language Models (LLMs):** Powered by Google Gemini (`gemini-1.5-pro`) to provide the "reasoning" capability for each agent persona.
* **Tool Calling / RAG (Retrieval-Augmented Generation):** Integrated a live search tool (`langchain-community` DuckDuckGo wrapper) enabling the agents to interact with the real world rather than relying solely on training data.
* **Vector Databases & Memory:** CrewAI utilizes persistent and short-term memory (backed by ChromaDB) allowing the agents to retain context across tasks, learn from previous steps, and maintain state—crucial for complex problem-solving.
* **System Design:** A decoupled, modular architecture (`agents.py`, `tasks.py`, `tools.py`) ensuring easy scalability if new Agent roles need to be added in the future.

## 🎯 Why This Matters

This project proves an ability to move beyond basic chatbot APIs and build **autonomous systems**. It showcases skills in:
- AI Orchestration
- Prompt Engineering and Persona Definition
- Tool Integration (Search APIs)
- State Management and Memory Context Window handling

*Feel free to browse the `system_design.md` file in the root directory for a visual Mermaid diagram of the architecture flow!*
