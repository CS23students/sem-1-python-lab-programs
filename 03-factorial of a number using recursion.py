# factorial of a number using recursion

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


n = int(input("Enter positive integer: "))
res = fact(n)
print("The factorial of a given number: ", res)
