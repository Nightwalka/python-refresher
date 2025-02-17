
name = input("Whats your name? ")

with  open("names.txt", "a")as file:
    file.write(f"{name}\n") 

















# name = input("Whats your name? ")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# name = []
# for _ in range(3):

#     names.append(input("Whats your name? "))

# for name in  sorted(names):
#     print(f"Hello, {name}")