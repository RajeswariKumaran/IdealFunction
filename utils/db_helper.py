import pandas as pd
from dotenv import load_dotenv
import os
import sqlalchemy as db
import pymysql


load_dotenv()
global connection_string
connection_string = os.getenv('connection_string')
 
def create_functions_data_table():
    # get sqlalchemy and pymysql used libraries version
    print("sqlalchemy: {}".format(db.__version__))
    print("pymysql: {}".format(pymysql.__version__))
    # get engine object using pymysql driver for mysql
    engine = db.create_engine(connection_string)
    # get connection object
    connection = engine.connect()
    # get meta data object
    meta_data = db.MetaData()
    # set actor creation script table
    functionsdata = db.Table(
        "functionsdata", meta_data,
        db.Column("id", db.Integer, primary_key=True, autoincrement=True,
        nullable=False),
        db.Column("x", db.Float, nullable=False),
        db.Column("y1", db.Float, nullable=False),
        db.Column("y2", db.Float, nullable=False),
        db.Column("y3", db.Float, nullable=False),
        db.Column("y4", db.Float, nullable=False),
        db.Column("y5", db.Float, nullable=False),
        db.Column("y6", db.Float, nullable=False),
        db.Column("y7", db.Float, nullable=False),
        db.Column("y8", db.Float, nullable=False),
        db.Column("y9", db.Float, nullable=False),
        db.Column("y10", db.Float, nullable=False),
        db.Column("y11", db.Float, nullable=False),
        db.Column("y12", db.Float, nullable=False),
        db.Column("y13", db.Float, nullable=False),
        db.Column("y14", db.Float, nullable=False),
        db.Column("y15", db.Float, nullable=False),
        db.Column("y16", db.Float, nullable=False),
        db.Column("y17", db.Float, nullable=False),
        db.Column("y18", db.Float, nullable=False),
        db.Column("y19", db.Float, nullable=False),
        db.Column("y20", db.Float, nullable=False),
        db.Column("y21", db.Float, nullable=False),
        db.Column("y22", db.Float, nullable=False),
        db.Column("y23", db.Float, nullable=False),
        db.Column("y24", db.Float, nullable=False),
        db.Column("y25", db.Float, nullable=False),
        db.Column("y26", db.Float, nullable=False),
        db.Column("y27", db.Float, nullable=False),
        db.Column("y28", db.Float, nullable=False),
        db.Column("y29", db.Float, nullable=False),
        db.Column("y30", db.Float, nullable=False),
        db.Column("y31", db.Float, nullable=False),
        db.Column("y32", db.Float, nullable=False),
        db.Column("y33", db.Float, nullable=False),
        db.Column("y34", db.Float, nullable=False),
        db.Column("y35", db.Float, nullable=False),
        db.Column("y36", db.Float, nullable=False),
        db.Column("y37", db.Float, nullable=False),
        db.Column("y38", db.Float, nullable=False),
        db.Column("y39", db.Float, nullable=False),
        db.Column("y40", db.Float, nullable=False),
        db.Column("y41", db.Float, nullable=False),
        db.Column("y42", db.Float, nullable=False),
        db.Column("y43", db.Float, nullable=False),
        db.Column("y44", db.Float, nullable=False),
        db.Column("y45", db.Float, nullable=False),
        db.Column("y46", db.Float, nullable=False),
        db.Column("y47", db.Float, nullable=False),
        db.Column("y48", db.Float, nullable=False),
        db.Column("y49", db.Float, nullable=False),
        db.Column("y50", db.Float, nullable=False))
    # create actor table and stores the information in metadata
    meta_data.create_all(engine)

def create_training_data_table():

    # get sqlalchemy and pymysql used libraries version
    print("sqlalchemy: {}".format(db.__version__))
    print("pymysql: {}".format(pymysql.__version__))
    # get engine object using pymysql driver for mysql
    # engine = db.create_engine("mysql+pymysql://root:RajiMySql-1@localhost/functiondb")
    engine = db.create_engine(connection_string)
 
    # get connection object
    connection = engine.connect()
    # get meta data object
    meta_data = db.MetaData()
    # set actor creation script table
    trainingdata = db.Table(
        "trainingdata", meta_data,
        db.Column("id", db.Integer, primary_key=True, autoincrement=True,
        nullable=False),
        db.Column("x", db.Float, nullable=False),
        db.Column("y1", db.Float, nullable=False),
        db.Column("y2", db.Float, nullable=False),
        db.Column("y3", db.Float, nullable=False),
        db.Column("y4", db.Float, nullable=False))
    meta_data.create_all(engine)

def create_testing_data_table():

    # get sqlalchemy and pymysql used libraries version
    print("sqlalchemy: {}".format(db.__version__))
    print("pymysql: {}".format(pymysql.__version__))
    # get engine object using pymysql driver for mysql
    # engine = db.create_engine("mysql+pymysql://root:RajiMySql-1@localhost/functiondb")
    engine = db.create_engine(connection_string)
    # get connection object
    connection = engine.connect()
    # get meta data object
    meta_data = db.MetaData()
    # set actor creation script table
    trainingdata = db.Table(
        "testingdata", meta_data,
        db.Column("id", db.Integer, primary_key=True, autoincrement=True,
        nullable=False),
        db.Column("x", db.Float, nullable=False),
        db.Column("y", db.Float, nullable=False),
        db.Column("ideal_function_number", db.VARCHAR(3), nullable=True),
        db.Column("deviation_value", db.Float, nullable=True))
    meta_data.create_all(engine)

def create_functions_table():

    # get sqlalchemy and pymysql used libraries version
    print("sqlalchemy: {}".format(db.__version__))
    print("pymysql: {}".format(pymysql.__version__))
    # get engine object using pymysql driver for mysql
    # engine = db.create_engine("mysql+pymysql://root:RajiMySql-1@localhost/functiondb")
    engine = db.create_engine(connection_string)
     # get connection object
    connection = engine.connect()
    # get meta data object
    meta_data = db.MetaData()
    # set actor creation script table
    functions = db.Table(
        "functions", meta_data,
        db.Column("id", db.Integer, primary_key=True, autoincrement=True,
        nullable=False),
        db.Column("function_number", db.VARCHAR(3), nullable=False),
        db.Column("x_coeff", db.Float, nullable=False),
        db.Column("intercept", db.Float, nullable=False),
        db.Column("y1_rmse", db.Float, nullable=False),
        db.Column("y2_rmse", db.Float, nullable=False),
        db.Column("y3_rmse", db.Float, nullable=False),
        db.Column("y4_rmse", db.Float, nullable=False),
        db.Column("ideal", db.Boolean, nullable=False))
    meta_data.create_all(engine)

def load_data_table(table_name, df_data):
    # get engine object using pymysql driver for mysql
    # engine = db.create_engine("mysql+pymysql://root:RajiMySql-1@localhost/functiondb")
    engine = db.create_engine(connection_string)
     # get metadata object
    meta_data = db.MetaData()
    # get connection object
    connection = engine.connect()
    # get functionsdata table definitio
    data_table = db.Table(table_name, meta_data, autoload_with=engine)
    # set the insert statement
    df_data.to_sql(table_name, con=engine, index=False, if_exists="append")


def get_data_from_table(table_name):

    # get engine object using pymysql driver for mysql
    # engine = db.create_engine("mysql+pymysql://root:RajiMySql-1@localhost/functiondb")
    engine = db.create_engine(connection_string)
    meta_data = db.MetaData()
    # get connection object
    connection = engine.connect()
    # get table definition
    table = db.Table(table_name, meta_data,autoload_with=engine)
    # set the select statement
    select_table = db.select(table)
    # execute the select statement
    dataset = connection.execute(select_table).fetchall()
    # print row by row
    # for row in dataset:
    #     print(row)
    return dataset

def delete_data_from_table(table_name):
    # get engine object using pymysql driver for mysql
    # engine = db.create_engine("mysql+pymysql://root:RajiMySql-1@localhost/movie", pool_pre_ping=True)
    engine = db.create_engine(connection_string)
    meta_data = db.MetaData()
    # get connection object
    # connection = engine.connect()
    # get actor table definition
    table = db.Table(table_name, meta_data, autoload_with=engine)
    # set delete sql statement. delete the record where id is equal to 1
    sql_query = db.delete(table)
    with engine.begin() as conn:
        results = conn.execute(sql_query)
        print(results.rowcount)

def update_ideal_functions(ideal_function_number):
    
    # get engine object using pymysql driver for mysql
    engine = db.create_engine(connection_string)
    meta_data = db.MetaData()
    # get actor table definition
    table = db.Table("functions", meta_data, autoload_with=engine)
    # set update sql statement. update column 'active' to true where id is equal to 4 
    # sql_query = db.update(actor_table).where(actor_table.columns.id==10).values(age=55)
    # print(ideal_function_number)
    sql_query = db.update(table).where(table.columns.function_number==ideal_function_number).values({"ideal":True})
    # print(sql_query)
    with engine.begin() as conn:
        results = conn.execute(sql_query)
        print(results.rowcount)


def get_ideal_functions_data(ideal_function_numbers):
    print("ideal function numbers in dbhelper")
    print(ideal_function_numbers)
    # get engine object using pymysql driver for mysql
    # engine = db.create_engine("mysql+pymysql://root:RajiMySql-1@localhost/functiondb")
    engine = db.create_engine(connection_string)
    meta_data = db.MetaData()
    # get connection object
    connection = engine.connect()
    # get table definition
    table = db.Table("functionsdata", meta_data, include_columns=ideal_function_numbers, autoload_with=engine)
    columns = table.c
    # set the select statement
    select_table = db.select(table)
    dataset = connection.execute(select_table).fetchall()
    # print row by row
    # for row in dataset:
    #     print(row)
    return dataset

def update_test_data(id, ideal_function_number, deviation):
    # get engine object using pymysql driver for mysql
    engine = db.create_engine(connection_string)
    meta_data = db.MetaData()
    # get actor table definition
    table = db.Table("testingdata", meta_data, autoload_with=engine)
    # set update sql statement. update column 'active' to true where id is equal to 4 
    # sql_query = db.update(actor_table).where(actor_table.columns.id==10).values(age=55)
    sql_query = db.update(table).where(table.columns.id==id).\
        values({"deviation_value":deviation,"ideal_function_number":ideal_function_number})
    print(sql_query)
    with engine.begin() as conn:
        results = conn.execute(sql_query)
        print("rows affected: {}".format(results.rowcount))
