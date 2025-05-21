
import importlib

import session2.fun as fun
import session2.hw_fun as hw_fun
importlib.reload(hw_fun)


#first downloaded "rockyou.txt" from kaggle.
with open("rockyou.txt", "r", encoding="latin-1") as file:
    lines = file.readlines()

#1. Count how many passwords start with the letter `'a'`.
#already done in class
print(fun.count_start_letter(lines, 'a'))

#2. Count how many anagram groups exist in the password list.
#   -  *Anagram:* Words that contain the same letters in a different order (e.g., `"listen"` and `"silent"`).
print(hw_fun.count_anagrams(lines))

#3. Count how many passwords are palindromes.
#   -  *Palindrome:* A word that reads the same forward and backward (e.g., `"racecar"`, `"level"`).
print(hw_fun.palindrome(lines))      

#4. Find the top 5 most frequent starting letters in the password list.
# too tough even looking at solutions, go back to this later.
#attempt to start this:
print(hw_fun.frequency_starting_dict(lines)) # first step

#5. Count how many passwords contain only numerics.
# see useful reference material in the homework .md file.
print(hw_fun.count_numeric(lines))

#6. Find the longest password in the list.
print(hw_fun.longest(lines))               #nb there is some corruption in the list

#7. Count how many passwords are exactly 8 characters long.
print(hw_fun.count_by_length(lines, 8))

#8. Count how many passwords are made of only lowercase letters.
print(hw_fun.lowercount(lines))

#9. Count how many passwords contain the substring `"123"`.
print(hw_fun.containstring(lines, "123"))

#10. Calculate the average length of all passwords.
print(hw_fun.avlength(lines))