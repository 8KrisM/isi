from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import utils

from algorithms import BFS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    maze: List[List[str]]


@app.post("/BFS")
async def BFS_endpoint(item: Item):
    response = await BFS(item.maze)
    return response
