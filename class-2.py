

class Student:
    def __init__(self,name,city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"Your name is {self.name} you are from {self.city}"
    @property
    def name(self):
        return self._name
    @property
    def city(self):
        return self._city
    @name.setter
    def name(self, name):
        if name:
            self._name=name
        else:
            raise ValueError(" Enter a valid name!!!")
    @city.setter
    def city(self,city):
        x = ["c","z","x"]
        if city in x:
            self._city = city
        else:
            raise ValueError("This is not a valid city")
    
def get_name():
    x = input("please enter you name: ")
    y = input("Please enter the city your come from: ")
    student =  Student(x,y)
    return student

def main():
    info = get_name()
    print(f"{info}")

if __name__ == "__main__":
    main()