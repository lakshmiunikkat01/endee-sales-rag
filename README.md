# **Endee Sales & Demo RAG Assistant**

## **Project Overview**
This project is a **Retrieval-Augmented Generation (RAG) assistant** designed for internal sales and demo workflows.  
It allows users to upload documents once and ask natural-language questions instead of manually searching through folders.

The system uses **Endee as the vector database layer** for semantic retrieval and **Groq as the LLM** for generating answers strictly based on retrieved document content.

---

## **Problem Statement**
Sales teams and founders frequently receive repetitive questions related to product capabilities, scalability, and features.  
Manually searching internal documents such as FAQs and feature notes is inefficient and error-prone.

This project aims to:
- Retrieve answers directly from internal documents  
- Prevent hallucinated or unsupported answers  
- Clearly attribute the source of information  

---

## **System Design / Technical Approach**
The project follows a standard **Retrieval-Augmented Generation (RAG)** architecture:

Documents → Endee (Vector Retrieval) → Groq (Answer Generation)

### **Workflow**
1. Documents are ingested and indexed into Endee  
2. A user asks a question  
3. Endee retrieves relevant document content semantically  
4. Retrieved context is passed to Groq  
5. Groq generates an answer strictly from the provided context  
6. If the information is not present, the system explicitly states so  

The architecture is modular and production-oriented.

---

## **How Endee Is Used**
Endee is used as the **vector database abstraction** for semantic retrieval.

- Document text is stored in Endee with metadata during ingestion  
- User queries are matched against stored documents using semantic retrieval  
- Only retrieved content is passed to the LLM  

This ensures:
- Meaning-based retrieval  
- Explainable answers  
- No hallucination beyond uploaded documents  

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/lakshmiunikkat01/endee-sales-rag.git
cd endee-sales-rag
```  
### **2. Install Dependencies**

```bash
pip install groq python-dotenv
```  
### **3. Configure Environment Variables**
Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```  
### **4. Add Documents**

Place text files inside the following directory:

```text
data/docs/
```  
## **Execution Instructions**

### **Ingest Documents**

python src/ingest.py
python src/query.py


## **Example Questions**

- What is Endee designed for?
- Does Endee support semantic search?

If the answer is not explicitly present in the documents, the system responds accordingly.
## **Key Features**

- Retrieval-Augmented Generation (RAG)
- Endee-based semantic retrieval
- Groq-based answer generation
- Hallucination-safe responses
- Source attribution
- Incremental document ingestion
- CLI-based execution
## Conclusion

This project implements a simple and practical Retrieval-Augmented Generation (RAG) pipeline using Endee for semantic retrieval and Groq for answer generation.  
It demonstrates safe, source-grounded question answering over internal documents with a modular ingestion and query workflow suitable for real-world use cases.



This project demonstrates a practical RAG workflow using Endee for retrieval and Groq for generation.
It is designed with safety, explainability, and modularity in mind, aligning with real-world enterprise AI requirements.
