import random

class Hat:

    houses = ["x","t","w"]

    def sort(cls,name):
        print(name, " is in", random.choice(self.houses))

hat = Hat()
hat.sort("harry")