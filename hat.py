import random

class Hat:

    houses = ["x","t","w"]
    @classmethod
    def sort(cls,name):
        print(name, " is in", random.choice(cls.houses))


Hat.sort("harry")