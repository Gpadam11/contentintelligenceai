# Jargon Buster (SentinelFlow AI) 🚀

**A multi-agent semantic translation layer for technical documentation.**
*Built for the Economic Times GenAI Hackathon.*

---

## 🌐 Live Demo
**Access the deployed application here:** https://jargon-buster-final-692493868742.us-central1.run.app/dev-ui/?app=personal_assistant&session=c005b183-8403-47a7-b534-1eb04aa53f1f&userId=user

---

## 📖 Overview
Jargon Buster (SentinelFlow AI) bridges the gap between complex technical documentation and non-technical stakeholders. By utilizing a multi-agent architecture, it intelligently parses, translates, and simplifies dense industry jargon into clear, actionable, and accessible language without losing the core technical meaning. 

## ✨ Key Features
* **Multi-Agent Architecture:** Utilizes specialized AI agents working in tandem to analyze and translate content accurately.
* **Semantic Translation:** Goes beyond simple keyword replacement to understand the context and intent of technical documents.
* **Zero-Hallucination Focus:** Grounded in retrieval and strict system prompts to ensure the translated output remains factually accurate to the source material.
* **Intuitive Interface:** Designed for seamless user interaction, allowing rapid processing of documents or text snippets.

## 🛠️ Tech Stack
* **LLM Engine:** Google Gemini APIs
* **Cloud Infrastructure:** Google Cloud Platform (GCP)
* **Backend:** Python
* **Agentic Framework:** Custom Multi-Agent Tooling

## 🚀 Getting Started (Local Development)

### Prerequisites
* Python 3.10+
* Google Cloud Project with Vertex AI / Gemini API access enabled
* `.env` file configured with your API keys

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Gpadam11/contentintelligenceai.git](https://github.com/Gpadam11/contentintelligenceai.git)
   cd contentintelligenceai

### Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
### Install dependencies:
pip install -r requirements.txt
### Run the code:
python personal_assistant/agent.py
