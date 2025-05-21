
print("hw_fun.py loaded")

#2. Count how many anagram groups exist in the password list.
#   -  *Anagram:* Words that contain the same letters in a different order (e.g., `"listen"` and `"silent"`).
# NB used solutions and hints to solve this.
def count_anagrams(alist):
    groups = set()
    for i in alist:
        word = i.strip()
        if len(word) > 1:
            sorted_word = ''.join(sorted(word)) #sort the letters in the word. any anagrams will then be the same as others in the same group.
        else:
            sorted_word = word
        groups.add(sorted_word)  # add to set. Sets do not allow duplicates.
    return len(groups)

#3. Count how many passwords are palindromes.
#   -  *Palindrome:* A word that reads the same forward and backward (e.g., `"racecar"`, `"level"`).
def palindrome(alist):
    count = 0
    for i in alist:
        if i == i[::-1]:
            count += 1
    return count

#4. Find the top 5 most frequent starting letters in the password list.
# using code in the README file:
# did this in stages, started with frequency of passwords. then first letters. used the solutions and readme.
def frequency_starting_dict(data):
    freq = {}
    for i in data:
        word = i.strip()
        if word:
            first = word[0].lower()  # first letter in the word - lowercase
            if first in freq:
                freq[first] += 1
            else:
                freq[first] = 1
    
    items = list(freq.items())
    # Simple bubble sort (descending)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[j][1] > items[i][1]:
                items[i], items[j] = items[j], items[i]
    return items[:5]

#5. Count how many passwords contain only numerics.
def count_numeric(alist):
    count = 0
    for i in alist:
        word = i.strip()
        if word.isnumeric():
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

#10. Calculate the average length of all passwords.
def avlength(alist):
    totallength = 0
    count = 0
    for i in alist:
        word = i.strip()
        totallength += len(word)
        count += 1
    return totallength/count


