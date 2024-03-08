# from typing import List
from fastapi import FastAPI #, Depends
# from sqlalchemy.orm import Session
# from typing import Any
# from pydantic import BaseModel

# class FirstItem(BaseModel):
#     name: str

from tasks import first

# resp = first()
# print(resp)

app = FastAPI()

@app.get("/first_task")
def f():
    resp = first()
    return resp


#
#
# def get_session():
#     with SessionLocal() as session:
#         return session
#
#
# @app.get("/user/all", response_model=List[UserGet])
# def get_all_users(limit: int = 10, db: Session = Depends(get_session)):
#     return db.query(Member).limit(limit).all()
#
#
# @app.get("/facility/all")
# def get_all_facilities(limit: int = 1, db: Session = Depends(get_session)):
#     return db.query(Facility).limit(limit).all()
#
#
# @app.get("/booking/all", response_model=List[BookingGet])
# def get_all_bookings(limit: int = 10, db: Session = Depends(get_session)):
#     return db.query(Booking).limit(limit).all()
