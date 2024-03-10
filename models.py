from pydantic import BaseModel

class sixth(BaseModel):
    member: str | None = None
    facility: str | None = None
    cost: float | None = None
