# integer to roman numeral
num = int(input("Enter a number : "))
val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

roman_num = " "

i = 0
while num > 0:
    count = num // val[i]
    roman_num += sym[i] * count
    num -= val[i] * count
    i += 1

print(f"The Roman numeral is: {roman_num}")
