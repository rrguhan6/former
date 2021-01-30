import os
import pathlib
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table,MetaData 
from sqlalchemy.engine import reflection
import time

start = time.time()

basedir = pathlib.Path().absolute()
Base = declarative_base()

table_name = "newtable2"

engine = create_engine('sqlite:///' + os.path.join(basedir, 'mydatabase3.db'), echo=True)

Test = type(table_name, (Base,), {'__tablename__': table_name,'test_id': Column(Integer, primary_key=True, autoincrement=True),'name': Column(String(80), unique=False, nullable=False),})

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
meta = MetaData()

# data = {
#     "name":"guhan"
# }

# # for i in range(1000):
# #     ins = Table('test',meta,autoload=True, autoload_with=engine).insert().values(**data)
# #     conn = engine.connect()
# #     conn.execute(ins)


ins = Table(table_name,meta,autoload=True, autoload_with=engine).insert().values(name="guhwean")
conn = engine.connect()
conn.execute(ins)


# ins = Table(table_name,meta,autoload=True, autoload_with=engine).insert().values(name="guhan")
# conn = engine.connect()
# conn.execute(ins)

print(session.query(Base.metadata.tables[table_name]).filter_by(name='guhan'))

print(session.query(Base.metadata.tables[table_name]).all())

end = time.time()

print(end - start)