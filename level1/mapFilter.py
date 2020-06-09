def square(n):
    return n * n

arr = list(map(int,input("Please enter a space separated list of numbers ").strip().split()))

#map applies the mentioned function on each element of the list
print("The squares:")
print(list(map(square,arr)))

def isOdd(n):
    return bool(n%2)

#filter applies a function to each element of list and returns only those elements who are True by the function
print("The odd numbers are:")
print(list(filter(isOdd,arr)))