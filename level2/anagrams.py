#check if 2 strings are anagrams - consider only alpha numeric characters of the string
import re
s1 =str(input("Enter the string "))
s2 =str(input("Enter the string "))
str1 = re.sub('[^a-zA-Z0-9]+','', s1).lower()
str2 = re.sub('[^a-zA-Z0-9]+','', s2).lower()
print(bool(sorted(str1) == sorted(str2)))