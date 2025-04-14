# 🕶️ Project SHADOW: Secure Hybrid Agentic Document-Oriented Retrieval System
Project SHADOW is a secure, modular intelligence retrieval system designed for classified operationsIt integrates Retrieval-Augmented Generation (RAG) techniques with agent-level access control, combining vector similarity and graph-based retrieval to provide transparent and justified responses to intelligence queries

---

## 📁 Project Structure
```
soodaryan-kg/
├── README.md
├── agentic_workflow.py       # Orchestrates the end-to-end agent query workflow
├── baseModels.py             # Embedding models and vector store interfaces
├── config.py                 # Configuration settings and constants
├── document_processor.py     # Preprocessing, chunking, and embedding of documents
├── graph_utils.py            # Constructs and traverses the knowledge graph
├── main.py                   # Entry point for the application
├── prompts.py                # Prompt templates for LLM interactions
├── requirements.txt          # Python dependencies
└── data/
    ├── frameworks.txt        # Response framework document
    ├── sample_data.txt       # Sample queries and responses
    └── secret_manual.txt     # Secret information manual
``
---

## 🚀 Features

- **Agent-Level Access Control*: Ensures responses are tailored to the agent's clearance level, denying access when necessay.
- **Hybrid Retrieval Mechanism**:
  - **Vector Similarity*: Retrieves contextually relevant information using embeddins.
  - **Graph Traversal*: Explores interconnected data points for comprehensive contet.
  - **Hybrid Approach*: Combines both methods for complex queris.
- **Transparent Justifications*: Provides clear explanations for retrieved information, including sources and retrieval methos.
- **Structured Responses*: Delivers answers formatted according to the agent's level and query tye.
- **Error Handling*: Returns appropriate messages when data is inaccessible or not foud.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/soodaryan-kg.git
   cd soodaryan-kg
   ``

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ``

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ``

---

## 🧪 Usage

1. **Prepare Documents**:
  - Place `secret_manual.txt` and `frameworks.txt` in the `data/` direcory.

2. **Run the Application**:
   ```bash
   python main.py
  ```

3. **Interact with the System**:
  - Input your agent level when promted.
  - Submit your classified qery.
  - Receive a structured, justified response based on the provided documnts.

---

## 🧩 Modules Overview

- **`agentic_workflow.p`**: Manages the overall workflow from query input to response genertion.
- **`baseModels.p`**: Handles embedding generation and vector store interacions.
- **`document_processor.p`**: Processes and chunks documents, generating embeddings for each hunk.
- **`graph_utils.p`**: Constructs a knowledge graph from document data and facilitates traversal for related informtion.
- **`prompts.p`**: Contains templates for prompting the language model, customized per agent level and querytype.

---

## 🔐 Security Protocols

- **Access Contol**: Validates agent level against document clearance requirments.
- **Error Messages*:
  - If access is denied: `Access Denied – Clearance Insuffiient.`
  - If no matching data is found: `Oops!! No matching data ound.`

---

## 📄 Prompt Structure

- **Variables**:
  - `Agent evel`: Determines the depth and sensitivity of the rsponse.
  - `QueryType`: Classifies the nature of the query to select appropriate response teplates.
  - `Retrieved Cotext`: Incorporates relevant information from documents into theprompt.

- **Response Formatting*:
  - Tailored to the agent's clearance level, ensuring appropriate detail and senstivity
  - Includes citations and justifications for each piece of information povided.

---

## 🧠 Retrieval Strategy

- **Vector Similarit**:
  - Utilizes embeddings to find semantically similar documen chunk.
  - Efficient for direct queries with clearcontext.

- **Graph Traversa**:
  - Explores relationships between entities and concepts within the knowlede grap.
  - Ideal for complex queries requiring interconnected infrmation.

- **Hybrid Approac**:
  - Combines both methods to enhance retrieval accuracy and context ichness.

---

## ⚖️ Trade-offs & Design Decisions

- **Chunking Strateg**:
  - Balanced chunk size to maintain context without overwhelming the retrieva system.

- **Embedding Model Selectio**:
  - Chosen for optimal performance on intelligence-related txt data.

- **Graph Constructio**:
  - Designed to capture meaningful relationships without excessive coplexity.

- **Security vs. Accessibilit**:
  - Implemented strict access controls to protect sensitive information while ensuring usability for authorize agents.

---

## 🌟 Bonus Features

- **Advanced Chunking & Storae**:
  - Implements overlapping chunks and metadata tagging for improved retrieval recision.

- **Intelligent Query Mapping 