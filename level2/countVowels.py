vowels = ['a','e','i','o','u']
cnt_vowels = 0
for c in str(input("Enter the string ")):
    if c in vowels:
        cnt_vowels += 1
print(cnt_vowels)