# reverse and palindrome of strings

str_1 = input("Enter a string: ")

# reverse (slice)
str_2 = str_1[::-1]
print("The reversed string using slice: ", str_2)

# reverse (for-loop)
s = ''
for i in str_1:
    s = i+s
print("The reversed string using for-loop", s)

# palindrome or not
if str_1 == str_2:
    print(str_1, "is a palindrome")
else:
    print(str_1, "is not a palindrome")
