

names= []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
        print(f"Hello,----> {name}")






# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,", line.rstrip())

















# with open("names.txt", "r") as file:
#     lines = file.readlines()



# for line in lines:
#     print("Hello,", line.rstrip())