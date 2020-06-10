#given a string of words , capitalise each word
words = list(map(str, input("Enter the string ").split()))
c_words = " ".join([x.capitalize() for x in words])
print(c_words)