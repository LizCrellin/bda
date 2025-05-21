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

# keys in dictionary are immutable.

# tutorial on dictionaries available in session 4 link.

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

# more elegant way to pass to function, via dictionary - in fact a few different ways. use the tutorial to see/try these.

# can have default values set.
# named parameters with defaults.
# 3rd way missed!
# using *args
# 5 using **kwargs - keyward arguments dict.
# 6 accept a dictionary as a single argument.

# Stelios says 6 is best way to do the assignment!


'''
preparing environment for assignment
'''
#new project/folder
#keep track
#separate function and other script


import fun_new #this is the name of the function script.
input_data = {"filename": "netflix_titles.csv", "type": "csv"}
# this is useful metadata for the function .
load_csv_data(input_data)
#and create the function to handle the dictionary input I guess.

#in hte function script:
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






