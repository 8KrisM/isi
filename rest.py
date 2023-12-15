from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
import utils

from algorithms import BFS

app = FastAPI()

class Item(BaseModel):
    maze: List[List[str]]


@app.post("/BFS")
async def BFS_endpoint(item: Item):
    response = await BFS(item.maze)
    return response
