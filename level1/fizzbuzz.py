#if a number is divisble by 5 show "buzz" , if divisble by 3 show "fizz". 
#if divisible by both 3 and 5, then display "fizzbuzz"
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("fizbuzz")
    elif n % 3 == 0 :
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)


while True:
    n = int(input("Fizzbuzz enter number: "))
    fizzbuzz(n)