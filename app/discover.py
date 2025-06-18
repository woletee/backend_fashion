from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
import requests
from utils.model_utils import predict_image
from utils.recommender import get_recommendations_with_images

router = APIRouter(prefix="/discover", tags=["Discover"])

class WardrobeRequest(BaseModel):
    image_urls: List[str]

@router.post("/")
async def discover_recommendations(request: WardrobeRequest):
    detected_items = []

    for url in request.image_urls:
        try:
            res = requests.get(url)
            if res.status_code == 200:
                detected = predict_image(res.content)
                print(f"✅ Detected from image: {detected}")
                detected_items.append(detected)
            else:
                print(f"❌ Failed to fetch image: {url}")
        except Exception as e:
            print(f"❌ Exception while processing {url}: {e}")

    print("📦 Final Detected Items:", detected_items)

    if not detected_items:
        print("⚠️ No items detected — fallback triggered")
        detected_items = ["shirt"]  # You can use any default known type

    recommendations = get_recommendations_with_images(detected_items)
    print("🧠 Final Recommendations:", recommendations)
    return recommendations
