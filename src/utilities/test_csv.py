import csv

file = 'random_test_small.csv'

reader = csv.reader(open(file,'r'),delimiter=',')

for row in reader:
  print(row)
