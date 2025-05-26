
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
From solutions - no this is incorrect. 

Time complexity is 0(k) where k = min(limit, len(alist)). we don't at any point construct a new list.

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
Space Complexity: O(k) where k = limit (You're storing limit values, not n)
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

CORRECT
FROM SOLUTIONS:
Time complexity: `O(n)` — where `n` is the number of rows in `data`
Space complexity: `O(n)` — builds and stores a list of up to `limit` values in memory.

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

CORRECT
FROM SOLUTIONS:
- **Time Complexity**: `O(n)` — same as the original.
- **Space Complexity**: `O(1)` — only one matching item is held in memory at a time.
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

NO
FROM SOLUTIONS:
Time: `O(n·m)` — where `n` is the number of rows and `m` is the average length of each title (`lower()` and `'blood' in ...` are O(m) string operations per row).
Space: `O(n)` — where `n` is the number of matching titles that contain "love".  
# I RECKON SOLUTION IS WRONG HERE, AS IT'S NOT STORING ALL TITLES IN MEMORY AT ONCE, IT IS YIELDING ONE AT A TIME.
'''
# or could add to a list? then can get length etc.
lovemovies_list = []
for item in lovemovies(netflix_data):
    lovemovies_list.append(item)
print(len(lovemovies_list))

# i guess this is an option but not as space efficient.

#8. Finds all movies with a PG-13 rating.
#using return:
def pg13movies(data):
    pg13list = []
    for row in data:
        if row['rating'].lower() == 'pg-13' and row['type'].lower()== 'movie':
            pg13list.append(row['title'])
    return pg13list
print(pg13movies(netflix_data))

'''
from solutions:
**Time Complexity: `O(n)`**

- The function loops over all `n` rows in the dataset once.
- Each condition check and append operation is constant time.

 **Space Complexity: `O(k)`**

- Where `k` is the number of matching entries (`PG-13` movies).
- The function builds a list containing only the matches.
'''

#using yield:
def pg13movies(data):
    for row in data:
        if row['rating'].lower() == 'pg-13' and row['type'].lower()== 'movie':
            yield row['title']
for item in pg13movies(netflix_data):
    print(item)

'''
from solutions:
**Time Complexity: `O(n)`**

- Loops through each of the `n` rows in `data`.
- Performs constant-time comparisons and yields matches.
- Same as the list version.

**Space Complexity: `O(1)`**

- **Does not** store results in a list.
- Only holds **one matching title in memory at a time**.
'''


#9. Develop the my_len function, to count the total entries
def my_len(data):
    count = 0
    for row in data:
        count += 1
    return count
print(my_len(netflix_data))

# Can I use yield here?
# NO, CANNOT AS YIELD ONLY YIELDS ONE AT A TIME.

'''FROM SOLUTIONS:
No, you **should not use `yield`** for `my_len`, because:

- `yield` is used to **produce values one-by-one**
- `my_len` is a function that returns a **single final count**, not a stream

**Time Complexity: `O(n)`**

- The loop runs once for every element in `alist`
- Simple increment per item → linear time

 **Space Complexity: `O(1)`**

- Only one variable (`count`) is used for tracking
- No new data structures are created or stored
'''


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

'''
FROM SOLUTIONS:
**Time Complexity: `O(n)`**

- The function loops over all `n` rows in the dataset.
- Each comparison and increment is constant time → total is linear.

 **Space Complexity: `O(1)`**

- Only two counters (`tv` and `movie`) are maintained.
- The final result is a fixed-size dictionary with two keys.
'''
#AGAIN - CAN'T USE YIELD HERE.

# 11. **Count Per Category**
# Generate a frequency table
'''FROM SOLUTIONS:'''
def count_type_frequency(data):
    type_counts = {}
    for row in data:
        content_type = row["type"]
        if content_type in type_counts:
            type_counts[content_type] += 1
        else:
            type_counts[content_type] = 1
    return type_counts

typecounts = count_type_frequency(netflix_data)
print(typecounts)

'''from solutions:
**Time Complexity: `O(n)`**

- The function iterates over all `n` rows once.
- Dictionary operations (`in`, `+= 1`, assignment) are on average **O(1)**.
- So the total time is **O(n)**.

**Space Complexity: `O(t)`**, where `t` is the number of unique content types

- A dictionary `type_counts` is built with one entry per unique type (e.g., "Movie", "TV Show", etc.).
- In practice, `t` is small, so this is often treated as **O(1)**.
'''

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

'''from solutions:
**Time Complexity: `O(n)`**

- Iterates through all `n` rows.
- For each row, it performs:
  - A string check (`'Season' in row['duration']`) → O(1)
  - A string split and conversion to `int()` → O(1)
- All operations inside the loop are constant time → **O(n)** overall.

**Space Complexity: `O(1)`**

- Only two variables (`total`, `count`) are used.
- No new data structures or collections are created.
'''



#13. Sort by release year using `Bubble sort`.
def sort_by_year(data, year):   
    n = len(data)
    for i in range(n):
        for j in range(0, n-1-i):
            if data[j][year] > data[j + 1][year]:
                data[j][year], data[j + 1][year] = data[j + 1][year], data[j][year]
    return data
sorted_data = sort_by_year(netflix_data, 'release_year')
print(sorted_data[:5])

# improvements from solutions:
def sort_by_release_year(data): # no need to select a year! we are sorting by this variable.
    sorted_data = data[:]  # Copy to avoid modifying the original  - do this within the function.
    n = len(sorted_data)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            year_j = int(sorted_data[j]['release_year'])    # convert to int here 
            year_next = int(sorted_data[j + 1]['release_year'])
            if year_j > year_next:
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
    
    return [row['title'] for row in sorted_data]  
print(sort_by_release_year(netflix_data)[:5])

#From solutions:
'''
**How Bubble Sort Works:**

- Repeatedly compares adjacent elements
- Swaps them if they're in the wrong order
- "Bubbles" the largest value to the end in each pass

Time complexity: `O(n^2)`

Space complexity: `O(n)` — due to copying the list
'''

#14. **Convert durations**
'''
The function extracts numeric values from the `"duration"` field and groups them into a dictionary based on units like `"min"`, `"Season"`, or `"Seasons"`. 
It skips empty or malformed entries.

*It works on a list of dictionaries where each dictionary has a `'duration'` key.*
'''
#Here I took the function from the solutions:
def group_durations(data):
    result = {}     # dictionary
    for row in data:
        duration = row.get('duration', '').strip()
        if not duration:
            continue
        parts = duration.split()
        if len(parts) != 2:
            continue
        num, unit = parts
        try:
            num = int(num)
        except ValueError:
            continue
        if unit not in result:
            result[unit] = []
        result[unit].append(num)
    return result

group_durations(netflix_data)

#15. **What is the distribution of content types (TV Show vs Movie)?**
'''
Create a **bar chart** showing how many titles fall into each type.
'''
# Here I took the function from the solutions:
import matplotlib.pyplot as plt

def plot_type_distribution(data):
    # Count how many of each type (e.g., Movie, TV Show)
    type_counts = {}            # stores the type counts in a dictionary. doesn't matter what types - will catch them all.
    for row in data:
        typ = row["type"]
        if typ in type_counts:
            type_counts[typ] += 1
        else:
            type_counts[typ] = 1

    # Plot using matplotlib
    plt.figure(figsize=(6, 4))
    plt.bar(type_counts.keys(), type_counts.values())
    plt.title("Distribution of Content Types")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# Call the function on your dataset
plot_type_distribution(data)


