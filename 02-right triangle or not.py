# right angle triangle or not

a = int(input("Enter side a : "))
b = int(input("Enter side b : "))
c = int(input("Enter side c : "))

# Sort the sides in ascending order
sides = [a, b, c]
sides.sort()

# Check if it forms a right triangle
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("The given sides form a right triangle.")
else:
    print("The given sides do not form a right triangle.")
