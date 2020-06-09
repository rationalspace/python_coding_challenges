#in a list of socks or numbers - find pairs and count them

def findPairs(socks):
    pairs = 0
    for i in range(len(socks)):
        s = socks[i]
        if(s and s in socks[i+1:]):
            indexOfFound = socks[i+1:].index(s) + i + 1
            socks[i] = socks[indexOfFound] = None
            pairs += 1
    return pairs

socks = list(map(int,input("Please enter the space separated list sock numbers ").strip().split()))
print("Pairs", findPairs(socks))