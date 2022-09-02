import pandas as pd

input_directory="../input_data_generator/input_data/starter/"
output_directory="../input_data/ready/"
files=["customers.csv","products.csv"]

print("Removing empty rows started")
for file in files:
    df=pd.read_csv(input_directory+file)
    df.to_csv(output_directory+file, index=False)
    print("- Empty rows removed from " + file)
print("Removing empty rows finished")