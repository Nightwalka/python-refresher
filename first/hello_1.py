
# '''def hello():
#     print(" hello")    
# name = input(" whats your name")
# hello()
# print(name)'''



# '''def hello(to= "world "):
#     print("hello,", to)
# hello()

# name = input("whats your name: ")
# hello(name)
# '''

def main():  
    name = input("whats your name: ")
    # hello(name)
    print(hello(name))

def hello(to= "world "):
    # print("hello,", to)
    return f"hello, {to}"

if __name__ == "__main__":
    main()
