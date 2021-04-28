# defining function
def fibo(x):
    if x <= 1:
        return x
    else:
#function formula
        return (fibo(x-1)) + fibo(x - 2)
# the sequence will till the 20th term
terms = 20

if terms <= 0:
    print("enter positive number")
# if the number of terms entered are positive the fibonacci sequence will be printed
else:
    print("Fibonacci sequence: ")
    for i in range(terms):
        print(fibo(i))
