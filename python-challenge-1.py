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
while True:
    try:
        answer = input(str("what city? "))
        for cityname in cities:
            i += 1
            if cityname == answer:
                linenum.append(i)
            elif answer == "exit":
                exit()
        print(answer, "is on lines", linenum)
    except EOFError:
        exit()
