import os
import streamlit as st
import logging
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Configure secure logging matrix
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Set up Streamlit Page Configuration
st.set_page_config(page_title="Enterprise Agentic Workspace", page_icon="🛡️", layout="wide")
st.title("🛡️ Secure Enterprise Multi-Agent Workspace & RAG Core")
st.write("Production-grade isolated environment for vector ingestion and autonomous multi-agent code compilation.")

# 1. Thread-Safe Model Ingestion Layer
@st.cache_resource
def initialize_core_engines():
    try:
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        llm = ChatOllama(model="llama3:8b", temperature=0)
        return embeddings, llm
    except Exception as e:
        st.error(f"❌ Failed to bind local AI engines: {str(e)}")
        logging.critical("Ollama connection timeout or missing weights.")
        return None, None

embeddings, llm = initialize_core_engines()

if embeddings and llm:
    # 2. Secure File Ingestion Segment
    uploaded_file = st.file_uploader("📂 Ingest System Parameters Document (.txt):", type=["txt"])

    if uploaded_file is not None:
        try:
            file_contents = uploaded_file.read().decode("utf-8")
            st.info(f"💾 File loaded successfully: '{uploaded_file.name}'")
            
            # Persistent vector database location
            persist_directory = "./chroma_db"

            # 3. Secure Vector Space Initialization
            with st.spinner("Indexing vector matrices..."):
                vectorstore = Chroma.from_texts(
                    texts=[file_contents], 
                    embedding=embeddings,
                    persist_directory=persist_directory
                )
                retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

            # Vector Search Prompt Template
            template = """You are a precise corporate IT assistant. Use the following context to answer the question.
            Context: {context}
            Question: {question}
            Answer:"""
            prompt = ChatPromptTemplate.from_template(template)
            rag_chain = ({"context": retriever, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser())

            # Workspace Layout Split
            col1, col2 = st.columns(2)

            with col1:
                st.header("🔍 Direct Context Lookup")
                user_query = st.text_input("Query file metrics:")
                if user_query:
                    with st.spinner("Calculating semantic search vectors..."):
                        st.success(rag_chain.invoke(user_query))

            with col2:
                st.header("🚀 Autonomous Dev-Ops Micro-Team")
                st.write("Trigger sequential micro-agents to build and audit clean system code pipelines.")
                
                if st.button("⚡ Execute Micro-Team Pipeline"):
                    st.subheader("📡 Live Agent Pipeline Invocations:")
                    
                    # Dashboard Layout Containers
                    agent1_status = st.empty()
                    agent1_output = st.empty()
                    
                    agent2_status = st.empty()
                    agent2_output = st.empty()
                    
                    agent3_status = st.empty()
                    agent3_output = st.empty()

                    # --- AGENT 1: ANALYSIS ---
                    agent1_status.info("🧠 **[Agent 1: Requirements Specialist]** is compiling metrics...")
                    a1_prompt = ChatPromptTemplate.from_template(
                        "Extract the technical tasks, target directories, rules, and parameters mentioned in the text. "
                        "Format cleanly in bullet points.\n\nSource Data:\n{text}"
                    )
                    chain1 = a1_prompt | llm | StrOutputParser()
                    requirements = chain1.invoke({"text": file_contents})
                    agent1_status.success("✅ **Agent 1 Complete:** Parameters isolated.")
                    agent1_output.text_area("Agent 1 Analysis Log:", value=requirements, height=150)

                    # --- AGENT 2: COMPILATION ---
                    agent2_status.info("💻 **[Agent 2: Core Developer]** is compiling target code structures...")
                    a2_prompt = ChatPromptTemplate.from_template(
                        "Write a complete, functional Python script to handle the following requirements. "
                        "Implement robust error handling using try-except blocks, add logging, and verify directories exist before writing. "
                        "Return ONLY markdown-formatted code blocks.\n\nRequirements:\n{requirements}"
                    )
                    chain2 = a2_prompt | llm | StrOutputParser()
                    compiled_code = chain2.invoke({"requirements": requirements})
                    agent2_status.success("✅ **Agent 2 Complete:** Automated script compiled.")
                    agent2_output.text_area("Agent 2 Code Deployment Asset:", value=compiled_code, height=200)

                    # --- AGENT 3: PRODUCTION AUDIT ---
                    agent3_status.info("🛡️ **[Agent 3: QA & Security Auditor]** executing code risk evaluation...")
                    a3_prompt = ChatPromptTemplate.from_template(
                        "Review the following Python code for structural security vulnerabilities, permissions bugs, "
                        "and logical exceptions. Outline a short report using explicit sections: Syntax Errors, Logical Vulnerabilities, "
                        "and Deployment Verdict (PASS or FAIL).\n\nTarget Code:\n{code}"
                    )
                    chain3 = a3_prompt | llm | StrOutputParser()
                    audit_report = chain3.invoke({"code": compiled_code})
                    agent3_status.success("🎯 **Agent 3 Complete:** Security verification gate finalized.")
                    agent3_output.text_area("Agent 3 Compliance Audit Report:", value=audit_report, height=150)

        except Exception as file_error:
            st.error(f"⚠️ Structural error parsing uploaded document: {str(file_error)}")
            logging.error(f"Inbound stream processing failure: {str(file_error)}")
    else:
        st.warning("📥 System waiting for secure data transmission...")
