import csv
import json

data_from_csv=[]
with open("data_set.txt","r") as file:
	data_txt=json.loads(file.read())

field_names=["brake","hand_brake","throttle","steer"]

file_store=open("data_227.csv","w",newline="")

writer=csv.DictWriter(file_store,fieldnames=field_names)
writer.writeheader()
writer.writerows(data_txt)

with open('data_227.csv', 'r') as file:
	reader = csv.reader(file)
	for rows in reader:
		data_from_csv.append(rows)

print(data_from_csv)



