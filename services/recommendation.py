from rag.retriever import retrieve
from llm.chains import ask_llm

def recommend(query: str):

    docs = retrieve(query)

    context = "\n".join(docs)

    return ask_llm(
        f"Recommend a wine for: {query}",
        context
    )