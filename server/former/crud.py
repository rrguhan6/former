import os
import pathlib
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table,MetaData 
from sqlalchemy import text

basedir = pathlib.Path().absolute()
Base = automap_base()

_engine = create_engine('sqlite:///' + os.path.join(basedir, 'mydatabase.db'), echo=True)
Base.prepare(_engine, reflect=True)

def create_table(table_name , meta_data=None, engine = None):

    if(engine is None):
        engine = _engine

    table_name = f"table_{table_name}"
    _meta_data = {
        '__tablename__': table_name,
        'id': Column(Integer, primary_key=True, autoincrement=True),
    }
    for i in meta_data["components"]:
        if(i['type'] != "button"):
            _meta_data[i["key"]] = Column(String(100), unique=i["unique"], nullable=i["validate"]["required"])
    # breakpoint()
    type(table_name, (Base,), _meta_data)
    Base.metadata.create_all(engine)
    


def insert(table_name , data, engine = None):

    if(engine is None):
        engine = _engine

    meta = MetaData()

    ins = Table(table_name,meta,autoload=True, autoload_with=_engine).insert().values(**data)
    conn = _engine.connect()
    conn.execute(ins)


def get_all(table_name, engine=None):
    if(engine is None):
        engine = _engine
    # breakpoint()
    Session = sessionmaker(bind=_engine)
    session = Session()
    meta = MetaData()

    return session.query(Base.metadata.tables[table_name]).all()


def add_column(table_name, column, engine= None):
    if(engine is None):
        engine = _engine

    engine.execute(f'alter table {table_name} ADD {column["name"]} {column["datatype"]}')


# drop won't work in sqlite
def drop_column(table_name , column, engine=None):
    if(engine is None):
        engine = _engine

    engine.execute(f'alter table {table_name} DROP COLUMN {column}')

