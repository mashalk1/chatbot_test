from fastapi import APIRouter
import openai
import os

router = APIRouter()

# Predefined maintenance tips in English
maintenance_tips = {
    "cleaning": "Use a soft cloth or duster to remove dust. For more thorough cleaning, use mild soap and water.",
    "uv_protection": "To prevent fading, place artificial plants in shaded areas or use a UV-resistant spray.",
    "duurzaam": "Our plants are made from environmentally friendly materials. Consider reusing old plants instead of throwing them away."
}

@router.get("/maintenance/{topic}")
def get_maintenance_tips(topic: str):
    topic = topic.lower()
    if topic in maintenance_tips:
        return {
            "message": f"Here's what you need to know about {topic.replace('_', ' ')}:",
            "tip": maintenance_tips[topic]
        }
    else:
        return {
            "message": "Sorry, I don't have information on this topic. Try cleaning, uv_protection, or durability."
        }

@router.get("/maintenance/plant/{plant_name}")
def get_plant_maintenance(plant_name: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert on plant maintenance."},
            {"role": "user", "content": f"How do I maintain {plant_name}?"}
        ]
    )
    
    tip = response["choices"][0]["message"]["content"]
    return {
        "message": f"Here's what you need to know about maintaining {plant_name}:",
        "tip": tip
    }

# Ensure compatibility with app.py
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
