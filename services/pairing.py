from rag.retriever import retrieve
from llm.chains import ask_llm

def pairing(food: str):

    docs = retrieve(food)

    context = "\n".join(docs)

    return ask_llm(
        f"What wine pairs with {food}?",
        context
    )