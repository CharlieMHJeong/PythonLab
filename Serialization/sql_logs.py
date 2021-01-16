#SQL Example

import sqlite3
from random import choice
from datetime import datetime, timedelta

#use :memory: for in memory db
#create sqlite db and connect it
db = sqlite3.connect('sql_logs.db')
with open('sql_schema.sql') as fp:
    schema_sql = fp.read()

db.executescript(schema_sql)
db.commit()

#Generate random data
cur = db.cursor() #DB cursor
now = datetime.now() #mark the current time

insert_sql = 'INSERT INTO logs (time, level, message) values (?, ?, ?)' # ?:Place holders for parameters
for i in range(10_000):
    time = now - timedelta(seconds=i)
    level = choice(['INFO', 'WARNING', 'ERROR'])
    message = f'log message #{i}'
    cur.execute(insert_sql, (time, level, message))
db.commit()

#Query the db
db.row_factory = sqlite3.Row # Access column by name
cur = db.cursor()
query_sql = 'SELECT * FROM logs WHERE level = "INFO" LIMIT 5'

for row in cur.execute(query_sql):
    print(dict(row))
