from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from sqlalchemy import Table
from db_key import URL

schema_name = 'cd'
engine = create_engine(URL, echo=False)
metadata_obj = MetaData(schema = schema_name)
metadata_obj.reflect(engine)

tables = {}
for table_name in metadata_obj.tables:
    t_name = table_name[len(schema_name) + 1: ]
    tables[t_name] = Table(t_name, metadata_obj, autoload=True)

if __name__ == '__main__':

    # test 1st task
    from sqlalchemy import select
    from sqlalchemy.orm import Session

    sql_query = select(tables['members'].c['surname']).distinct()
    sql_query = sql_query.where(tables['members'].c.memid != 0)
    sql_query = sql_query.order_by(tables['members'].c['surname']).limit(10)

    with Session(engine) as session:
        result = session.execute(sql_query).fetchall()

    for res in result:
        print(res[0])

    print(type(result))
    print(list(result))
    print(result)
