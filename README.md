# otto-mcp-client
Aviation Designer Assistant Demo

# ✈️ Otto Aviation MCP Client – Proof of Concept

This project demonstrates a Retrieval-Augmented Generation (RAG) platform designed to help Otto Aviation extract insights from internal documents using natural language queries.

## 🚀 Features

- Loads queries and context from `mcp_input.json`
- Reads multiple context files and assembles a prompt
- Simulates a response from an LLM (Ollama)
- Logs activity and saves responses to timestamped files
- Includes a Flask-based web UI with Otto-inspired styling

## 🧱 Folder Structure
mcp_client/
├── mcp_client.py

├── mcp_web_ui.py

├── mcp_input.json

├── otto_aviation_overview.txt

├── celera_technical_specs.txt

├── market_analysis_summary.txt

├── ollama_response_YYYYMMDD_HHMMSS.txt

├── mcp_client.log

├── venv/


## 🧪 Running Locally

### 1. Set up environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask

2. Run the CLI client
python mcp_client.py

3. Launch the web UI
python mcp_web_ui.py

Visit: http://127.0.0.1:5000

📊 Demo Queries

What are the aerodynamic advantages of the Celera aircraft?
How does Otto Aviation’s Celera reduce fuel consumption?
What makes the Celera design innovative?

🧠 Future Enhancements

Real LLM integration via Ollama or OpenAI
Secure document indexing
Authentication and user roles
CI/CD pipeline for deployment
