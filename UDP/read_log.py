import csv
import os


with open("data.csv", 'r') as file:
    csvreader = csv.reader(file)
    for i, row in enumerate(csvreader):
        print(i, row[0])
