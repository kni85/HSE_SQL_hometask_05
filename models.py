from pydantic import BaseModel
from datetime import datetime

class first(BaseModel):
    surname: str | None = None

class second(BaseModel):
    firstname: str | None = None
    surname: str | None = None
    joindate: datetime | None = None

class third(BaseModel):
    starttime: datetime | None = None
    facility_name: str | None = None

class fourth(BaseModel):
    firstname: str | None = None
    surname: str | None = None
    recomendedby_name: str | None = None
    recomendedby_surname: str | None = None

class fifth(BaseModel):
    facid: int | None = None
    Total_slots: int | None = None

class sixth(BaseModel):
    member: str | None = None
    facility: str | None = None
    cost: float | None = None
