import csv

with open('rates.csv', newline='') as csvfile:
     rates = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in rates:
         print(', '.join(row))

# to dict, preserves ordering
with open('names.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['first_name'], row['last_name'])