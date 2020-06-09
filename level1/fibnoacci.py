#fibnoacci series - each number in the series is the sum of its previous 2
#1,1,2,3,5,8

# fibnoacci recursive function becomes very expensive (exponential) and takes a lot of time to calculate - if you try for small indexes like 50
# this will create a cache of function results  - you can apply this memoization technique to make it faster
def memoize(f):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x]  = f(x)
        return cache[x]
    return helper

@memoize
def fibnoacci(n):
    if n<2:
        return n
    else:
        return fibnoacci(n-2) + fibnoacci(n-1)

number = int(input("Fibnoacci number of which index? "))
print(fibnoacci(number))