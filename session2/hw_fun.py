
print("hw_fun.py loaded")


#3. Count how many passwords are palindromes.
#   -  *Palindrome:* A word that reads the same forward and backward (e.g., `"racecar"`, `"level"`).
def palindrome(alist):
    count = 0
    for i in alist:
        if i == i[::-1]:
            count += 1
    return count

#6. Find the longest password in the list.
def longest(alist):
    longest = ""
    for i in alist:
        word = i.strip()
        if len(word) > len(longest):
            longest = word
    return longest

#7. 
def count_by_length(alist, chosenlength):
    count = 0
    for i in alist:
        if (len(i) - 1) == chosenlength:
            count += 1
    return count

#8. 
def lowercount(alist):
    count = 0
    for i in alist:
        word = i.strip()
        if word.islower() and word.isalpha():
            count += 1
    return count

#9. Count how many passwords contain the substring `"123"`.
def containstring(alist, qstring):
    count = 0
    for i in alist:
        word = i.strip()
        if qstring in word:
            count += 1
    print(count)