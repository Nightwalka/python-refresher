import csv

students= []


with open("student.csv") as file:
    for line in file:
        reader = csv.DictReader(file)
        for row in reader:
              students.append({"name": row["name"], "surname": row["surname"]})  # Adjusted keys



for student in sorted(students, key=lambda student: student["name"]):
        
    print(f"Name:---> {student['name']} surnamed---> {student['surname']}")





















# import csv

# students= []


# with open("student.csv") as file:
#     for line in file:
#         reader = csv.reader(file)
#         for name ,surname in reader:
#              students.append({"name": name,"surname":surname})



# for student in sorted(students, key=lambda student: student["name"]):
        
#     print(f"Name:---> {student['name']} surnamed---> {student['surname']}")