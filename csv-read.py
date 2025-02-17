import csv


students = []

with open("student.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": name, "surname": surname})

for student in students:
    print(f"Name:{student['name']} Surnamed:{student['surname']}")