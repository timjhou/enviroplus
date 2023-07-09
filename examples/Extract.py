import mysql.connector as connection
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql://Tim:Ahold9422@localhost:3306/test")
#conn = engine.connect()
with engine.connect() as connection:
    connection.execute(text("SELECT * FROM aqi)"))


#metadata = MetaData()
#division = Table('aqi')





""" try:
    mydb = connection.connect(host='192.168.86.169',
                              database = 'test',
                              user = 'Timmy PC',
                              passwd = 'Ahold9422',
                              use_pure = True)
    query = 'SELECT * FROM aqi;'
    result_df = pd.read_sql(query, mydb)
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))

result_df.head() """