\# Secure Enterprise Multi-Agent Workspace \& RAG Portal



An enterprise-grade, production-patterned \*\*Retrieval-Augmented Generation (RAG)\*\* web application and \*\*3-Agent Autonomous Workspace\*\*. This application operates \*\*100% locally and securely offline\*\*, ensuring zero data leakage, zero API costs, and complete privacy for sensitive corporate data layers.



\## 🏗️ System Architecture \& Workflow



\[ Ingest .txt Parameter File ]

│

▼

┌─────────────────────────┐

│  Nomic Embed Text Core  │ ──► Indexes Matrix into Local ChromaDB

└─────────────────────────┘

│

┌───────┴────────────────────────┐

▼                                ▼

\[ 🔍 Direct Vector RAG Search ]   \[ 🚀 Sequential 3-Agent Micro-Team ]

│

▼

Agent 1: Requirements Specialist (Analysis)

│

▼

Agent 2: Core Developer (Python Compilation)

│

▼

Agent 3: QA \& Security Auditor (Audit Gate)



\## 🛠️ The Production Stack

\*   \*\*Engine Ingestion Layer:\*\* Python 3.11 with localized virtual environment containment.

\*   \*\*Interface Dashboard Framework:\*\* Streamlit UI for high-performance internal tooling dashboards.

\*   \*\*Local AI Orchestration \& Logic Gates:\*\* LangChain (LCEL) routing pipeline states.

\*   \*\*Vector Database Architecture:\*\* ChromaDB (`langchain-chroma`) managing localized on-disk storage.

\*   \*\*Local LLM Hardware Server:\*\* Ollama running open-source parameter weights natively.

\*   \*\*Active Intelligence Models:\*\* `llama3:8b` (Reasoning/Generation Engine) and `nomic-embed-text` (Mathematical String Embedding Engine).



\## 🛡️ Production-Grade Implementation Features

\*   \*\*Robust Error Handling:\*\* Built-in validation blocks (`try-except`) wrapping file processing arrays and model bindings to secure system uptimes.

\*   \*\*Local Compliance Audit Gate:\*\* Integrated a Senior QA Auditor agent loop that runs static analysis on compiled code to ensure error-catching, permission checks, and safety constraints are verified before a deployment verdict is issued.

\*   \*\*Modular Architecture:\*\* Complete isolation of sensitive data stores via strict `.gitignore` schemas to ensure local database configurations are kept separate from code repositories.



\## 🏃‍♂️ Local Deployment Instructions



\### Prerequisites

Ensure you have \*\*Ollama\*\* installed locally and the target model tags pulled:

```bash

ollama pull llama3:8b

ollama pull nomic-embed-text



\### Installation



pip install -r requirements.txt



\### Execution



streamlit run app.py



