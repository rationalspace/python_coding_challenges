""" 
Print a pyramid for a given number of lines  
   *
  ***
 *****
*******
1->1
2->3
3->5
4->7 
"""

n = int(input("Enter the number of lines of pyramid "))
maxchars = (2 * n) - 1

def printLine(i):
    chars = (2 * i) - 1
    spaces = maxchars - chars
    line = ''
    for j in range(int(spaces/2)):
        line += ' '
    for j in range(chars):
        line += '#'
    for j in range(int(spaces/2)):
        line += ' '
    print(line)

for i in range(1,n+1):
    printLine(i)