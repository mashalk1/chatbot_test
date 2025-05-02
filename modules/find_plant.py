from fastapi import APIRouter
from typing import Dict, List, Any

router = APIRouter()

# Sample plant database with English values but maintaining database structure
PLANT_DATABASE = [
    {"name": "Sansevieria", "location": "indoor", "size": "medium", "style": "modern", "image": "image5.png"},
    {"name": "Ficus Lyrata", "location": "indoor", "size": "large", "style": "minimalist", "image": "image8.png"},
    {"name": "Palm Tree", "location": "outdoor", "size": "large", "style": "tropical", "image": "image9.png"},
    {"name": "Epipremnum", "location": "office", "size": "small", "style": "modern", "image": "image10.png"},
    {"name": "Aloe Vera", "location": "indoor", "size": "small", "style": "modern", "image": "image1.png"},
    {"name": "Calathea", "location": "indoor", "size": "medium", "style": "minimalist", "image": "image2.png"},
    {"name": "Dracaena", "location": "office", "size": "large", "style": "minimalist", "image": "image3.png"},
    {"name": "Monstera", "location": "office", "size": "large", "style": "tropical", "image": "image4.png"},
    {"name": "Begonia", "location": "indoor", "size": "small", "style": "modern", "image": "image6.png"},
    {"name": "Zamioculcas", "location": "office", "size": "medium", "style": "modern", "image": "image7.png"}
]

@router.post("/find_plant")
def find_plant(user_input: Dict[str, str]) -> List[Dict[str, Any]]:
    # Expected input: {"location": "office", "size": "small", "style": "modern"}
    location = user_input.get("location", "").lower()
    size = user_input.get("size", "").lower()
    style = user_input.get("style", "").lower()

    matching_plants = [
        plant for plant in PLANT_DATABASE
        if plant["location"] == location and plant["size"] == size and plant["style"] == style
    ]
    
    if not matching_plants:
        return [{"message": "Sorry, no perfect match found! Try adjusting your preferences."}]
    
    return matching_plants[:5]
