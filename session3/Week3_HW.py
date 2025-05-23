
'''
Exercises from README: in the lab materials
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

def my_head(alist, limit):
    newlist = []
    count = 0
    for i in alist:
        if count < limit:
            newlist.append(i)
            count += 1
    return newlist

print(my_head(netflix_data, 5))

# From solutions, this is how to do this with yield:
def my_head(alist, limit):
    for i in range(limit):
        if i < len(alist):
            yield alist[i]
        else:
            break

# Example usage:
for item in my_head(netflix_data, 5):
    print(item)


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


# MORE EXERCISES:
#3. Create a function called my_head_col(alist,col,limit) to return the first records of a specific column from the dataset as a list.
def my_head_col(alist, col, limit):
    newlist = []
    count = 0
    for i in alist:
        if count < limit:
            newlist.append(i[col])
            count += 1
    return newlist

print(my_head_col(netflix_data, "title", 7))
print(my_head_col(netflix_data, "show_id", 4))

'''
Time complexity: O(n) — worst case limit is the amount of data
Space Complexity: O(k) where k = limit (Youre storing limit values, not n)
'''

# From solutions: this was done similarly but backwards (is that more efficient?)
# as below:
def head_col(alist,col,limit):
    return_data=[]
    for i in alist:
        if limit==0:
            break
        return_data.append(i[col])
        limit-=1
    return return_data

head_col(data, "title", 5)

'''''
Time complexity: `O(n)` — worst case limit is the amount of data
Space Complexity: `O(k)` where `k = limit`  (You’re storing `limit` values, not `n`)
'''

#4. Filters titles added in the year 2021.
#Develop a function for shows_added_in_2021(data) for titles from United States
#solution with return:
def shows_added_in_2021(data):
    movies2021 = []
    for row in data:
        if row['release_year'] == '2021' and row['country'] == 'United States':
            movies2021.append(row['title'])
    return movies2021
print(shows_added_in_2021(netflix_data))

'''
Time complexity: 0(n)
Space complexity: 0(n)
'''
#solution with yield:
def shows_added_in_2021(data):
    for row in data:
        if row['release_year'] == '2021' and row['country'] == 'United States':
            yield row['title']
for item in shows_added_in_2021(netflix_data):
    print(item)
'''
Time complexity: 0(n)
Space complexity: `O(1)` — yields one item at a time, no list built in memory.
'''

#6. Develop a function for shows_added_in_2021(data) for titles from United States
# THIS IS THE SAME AS ABOVE!

#7. Titles with love (any case).
# with return - adapt function created for lab.
def lovemovies(data):
    lovemovies = []
    for row in data:
        if 'love' in row['title'].lower() and row['type'].lower()== 'movie':
            lovemovies.append(row['title'])
    return lovemovies
print(lovemovies(netflix_data))
'''
Time complexity: 0(n)
Space complexity: 0(n)
'''
#with yield:
def lovemovies(data):
    for row in data:
        if 'love' in row['title'].lower() and row['type'].lower()== 'movie':
            yield row['title']
for item in lovemovies(netflix_data):
    print(item)
'''
Time complexity: 0(n)
Space complexity: 0(1)
'''
# or could add to a list? then can get length etc.
lovemovies_list = []
for item in lovemovies(netflix_data):
    lovemovies_list.append(item)
print(len(lovemovies_list))

#8. Finds all movies with a PG-13 rating.
#using return:
def pg13movies(data):
    pg13list = []
    for row in data:
        if row['rating'].lower() == 'pg-13' and row['type'].lower()== 'movie':
            pg13list.append(row['title'])
    return pg13list
print(pg13movies(netflix_data))

#using yield:
def pg13movies(data):
    for row in data:
        if row['rating'].lower() == 'pg-13' and row['type'].lower()== 'movie':
            yield row['title']
for item in pg13movies(netflix_data):
    print(item)

#9. Develop the my_len function, to count the total entries
def my_len(data):
    count = 0
    for row in data:
        count += 1
    return count
print(my_len(netflix_data))

# Can I use yield here?
# NO, CANNOT AS YIELD ONLY YIELDS ONE AT A TIME.

#10. Count Types
#Counts how many entries are TV Show vs. Movie.
# nb don't think I can use yield here.
def count_types(data):
    counttv = 0
    countmovie = 0
    for row in data:
        if row['type'].lower() == 'tv show':
            counttv += 1
        if row['type'].lower() == 'movie':
            countmovie += 1
    return counttv, countmovie
print(count_types(netflix_data))


# 12. **Average TV show seasons**
def avg_seasons(data):
    count = 0
    countseasons = 0
    for row in data:
        if row['type'].lower() == 'tv show':
               seasons = int(row['duration'].split()[0])
               count +=1
               countseasons += seasons
    return countseasons/count
print(avg_seasons(netflix_data))
#can this be done with yield? maybe not - I'm not sure. we only need to return the counts, not the values.

#time complexity: 0(n)
#space complexity: 0(1)

#13. Sort by release year using `Bubble sort`.
def sort_by_year(data, year):
    n = len(data)
    for i in range(n):
        for j in range(0, n-1-i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr