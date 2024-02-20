# largest of three numbers

a = int(input("Enter number a: "))

b = int(input("Enter number b: "))

c = int(input("Enter number c: "))

if a > b and a > c:
    print("Largest number is", a)
elif b > a and b > c:
    print("Largest number is", b)
else:
    print("Largest number is", c)
