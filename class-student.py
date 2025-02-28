

class Student:
    def __init__(self,name,city):

        self.name = name
        self.city = city
        # self.styyle = styyle
    def __str__(self):
        return f"{self.name} from {self.city}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name!!!")
        self._name= name
    # getter
    @property
    def city(self):
        return self._city

    #setter 
    @city.setter
    def city(self, city):
        if city not in ["Harare", "Bulawayo","Vic"]:
            raise ValueError("Invalid city")
        self._city= city



def main():
    student = get_student()
   
    print(student)
    

def get_student():
    
    name = input("Name: ")
    city = input("City: ")
    # styyle = input("Music style: ")
    student =Student(name,city)
    return student

if __name__ == "__main__":
    main()

            
    # def music(self):
    #     match self.styyle:
    #         case "jazz":
    #             return "❤️"
    #         case "rock":
    #             return "😎"
    #         case "gospel":
    #             return "😇"
    #         case _:
    #             return "😒"
#  


    # student = Student()
    # student.name = input("Name: ")
    # student.city = input("City: ")
    # return student


    # student ={}
    # student["name"] = input("Name: ")
    # student["city"]= input("City: ")
    # return student




   














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