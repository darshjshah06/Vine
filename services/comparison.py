from rag.retriever import retrieve
from llm.chains import ask_llm

def compare(wine_a: str, wine_b: str):

    docs_a = retrieve(wine_a)
    docs_b = retrieve(wine_b)

    context = "\n".join(docs_a + docs_b)

    return ask_llm(
        f"Compare {wine_a} and {wine_b}",
        context
    )