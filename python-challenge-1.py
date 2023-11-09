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

    # newlist = [cityname for cityname in cities if answer == cityname]
newlist = [] # list of the input city amount
linenum = [] # want this to be the list of the row # captured city is on out of the whole list

i = 0
while i <= len(newlist):
    answer = input(str("what city? "))
    for cityname in cities:
        if cityname == answer:
            newlist.append(cityname)
            if
            linenum.append(i)
            i += 1
    citycount = len(newlist)
    print(citycount)
    print(i)
