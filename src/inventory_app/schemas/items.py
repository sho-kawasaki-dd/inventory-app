from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ItemCreate(BaseModel):
    sku: str | None = None
    name: str
    unit: str = "pcs"


class ItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    sku: str | None
    name: str
    unit: str
