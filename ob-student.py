def main ():
    student = get_student()
    print(f"You are : {student[0]} from: {student[1]}")

def get_student():
    n = input("Name: ")
    h = input("city: ")
    return( n,h)

if __name__ == "__main__":
    main()   