from fastapi import APIRouter, HTTPException
from typing import List, Dict
import os

router = APIRouter()

# Updated Base URL for serving images on Railway production
BASE_IMAGE_URL = os.getenv("BASE_IMAGE_URL", "https://chatbottest-production.up.railway.app/static/images/")

# Updated product data with English names, heights, and categories
PRODUCTS = {
    "Indoor": [
        {"id": 1, "name": "Artificial lemon tree", "price": 49.99, "stock": 5, "image": "image1.png", "height": "150 cm"},
        {"id": 2, "name": "Artificial olive tree", "price": 39.99, "stock": 2, "image": "image2.png", "height": "180 cm"},
        {"id": 3, "name": "Philodendron artificial plant", "price": 29.99, "stock": 6, "image": "image3.png", "height": "180 cm"},
        {"id": 4, "name": "Philodendron artificial vine", "price": 34.99, "stock": 4, "image": "image4.png", "height": "180 cm"},
        {"id": 5, "name": "Artificial banana plant", "price": 44.99, "stock": 3, "image": "image5.png", "height": "180 cm"},
    ],
    "Office": [
        {"id": 6, "name": "Artificial palm", "price": 59.99, "stock": 3, "image": "image6.png", "height": "180 cm"},
        {"id": 7, "name": "Artificial banana plant", "price": 49.99, "stock": 5, "image": "image7.png", "height": "120 cm"},
        {"id": 8, "name": "2-piece philodendron artificial plants", "price": 39.99, "stock": 2, "image": "image8.png", "height": "150 cm"},
        {"id": 9, "name": "Artificial eucalyptus plant", "price": 29.99, "stock": 6, "image": "image9.png", "height": "180 cm"},
        {"id": 10, "name": "Strelitzia artificial plant", "price": 34.99, "stock": 4, "image": "image10.png", "height": "120 cm"},
    ],
    "Outdoors": [
        {"id": 11, "name": "Japanese rose artificial plant", "price": 44.99, "stock": 3, "image": "image10.png", "height": "180 cm"},
        {"id": 12, "name": "Artificial olive tree", "price": 59.99, "stock": 3, "image": "image3.png", "height": "120 cm"},
        {"id": 13, "name": "Artificial eucalyptus plant", "price": 29.99, "stock": 6, "image": "image1.png", "height": "180 cm"},
        {"id": 14, "name": "Artificial banana plant", "price": 39.99, "stock": 2, "image": "image6.png", "height": "120 cm"},
        {"id": 15, "name": "Strelitzia artificial plant", "price": 34.99, "stock": 4, "image": "image8.png", "height": "180 cm"},
    ],
}

@router.get("/products/categories")
def get_categories() -> Dict[str, List[str]]:
    """
    Returns available product categories.
    """
    return {"categories": list(PRODUCTS.keys())}

@router.get("/products/list")
def get_products(category: str, limit: int = 5) -> Dict:
    """
    Fetches products from a selected category with an optional limit.
    """
    if category not in PRODUCTS:
        raise HTTPException(status_code=404, detail="Category not found")

    products = PRODUCTS[category][:limit]  # Limit number of products returned

    return {
        "message": f"Here are our top picks in {category}.",
        "products": [
            {
                "id": p["id"],
                "name": p["name"],
                "price": f"€{p['price']:.2f}",
                "stock": f"{p['stock']} in stock",
                "height": p["height"],
                "image": f"{BASE_IMAGE_URL}{p['image']}"
            }
            for p in products
        ],
        "actions": ["View more", "Help me choose", "See all"]
    }

@router.get("/products/all")
def get_all_products() -> Dict:
    """
    Returns all products from all categories.
    """
    all_products = []
    for category in PRODUCTS.values():
        all_products.extend(category)
    return {
        "message": "Here are all our products.",
        "products": [
            {
                "id": p["id"],
                "name": p["name"],
                "price": f"€{p['price']:.2f}",
                "stock": f"{p['stock']} in stock",
                "height": p["height"],
                "image": f"{BASE_IMAGE_URL}{p['image']}"
            }
            for p in all_products
        ]
    }
