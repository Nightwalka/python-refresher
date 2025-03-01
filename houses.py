

students = [
    {"name": "Hermione", "house": "x"},
    {"name": "Ron", "house": "x"},
    {"name": "Harry", "house": "x"},
    {"name": "Draco", "house": "y"},
    {"name": "Padma", "house": "z"}
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)