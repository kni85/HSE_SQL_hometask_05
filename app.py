from fastapi import FastAPI

from sqlalchemy import select, and_, func, union_all
from sqlalchemy.orm import Session

from db import tables, engine

from typing import List
import models

app = FastAPI()

@app.get("/first_task", response_model=List[models.first])
def first_task() -> list:
    sql_query = (select(tables['members'].c['surname'])
                 .distinct()
                 .where(tables['members'].c.memid != 0)
                 .order_by(tables['members'].c['surname'])
                 .limit(10))
    with Session(engine) as session:
        result = session.execute(sql_query).fetchall()
    return result

@app.get("/second_task", response_model=List[models.second])
def second_task():
    sql_query = (select(tables['members'].c.firstname,
                        tables['members'].c.surname,
                        tables['members'].c.joindate)
                 .order_by(tables['members'].c.joindate.desc())
                 .limit(1))

    with Session(engine) as session:
        result = session.execute(sql_query).fetchall()

    return result

@app.get("/third_task", response_model=List[models.third])
def third_task():
    sql_query = (select(tables['bookings'].c.starttime,
                        tables['facilities'].c.name.label('facility_name'))
                 .join(tables['facilities'])
                 .where(and_(tables['bookings'].c.starttime >= '2012-09-21',
                             tables['bookings'].c.starttime < '2012-09-22'))
                 .order_by(tables['bookings'].c.starttime))

    with Session(engine) as session:
        result = session.execute(sql_query).fetchall()

    return result

@app.get("/fourth_task", response_model=List[models.fourth])
def fourth_task():
    m = tables['members'].alias()
    mm = tables['members'].alias()

    sql_query = (select(m.c.firstname,
                        m.c.surname,
                        mm.c.firstname.label('recomendedby_name'),
                        mm.c.surname.label('recomendedby_surname'))
                 .join(mm, m.c.recommendedby == mm.c.memid, isouter=True)
                 .where(m.c.memid != 0)
                 .order_by(m.c.firstname, m.c.surname))

    with Session(engine) as session:
        result = session.execute(sql_query).fetchall()

    return result

@app.get("/fifth_task", response_model=List[models.fifth])
def fifth_task():
    b = tables['bookings'].alias()
    sql_query = (select(b.c.facid, func.sum(b.c.slots).label('Total_slots'))
                 .where(and_(b.c.starttime >= '2012-09-01',
                             b.c.starttime < '2012-10-01'))
                 .group_by(b.c.facid)
                 .order_by('Total_slots'))

    with Session(engine) as session:
        result = session.execute(sql_query).fetchall()

    return result

@app.get("/sixth_task", response_model=List[models.sixth])
def sixth_task():

    b = tables['bookings'].alias()
    m = tables['members'].alias()
    f = tables['facilities'].alias()

    data1 = (select(m.c.memid,
                    func.concat(m.c.firstname, ' ', m.c.surname).label('member'),
                    b.c.slots,
                    f.c.name.label('facility'),
                    f.c.membercost,
                    f.c.guestcost)
             .join(m, m.c.memid == b.c.memid)
             .join(f, f.c.facid == b.c.facid)
             .where(and_(b.c.starttime >= '2012-09-14',
                         b.c.starttime < '2012-09-15'))
             .cte())

    members = (select(data1.c.member,
                      data1.c.facility,
                      (data1.c.slots * data1.c.membercost).label('cost'))
               .where(data1.c.memid != 0))

    guests = (select(data1.c.member,
                     data1.c.facility,
                     (data1.c.slots * data1.c.guestcost).label('cost'))
              .where(data1.c.memid == 0))

    costs = union_all(guests, members).cte()

    sql_query = (select(costs)
                 .where(costs.c.cost > 30)
                 .order_by(costs.c.cost.desc()))

    with Session(engine) as session:
        result = session.execute(sql_query).fetchall()

    return result

if __name__ == '__main__':

    resp = first_task()
    print('First task responds with the following:')
    print(resp)

    resp = second_task()
    print('Second task responds with the following:')
    print(resp)

    resp = third_task()
    print('Third task responds with the following:')
    print(resp)

    resp = fourth_task()
    print('Fourth task responds with the following:')
    print(resp)

    resp = fifth_task()
    print('Fifth task responds with the following:')
    print(resp)

    resp = sixth_task()
    print('Sixth task responds with the following:')
    print(resp)
