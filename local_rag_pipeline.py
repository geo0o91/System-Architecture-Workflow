import os
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma  # Clean integration package without warnings!
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. Initialize our local Llama3 Chat Engine and dedicated Nomic Embedding model
print("🤖 Initializing Local Llama3 Chat Engine & Nomic Embeddings...")
embeddings = OllamaEmbeddings(model="nomic-embed-text")
llm = ChatOllama(model="llama3:8b", temperature=0)

# 2. Setup directory and read data
source_dir = "knowledge_source"
if not os.path.exists(source_dir):
    os.makedirs(source_dir)

# Create a clean data file if the folder is completely empty
if not os.listdir(source_dir):
    with open(os.path.join(source_dir, "sample.txt"), "w") as f:
        f.write("George B is a WES-certified Computer Engineer based in Ottawa, Canada, specializing in AI Agent architectures and automated systems.")

# Read text documents from the folder
documents = []
for file in os.listdir(source_dir):
    if file.endswith(".txt"):
        with open(os.path.join(source_dir, file), "r", encoding="utf-8") as f:
            documents.append(f.read())

print(f"📄 Successfully ingested {len(documents)} document(s) from local storage.")

# 3. Create Vector Database (ChromaDB) in memory using the proper embeddings model
print("🗄️ Vectorizing data and building local ChromaDB database...")
vectorstore = Chroma.from_texts(
    texts=documents,
    embedding=embeddings
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

# 4. Construct the RAG Prompt Template
template = """You are a highly precise Technical Assistant. Answer the user's question using ONLY the following context. If you do not know the answer based on the context, say 'Information not found'.

Context:
{context}

Question: {question}
Answer:"""

prompt = ChatPromptTemplate.from_template(template)

# 5. Build the LangChain Execution Chain (LCEL)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 6. Execute a live query against your private documents
query = "What is George B's specific engineering background and where is he located?"
print(f"\n❓ Querying System: '{query}'")

print("\n================== LOCAL RAG OUTPUT ==================")
response = rag_chain.invoke(query)
print(response)
print("=========================================================")
