'''try:
    x= int(input("NUMBERS ?:::"))
    print(f"number,{x}")
except ValueError :
    print("x is not nmber")'''

'''try:
    x= int(input("NUMBERS ?:::"))
    
except ValueError :
    print("x is not nmber")
else:
    
    print(f"number,{x}")'''


while True:
    try:
         x= int(input("NUMBERS ?:::"))
         break
    except ValueError :
        print("x is not nmber")
  
print(f"number,{x}")