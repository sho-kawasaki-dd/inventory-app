from __future__ import annotations

from pydantic import BaseModel


class StocktakeCreate(BaseModel):
    title: str
