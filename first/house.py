name = input("whats your name: ")

match name:
    case "Harry"| "Ronne":
        print("gryffindor")
    case "Hermione":
        print("Slytherin")
    case _:
        print("who?")