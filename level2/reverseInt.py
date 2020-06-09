#reverese an int
def reverseInt(n):
    m = -1 if n < 0 else 1
    n = n if n > 0 else (0 - n)
    return int((str(n)[::-1])) * m

print(reverseInt(int(input("Enter int to be reversed "))))