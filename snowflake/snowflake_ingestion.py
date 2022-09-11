import os
import snowflake.connector

USER = os.getenv('SNOWSQL_USR')
PASSWORD = os.getenv('SNOWSQL_PWD')
ACCOUNT = 'gz33782.eu-central-1'
WAREHOUSE = 'COMPUTE_WH'
ROLE = 'ACCOUNTADMIN'

data = ['products','customers','transactions']

conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    role=ROLE
    )
    
conn.cursor().execute("USE DATABASE TECH_TASK")
conn.cursor().execute("USE SCHEMA VL_TASK")

for d in data:
    print("Ingesting "+d+".csv")
    conn.cursor().execute("copy into "+d+" from @aws_"+d+" file_format = (type = csv field_delimiter = ',' skip_header = 1);")

print("Ingestion finished")
conn.close()
