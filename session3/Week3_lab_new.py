
import csv

with open('netflix_titles.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

print(data[1])


import csv

def load_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]  
    return data

data = load_csv('netflix_titles.csv')
print(data[0])

