#given a 6 by 6 array, find the hour glass that has maximum sum
arr = list(map(int,input("Please enter the space separated list for 6 by 6 matrix ").strip().split()))
big = []
i = 0
i = 0
tempsum = 0
maxsum = 0
hourglass = []

#create 6 by 6 array
while(i<len(arr)):
    temp = arr[i:i+6]
    big.append(temp)
    i += 6

#find max hour glass sum
for i in range(4):
    for j in range(4):
        tempsum  = big[i][j] + big[i][j+1] + big[i][j+2]
        tempsum += big[i+1][j+1]
        tempsum += big[i+2][j] + big[i+2][j] + big[i+2][j]
    if(tempsum>maxsum):
        hourglass = []
        maxsum = tempsum
        hourglass.append([big[i][j],big[i][j+1],big[i][j+2],big[i+1][j+1],big[i+2][j],big[i+2][j],big[i+2][j]])


print(hourglass)
print(maxsum)