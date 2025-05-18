import csv

def load_csv(filename):
    with open(filename, mode='r', newline = '') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data



data = load_csv('netflix_titles.csv')
print(data[0])
