import fun
import hw_fun


#first downloaded "rockyou.txt" from kaggle.
with open("rockyou.txt", "r", encoding="latin-1") as file:
    lines = file.readlines()

#1. Count how many passwords start with the letter `'a'`.

#already done in class
print(fun.count_start_letter(lines, 'A'))







#7. Count how many passwords are exactly 8 characters long.

print(hw_fun.count_by_length(lines, 8))


#8. Count how many passwords are made of only lowercase letters.