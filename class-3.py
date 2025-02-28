

class Student():
    def __init_(self, name,city):
        self.name= name
        self.city= city

    def __str__(self):
        return f"your name is : {self.name} you are from: {self.city}"
    @property
    def name(self):
        return self._name
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, city):
        if city not  in ["x","z","w"]:
            raise ValueError("Plese enter correct city name")
            
        self._city=city      
    @name.setter
    def name(self,name):
        if name:
            self._name=name
        else:
            raise ValueError("Please enter a valid name")

def get_name():
    x= input("Please enter name: ") 
    y= input("now your city: ")     
        