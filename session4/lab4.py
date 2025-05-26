'''
DICTIONARIES
'''

alist = [10,20,30,40,50]

student_list = ["Stelios", "London", 26]

student_dict = [
    {"name": "Stelios", "city": "London", "age": 26},
    {"name": "Mary", "city": "London", "age": 35}
]

# this is a list of dictionaries.
# we prefer dictionaries to multidimentional lists. easier to find things.


data = {"name": "Stelios", "city": "London", "age": 26}
print(data["name"])

#  for loop for a dictionary:
for key, value in data.items():
    print(key, value)

data["name"] = "Tom"
print(data)

data["job"] = "Engineer"
print(data)

job = data.get("job")
print(job)

job = data.pop("job")
print(job)

for key in data:
    print(key)  # Print keys

for value in data.values():
    print(value)  # Print values

for key, value in data.items():
    print(f"{key}: {value}")  # Key-value pairs
# keys in dictionary are immutable.

# tutorial on dictionaries available in session 4 link.

#### Nested Dictionaries
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

print(students["student1"]["name"])  # Alice

# See useful dictionary methods in README.md

'''
FUNCTIONS
'''
student_dict = [
    {"name": "Stelios", "city": "London", "age": 26},
    {"name": "Mary", "city": "London", "age": 35}
]
student_dict[0]
student_dict[0]["name"]

def sum_of_2(a,b):
    result = a + b
    return result
print(sum_of_2(10,20))

# more elegant way to pass to function, via dictionary - in fact a few different ways. use the tutorial 'Python functions.md' to see/try these.

# 2. can have default values set.
def sum_of_2(a=0, b=0):
    return a + b

# Usage
print(sum_of_2())         # 0
print(sum_of_2(2))        # 2 (b=0)
print(sum_of_2(2, 3))     # 5

# 3. named parameters with defaults.
def sum_of_2(num1=0, num2=0):
    return num1 + num2

# Usage
print(sum_of_2(num1=5, num2=10))  # 15

# 4. Using `\*args` (positional arguments tuple)
def sum_of_2(*args):
    return sum(args[:2])  # Only sum the first two

# Usage
print(sum_of_2(1, 2))         # 3
print(sum_of_2(1, 2, 3, 4))   # 3 (ignores extra)

# 5 using **kwargs - keyward arguments dict.
def sum_of_2(**kwargs):
    return kwargs.get("a", 0) + kwargs.get("b", 0)

# Usage
print(sum_of_2(a=4, b=6))  # 10
print(sum_of_2())          # 0

# 6 accept a dictionary as a single argument.
# Stelios says 6 is best way to do the assignment!
def sum_of_2(input_dict):
    return input_dict.get("a", 0) + input_dict.get("b", 0)

# Usage
print(sum_of_2({"a": 5, "b": 7}))  # 12

#7. Unpacking a dictionary into parameters
def sum_of_2(a=0, b=0):
    return a + b

# Usage
params = {"a": 2, "b": 3}
print(sum_of_2(**params))  # 5

# 8. Function with input type checking
def sum_of_2(a=0, b=0):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers.")
    return a + b

print(sum_of_2(10,20))

#SEE SUMMARY TABLE IN Python functions.md

'''
Preparing environment for assignment!!!!!
'''
#new project/folder
#keep track
#separate function and other script


import fun_new      #this is the name of the function script.
input_data = {"filename": "netflix_titles.csv", "type": "csv"}
# this is useful metadata for the function .
load_csv_data(input_data)
#and create the function to handle the dictionary input I guess.

#in the function script:
'''
load data from a csv specified in a dictionary

Args:
    input_dict: Dictionary of the data where the key is the filename of the csv file.
Returns:
    list[dict]: A list of dictionaries.
Example:
    input_data = {"data": "hi.csv"}
    [{...},{...},...]

'''
def load_csv_data(input_dict):
    filename = input_dict.get("filename")
    type = input_dict.get("type")
    encoding = input_dict.get("encoding")
    with open(filename, newLine = '', encoding=encoding) as csvfile:
        reader = csv.DictRaeader(csvfile)
        for row in reader:
            data_rows.append(row)
        return data_rows
    

#dictionaries as single argument will be most useful approach - refer to materials on github.
#also have a look at the examples for generators - this will also be useful. 
# These are in lab4.md.






