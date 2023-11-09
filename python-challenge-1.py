import csv

file = open('.venv/us-500.csv')
type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)

cities = []
for row in csvreader:
# pulls cities only
    cities.append(row[5])

file.close()



answer = input(str("what city? "))
    # newlist = [cityname for cityname in cities if answer == cityname]
newlist = []
for cityname in cities:
    if cityname == answer:
        newlist.append(cityname)
citycount = len(newlist)
print(citycount)
