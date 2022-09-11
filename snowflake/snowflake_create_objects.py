import os
import snowflake.connector

USER = os.getenv('SNOWSQL_USR')
PASSWORD = os.getenv('SNOWSQL_PWD')
ACCOUNT = 'gz33782.eu-central-1'
WAREHOUSE = 'COMPUTE_WH'
ROLE = 'ACCOUNTADMIN'

conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    role=ROLE
    )

ddl_files = ["products_create.ddl","customers_create.ddl","transactions_create.ddl", "final_view_create.ddl"]

conn.cursor().execute("USE DATABASE TECH_TASK")
conn.cursor().execute("USE SCHEMA VL_TASK")

for d in ddl_files:
    with open(d, 'r') as f:
        query=f.read()
        print("Creating object from "+d+" file")
        conn.cursor().execute(query)
        f.close()
print("Creating objects finished")
conn.close()