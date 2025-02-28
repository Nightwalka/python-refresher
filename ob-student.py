def main ():
    student = get_student()
    if student["name"] == "Ron":
        student["city"] = "Shenzhen"
    print(f"You are : {student['name']} from: {student['city']}")

def get_student():
    name = input("Name: ")
    city = input("City: ")
    return {"name": name, "city": city}


    # student ={}
    # student["name"] = input("Name: ")
    # student["city"]= input("City: ")
    # return student




if __name__ == "__main__":
    main()   














# def main ():
#     student = get_student()
#     print(f"You are : {student[0]} from: {student[1]}")

# def get_student():
#     n = input("Name: ")
#     h = input("city: ")
#     return( n,h) # turple
#     #return [n,h]

# if __name__ == "__main__":
#     main()   