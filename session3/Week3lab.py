'''
This is the Week 3 lab with live work and additions from the materials added after the session.
'''


#1. Load the data in Python as a dictionary.
# Read the CSV data into a list of dictionaries, for later usage.

import csv

with open('netflix_titles.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

print(data[1])

# Function implementation:
def load_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]  
    return data

netflix_data = load_csv('netflix_titles.csv')
print(netflix_data[0])
print(netflix_data[1])

'''From solutions:

Time Complexity: O(n·m)
---Opening file: O(1)
---Reading file line by line: O(n), where n is the number of rows (excluding the header)
---Parsing each row into a dictionary: O(n·m), where m is the number of columns (fields)
---Each field is mapped to a key, so constructing a dict is O(m)
---List comprehension to store all rows: O(n)

Space Complexity: O(n·m)
---Data stores all n rows in memory
---Each row is a dictionary with m key-value pairs

This method, using return, is not v efficient.
'''

#2 Create a function called my_head(alist,limit) to return the n first records of the dataset in a new list.
def my_head_yield(alist, limit):
    for i in range(limit):
        if i < len(alist):
            yield alist[i]
        else:
            break

# From solutions, example usage:
for item in my_head_yield(netflix_data, 5):
    print(item)


# adapt the above function for the file:
def load_csv_yield(filename, limit):
    with open(filename, mode='r', newline = '') as file:
        reader = csv.DictReader(file)
        count = 0
        for row in reader:
            if count < limit:
                yield row
                count += 1
            else:
                break

for item in load_csv_yield('netflix_titles.csv', 10):
    print(item)

data_stream = load_csv_yield('netflix_titles.csv', 100)

#From lab - how to print first few rows from the data
#not in memory so have to ask python to get it again
#use enumerate
for i, row in enumerate(data_stream):
  if i>=5:
    break
  print(row)

'''Why use yield?

You get one item at a time (no list built in memory). Its more efficient when you only need a few items from a large list or stream. 
Works well in pipelines or streaming scenarios.

Time Complexity:
Opening file: O(1) Reading file line by line: O(n), where n is the number of rows (excluding the header) 
Parsing each row into a dictionary: O(n·m), where m is the number of columns (fields) 
Each field is mapped to a key, so constructing a dict is O(m) List comprehension to store all rows: O(n) So overall O(n·m) 
From solutions - no this is incorrect. Time complexity is 0(k) where k = min(limit, len(alist)). we don't at any point construct a new list.

Space complexity: Data stores one row in memory.
Each row is a dictionary with m key-value pairs So overall 0(1) YES.'''


#find the cast of squid game!
#this is how we could do it in full ds
for row in netflix_data:
    if row['title'].lower() == 'squid game':
        print(row['cast'])
# Time: 0(n)
# Space: 0(1)


# attempt to do this from data_stream (doesn't work)...
#for row in enumerate(data_stream):
#  if row[2].lower() == 'squid game':
#    print(row['cast'])

#all movies with PG-13 rating:
for row in netflix_data:
    if row['rating'].lower() == 'pg-13' and row['type'].lower()== 'movie':
        print(row['title'])

#Extract these titles in a new list
newlist = []
for row in data:
    if row['rating'].lower() == 'pg-13' and row['type'].lower()== 'movie':
        #print(row['title'])
        newlist.append(row['title'])
    print(newlist)
#Time: 0(n)
#Space: 0(n) as worst case scenario is that all the movies are pg-13


'''Class Exercies:
#Exercises:

#1. Extract movies added Sept 3, 2021
#2. How many movies released 2021?
#3. Is there a movie called Manifest? T or F
#4. How many movies have the word love in their title?
#5. how many missing records in the director column?
#6. Average of release years in the dataset
'''

#1. Extract movies added Sept 3, 2021
septmovies = []
for row in data:
    if row['date_added'].lower() == 'september 3, 2021' and row['type'].lower()== 'movie':
        septmovies.append(row['title'])
print(septmovies)

#2. How many movies released 2021?
#this is solution with return
movies2021 = []
for row in data:
  if row['release_year'] == '2021' and row['type'].lower()== 'movie':
    movies2021.append(row['title'])
print(len(movies2021))

#make into a function
def shows_added_in_year(data,col,year):
  result = []
  for row in data:
    if row['release_year'] == year and row['type'].lower() == 'movie':
      result.append(row[col])
  return result
print(len(shows_added_in_year(netflix_data, 'title', '2021')))

'''
Time complexity: O(n) — where n is the number of rows in data
Space complexity: O(n) — builds and stores a list of up to limit values in memory.
'''
#This is solution with yield
def shows_added_in_year_yield(data, col, year):
    for row in data:
        if row['release_year'] == year and row['type'].lower()== 'movie':
            yield row[col]
# but i'm not sure how I would count them?
def shows_added_in_year_yield_count(data, col, year):
    count = 0
    for row in data:
        if row['release_year'] == year and row['type'].lower()== 'movie':
            count += 1
    return count

print(shows_added_in_year_yield_count(netflix_data, 'title', '2021'))


#3. Is there a movie called Manifest? T or F
manifest = False
for row in data:
    if row['title'].lower() == 'manifest':
        manifest = True
print(manifest)

#4. How many movies have the word love in their title?
lovemovies = []
for row in data:
    if 'love' in row['title'].lower() and row['type'].lower()== 'movie':
        lovemovies.append(row['title'])
print(len(lovemovies))
#OR (better for space)
count = 0
for row in data:
    if 'love' in row['title'].lower() and row['type'].lower()== 'movie':
        count+=1
print(count)

#5. how many missing records in the director column?
count_e = 0
for row in data:
    if row['director'] == '':
        count_e+=1
print(count_e)


#6.Average of release years in the dataset
count = 0
mysum = 0
for row in data:
    if(row['release_year']!=''):
        #print(int(row['release_year'])) #what about odd entries? have to deal with e.g. 2021.5, or text?
        count += 1
        mysum += int(row['release_year'])
print(mysum/count)
# another way could have been to extract into a list and then use length and sum of list
# but we don't do that as it would add space complexity.