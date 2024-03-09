from sqlalchemy import select
from sqlalchemy.orm import Session

from db import tables, engine

def first():
    sql_query = select(tables['members'].c['surname']).distinct()
    sql_query = sql_query.where(tables['members'].c.memid != 0)
    sql_query = sql_query.order_by(tables['members'].c['surname']).limit(10)

    with Session(engine) as session:
        result = session.execute(sql_query).fetchall()
    result = [r[0] for r in result]
    return result

if __name__ == '__main__':
    resp = first()
    print(resp)