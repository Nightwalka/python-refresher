students = [
    {"name": "Hermione", "house": "x"},
    {"name": "Ron", "house": "x"},
    {"name": "Harry", "house": "x"},
    {"name": "Draco", "house": "y"},
    {"name": "Padma", "house": "z"},
]

# gryffindors=[
#     student["name"] for student in students if student["house"]=="x"
# ]
# for gry in gryffindors:
#     print(gry)


def is_gryfindor(s):
    return s["house"] == "x"


gryffindors = filter(is_gryfindor, students)

for gry in sorted(gryffindors, key=lambda s: s["name"]):
    print(gry["name"])
