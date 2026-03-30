# 🚀 GCP Release Notes Intelligence Agent (Track 2)

A production-grade AI agent system architected with the **Agent Development Kit (ADK)** and the **Model Context Protocol (MCP)**. This project automates the complex task of monitoring and analyzing the Google Cloud ecosystem by bridging natural language reasoning with a BigQuery data warehouse.

## 🏗️ Architecture
This project follows a secure, decoupled architecture consisting of two serverless services on **Google Cloud Run**:

1.  **Reasoning Layer (ADK Agent):** A Python-based agent powered by `gemini-2.5-flash` on Vertex AI. It acts as the "Brain," interpreting user intent and orchestrating tool calls.
2.  **Tooling Layer (MCP Server):** A standalone instance of the **Google MCP Toolbox for Databases**. This service handles the secure connection to BigQuery, exposing structured SQL operations as standardized MCP tools.



## 🛠️ Tech Stack
* **Orchestration:** [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/)
* **Protocol:** [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
* **Intelligence:** Gemini 2.5 Flash via Vertex AI
* **Compute:** Google Cloud Run (Serverless Containers)
* **Data Warehouse:** BigQuery Public Datasets (`bigquery-public-data.google_cloud_release_notes`)

## ✨ Key Features
* **Autonomous Multi-Step Reasoning:** The agent can "chain" tools. For example, it first fetches temporal data and then filters by keyword to provide highly specific audits.
* **Automated Categorization:** Automatically labels updates as **🚨 Security**, **✨ Feature Update**, or **ℹ️ Announcement**.
* **Impact Analysis:** Goes beyond raw data to explain *why* an update matters to a Cloud Engineer or Architect.

## 🧪 Winning Demo Prompts
Test the agent's intelligence at the [Live Agent UI](https://release-notes-agent-903731837352.asia-south1.run.app):

1.  **Security Audit:** *"I need a security audit for GKE and Compute Engine. Find all 'SECURITY_BULLETIN' updates from the last 30 days and summarize them."*
2.  **Product Roadmap:** *"What are the most impactful 'Feature Updates' for Cloud Run and Vertex AI from the last 60 days?"*
3.  **Regional Awareness:** *"Check for any service migrations or updates specifically mentioning the Melbourne (asia-southeast2) region."*

## 🚀 Live Endpoints
* **Agent Web UI:** [https://release-notes-agent-903731837352.asia-south1.run.app](https://release-notes-agent-903731837352.asia-south1.run.app)
* **MCP Server API:** [https://release-notes-toolbox-903731837352.asia-south1.run.app](https://release-notes-toolbox-903731837352.asia-south1.run.app)

## 💻 Repository Structure
```text
hack-to-skill-track2-mcp/
├── release_notes_agent/
│   ├── agent.py          # ADK Agent definition with reasoning logic
│   └── __init__.py       # Package initialization for ADK discovery
├── toolbox/
│   ├── tools.yaml        # MCP Toolbox configuration & SQL definitions
│   └── Dockerfile        # Container config for official Toolbox image
├── Dockerfile            # Root Dockerfile for the ADK Agent
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

📝 Problem Statement (Track 2)
"Keeping up with the fast-paced Google Cloud ecosystem is a manual, time-consuming task. I built an AI agent that integrates Gemini's reasoning capabilities with BigQuery using the Model Context Protocol (MCP). By separating tool execution from AI reasoning, this project demonstrates a secure, scalable, and standardized way to connect LLMs to real-world data sources."

🧹 Cleanup
To avoid recurring costs after evaluation:
```Bash
gcloud run services delete release-notes-agent --region asia-south1
gcloud run services delete release-notes-toolbox --region asia-south1
```
