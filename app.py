from fastapi import FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session

from db import tables, engine

app = FastAPI()
@app.get("/first_task")
def first_task() -> list:
    sql_query = (select(tables['members'].c['surname'])
                 .distinct()
                 .where(tables['members'].c.memid != 0)
                 .order_by(tables['members'].c['surname'])
                 .limit(10))
    with Session(engine) as session:
        result = session.execute(sql_query).fetchall()
    result = [r[0] for r in result]
    return result

@app.get("/second_task")
def second_task() -> list:
    sql_query = (select(tables['members'].c.firstname,
                        tables['members'].c.surname,
                        tables['members'].c.joindate)
                 .order_by(tables['members'].c.joindate.desc())
                 .limit(1))
    with Session(engine) as session:
        result = session.execute(sql_query).fetchall()
    result = [{'firstname':  r[0],
               'surname': r[1],
               'joindate': r[2]}
              for r in result]
    return result

if __name__ == '__main__':
    resp = first_task()
    # resp = second_task()
    print(resp)

