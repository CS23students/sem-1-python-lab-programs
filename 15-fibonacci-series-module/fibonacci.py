# fibonacci series function

def fibonacci(n):
    f1 = 0
    f2 = 1
    print(f1)
    print(f2)
    i = 2
    while i <= n:
        f3 = f1+f2
        print(f3)
        f1 = f2
        f2 = f3
        i = i+1
