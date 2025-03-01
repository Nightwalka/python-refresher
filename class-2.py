

class Student:
    def __init__(self,name,city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"Your name is {self.name} you are from {self.city}"
        
    @classmethod
    def get(cls):
        name= input("Name: ")
        city= input("City: ")
        return cls(name,city)
    

def main():
    info = Student.get()
    print(f"{info}")

if __name__ == "__main__":
    main()