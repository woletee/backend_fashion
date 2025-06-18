# outfit.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict, Optional
import random
import requests

router = APIRouter(prefix="/outfit", tags=["Outfit"])

WARDROBE_API_URL = "https://wardrobestudio.net/wardrobe/items"

class OutfitDay(BaseModel):
    day: str
    top: Optional[Dict] = None
    bottom: Optional[Dict] = None
    shoes: Optional[Dict] = None

@router.get("/weekly", response_model=List[OutfitDay])
async def generate_weekly_outfit():
    try:
        res = requests.get(WARDROBE_API_URL)
        wardrobe = res.json()
    except Exception as e:
        return []  # still returning a list to avoid crashing

    # Group wardrobe items by tag
    tops = [item for item in wardrobe if item.get("tag") == "top"]
    bottoms = [item for item in wardrobe if item.get("tag") == "bottom"]
    shoes = [item for item in wardrobe if item.get("tag") == "shoes"]

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekly_outfits = []

    for i in range(7):
        outfit = {"day": days[i]}
        if tops:
            outfit["top"] = random.choice(tops)
        if bottoms:
            outfit["bottom"] = random.choice(bottoms)
        if shoes:
            outfit["shoes"] = random.choice(shoes)
        weekly_outfits.append(outfit)

    return weekly_outfits
