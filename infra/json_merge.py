import os.path

directory = "../input_data_generator/input_data/starter/transactions"
file_list=[]

#retrieve list of transaction.json files from all subfolders under transactions
for root, subdirectories, files in os.walk(directory):
    for file in files:
        file_list.append(os.path.join(root, file).replace("\\","/"))

#merging separate transaction files into one
with open("../input_data/starter/transactions_full.json", "w") as outfile:
    outfile.write("[")
    for f in file_list:
        print("Processing file "+f)
        with open(f, "r") as infile:
            for line in infile:
                outfile.write(line+",")
    outfile.write("]")
print("Merging finished")