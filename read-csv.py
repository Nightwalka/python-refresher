
#sorting the studenst whoa RE IN A LIST AND A DICTIONARIES AND PACING A FNC AR ARGUEMENT TO A FUNCTION  

students= []


with open("names.csv") as file:
    for line in file:
        name,surname = line.rstrip().split(",")
        student ={"name": name, "surname": surname}
        students.append(student)


def get_name (student):
        return student["name"]


for student in sorted(students, key=get_name):
        
    print(f"Name:---> {student['name']} surnamed---> {student['surname']}")












# students= []


# with open("names.csv") as file:
#     for line in file:
#         name,surname = line.rstrip().split(",")
#         student ={"name": name, "surname": surname}
#         students.append(student)
 
# for student in students:
        
#     print(f"Name:---> {student['name']} surnamed---> {student['surname']}")















# with open("names.csv") as file:
#     for line in file:
#         name,surname = line.rstrip().split(",")
#         print(f"{name} {surname}")








# with open("names.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} {row[1]}")