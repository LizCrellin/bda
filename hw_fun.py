
def count_by_length(alist, chosenlength):
    count = 0
    for i in alist:
        if (len(i) - 1) == chosenlength:
            count += 1
    return count
