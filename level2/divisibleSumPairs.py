#find how many pairs of numbers are there in a given array divisible by x. Print those pairs
def findDivisibleSumPairs(arr,x):
    bigArr = []
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if((arr[i] + arr[j]) % x == 0):
                bigArr.append([arr[i],arr[j]])
                count += 1
    return(bigArr,count)

arr = list(map(int,input("Please enter the space separated list for divisible sum pairs ").strip().split()))
x = int(input("Please enter the number to be tested for divisibility "))
( bigArr, count ) = findDivisibleSumPairs(arr,x)
print(bigArr)
print(count)