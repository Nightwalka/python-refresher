def main():
    number =get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("whats n: "))
        if n > 0:
             return n
   
    

