#chunk a given array into given smaller pieces
def chunkArray(arr,size): 
    bigArr = []
    index = 0
    while(index<len(arr)):
        temp = arr[index:index+size]
        bigArr.append(temp)
        index += size
    return bigArr

arr = list(map(int,input("Enter the array to be chunked as space separated ").strip().split()))
size = int(input("Enter the size of a chunk "))
print(chunkArray(arr,size))