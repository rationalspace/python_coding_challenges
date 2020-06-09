#find if a string is a palindrome or not
def palindrome(s):
    rev = s[::-1]
    return bool(s == rev)

print(palindrome(str(input("Enter the string to be tested "))))