# outfit.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict
import random
import requests

router = APIRouter(prefix="/outfit", tags=["Outfit"])

WARDROBE_API_URL = "https://wardrobestudio.net/wardrobe/items"

class OutfitDay(BaseModel):
    day: str
    top: Dict
    bottom: Dict
    shoes: Dict

@router.get("/weekly", response_model=List[OutfitDay])
async def generate_weekly_outfit():
    try:
        res = requests.get(WARDROBE_API_URL)
        wardrobe = res.json()
    except Exception as e:
        return {"error": f"Failed to fetch wardrobe: {e}"}

    # Organize items by tag
    tops = [item for item in wardrobe if item.get("tag") == "top"]
    bottoms = [item for item in wardrobe if item.get("tag") == "bottom"]
    shoes = [item for item in wardrobe if item.get("tag") == "shoes"]

    if not (tops and bottoms and shoes):
        return {"error": "Insufficient wardrobe items in one or more categories (top, bottom, shoes)."}

    # Build combinations and ensure uniqueness
    all_combos = [(t, b, s) for t in tops for b in bottoms for s in shoes]
    random.shuffle(all_combos)

    if len(all_combos) < 7:
        return {"error": "Not enough unique outfits to generate a full week."}

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekly_outfits = [
        {
            "day": days[i],
            "top": combo[0],
            "bottom": combo[1],
            "shoes": combo[2],
        }
        for i, combo in enumerate(all_combos[:7])
    ]

    return weekly_outfits
