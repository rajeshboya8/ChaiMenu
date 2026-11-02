from fastapi import FastAPI, Query, HTTPException
from models import MenuItem, MenuResponse
from data import menu_items

app = FastAPI(
    title = "Chai Point Menu API",
    description = "This is a simple API for Chai Point Menu",
)

@app.get("/")

def root():
    return {"message": "Welcome to Chai Point Menu API!"}

@app.get("/menu", response_model=MenuResponse)
def get_menu_items(category: str = Query(None, description="Filter menu items by category")):
    if category:
        filtered_items = [item for item in menu_items if item["category"].lower() == category.lower()]
        if not filtered_items:
            raise HTTPException(status_code=404, detail="No menu items found for the specified category.")
        return MenuResponse(count=len(filtered_items), items=filtered_items)
    return MenuResponse(count=len(menu_items), items=menu_items)

@app.get("/menu/{item_id}", response_model=MenuItem)
def get_menu_item(item_id: int):
    item = next((item for item in menu_items if item["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found.")
    return item