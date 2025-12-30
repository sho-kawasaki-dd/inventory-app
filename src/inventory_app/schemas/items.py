from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ItemCreate(BaseModel):
    sku: str | None = None
    name: str
    unit: str = "pcs"
    category: str | None = None
    usage: str | None = None
    manufacturer: str | None = None


class ItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    sku: str | None
    name: str
    unit: str
    category: str | None
    usage: str | None
    manufacturer: str | None
