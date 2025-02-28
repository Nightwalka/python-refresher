

class Student:
    #intilitizing the the constructor for the classs Student
    def __init__(self,name ,city):
        #assign or record to the memory the values fromn the constructor that were passed as parameters
        self.name = name
        self.city = city

    # the method to deal with readable output
    def __str__(self):
        return f"Your are : {self.name} from : {self.city}"
    
    #the private att 
    #getter 
    @property
    def name(self):
        return self._name 
    
    @property
    def city(self):
        return self._city
    
    @name.setter
    def name(self,value):
        if value:
            self._name=value
        else:
            raise ValueError(" Please enter a valid name")

    @city.setter
    def city(self,value):
        match value:
         case  "v":
             self._city=value
         case  "h":
             self._city=value
         case  "z":
             self._city=value
         case _:
        
            raise ValueError("Please enter the correct city")

#a func to get the student info
def get_student():
    name = input("Please enter your name: ")
    city = input("Please enter the city you are from: ")
    student = Student(name,city)
    return student
    
#the main func that calls the get student 
def main():
    student = get_student()
    print(f"{student}")


if __name__ == "__main__":
    main()
