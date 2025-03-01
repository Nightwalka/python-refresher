

def main():
    yell("Ron can cloud", "In Jesus Name")

def yell(*words):
    uppercase=[]
    for word in words:
        uppercase.append(word.upper())

    print(*uppercase)

if __name__ =="__main__":
    main()