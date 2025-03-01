


def meow (n: int) ->str:
    """" 
    Meows n times.
    :param n: Number of times to meow.
    :raise TypeError: if not an int
    """
    return "meow\n"*n
        

number: int = int(input("Numner: "))
meows: str = meow(number)
print(meows, end="")