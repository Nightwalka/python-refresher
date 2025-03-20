x = int(input("What's the range: "))

for i in range(x):
    if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0:
        print(i)
