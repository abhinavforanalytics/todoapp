import csv

with open('Temperatur.csv') as file:
    data = list(csv.reader(file)) #list of lists

city = input("Enter the country name: ")

for row in data:
    if row[0] == city.title():
        print(row[1])