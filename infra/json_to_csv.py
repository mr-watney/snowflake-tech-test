import json
import pandas as pd


file = open('../input_data/starter/transactions_full.json', "r")
data = file.read()
d = data[:-2]+"]" # changing ',]' to ']' in last line
file.close()

print("Conversion to CSV started")

parsed=json.loads(d)

df=pd.json_normalize(parsed, "basket",["customer_id","date_of_purchase"])

df.to_csv('../input_data/ready/transactions.csv',index=False)

print("Conversion to CSV finished")