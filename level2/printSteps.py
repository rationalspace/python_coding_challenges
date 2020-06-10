def printLine(k,steps):
    line = ''
    for i in range(steps):
        line += '#' if i <= k else ' '
    print(line)

steps = int(input("Enter the number of steps "))

for k in range(steps):
    printLine(k,steps)