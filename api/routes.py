from fastapi import APIRouter

from services.recommendation import recommend
from services.pairing import pairing
from services.comparison import compare

router = APIRouter()

@router.get("/recommend")
def recommend_wine(query: str):

    return {
        "response": recommend(query)
    }

@router.get("/pairing")
def wine_pairing(food: str):

    return {
        "response": pairing(food)
    }

@router.get("/compare")
def compare_wines(
    wine_a: str,
    wine_b: str
):

    return {
        "response": compare(
            wine_a,
            wine_b
        )
    }