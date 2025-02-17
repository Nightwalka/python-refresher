

#dics

'''students = {
   "Hermioone": "Gryffindor",
   "harry"    :  "Gryffindor",
   "Ronn"     : "Slytherine"
}
for s in students:
    print(s, students[s], sep=" of house ")'''


students = [
    {"name": "Hermione", "house": "Gryffindor", "petronous": "Otter"},
    {"name": "Ron", "house": "Gryffindor", "petronous": "Owl"},
    {"name": "Harry", "house": "Slytherin", "petronous": "Stag"},
    {"name": "none", "house": "Slytherin", "petronous": "Stag"}
]

for s in students:
    print(s["name"], "of house", s["house"], "with a patronus", s["petronous"])
