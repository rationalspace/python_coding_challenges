#find the char that occurs maximum number of times in a string
import operator
def maxChars(s):
    cmap = {}
    for c in s:
        if c in cmap.keys():
            cmap[c] += 1
        else:
            cmap[c] = 1
            #sorts the hash map by key 1 which is the counts of characters
    return sorted(cmap.items(),key=operator.itemgetter(1),reverse=True)[0]

string = str(input("Enter the string "))
(maxchar,maxval)  = maxChars(string)
print(maxchar," occurs ", maxval, " number of times")