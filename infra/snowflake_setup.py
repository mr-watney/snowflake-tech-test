import os
import snowflake.connector

USER = os.getenv('SNOWSQL_USR')
PASSWORD = os.getenv('SNOWSQL_PWD')
ACCOUNT = 'gz33782.eu-central-1'
WAREHOUSE = 'COMPUTE_WH'
ROLE = 'ACCOUNTADMIN'
AWS_KEY_ID = os.getenv('AWS_SERVER_PUBLIC_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SERVER_SECRET_KEY')

data = ['products','customers','transactions']

conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    role=ROLE
    )
    
    
conn.cursor().execute("CREATE DATABASE IF NOT EXISTS TECH_TASK")
print("Database TECH_TASK created")
conn.cursor().execute("USE DATABASE TECH_TASK")
print("Switched to database TECH_TASK")
conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS VL_TASK")
print("Schema VL_TASK created")
conn.cursor().execute("USE SCHEMA VL_TASK")
print("Switched to schema VL_TASK")
for d in data:
    conn.cursor().execute("CREATE STAGE IF NOT EXISTS aws_"+d+" URL='s3://s3-bucket-mrwatney/"+d+"/' CREDENTIALS = (AWS_KEY_ID = '"+AWS_KEY_ID+"' AWS_SECRET_KEY = '"+AWS_SECRET_KEY+"') file_format=(type=csv)")
    print("Stage aws_"+d+" created")
conn.close()
print("Process finished")