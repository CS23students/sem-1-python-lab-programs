# prime number less than 20

for i in range(2, 20):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
