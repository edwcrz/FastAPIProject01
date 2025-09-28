from fastapi import APIRouter, HTTPException, WebSocketException 
from pydantic import BaseModel

router_instance = APIRouter()
@router_instance.get("/products")
async def get_products():
    return {"products": ["product 1", "product 2", "product 3", "product 4", "product 5"]}  