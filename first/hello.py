# i had forgottn how to code haha and is it even necessary anymore 
name= input("whats your name: ").strip().title()
#say hello --> sudo code allows you to write your logic when writing a script 

'''print("Hello : "+ name)
print(" Hello, ", name)
print(" hello,",end="")
print(name)


print('hello,"friend"')
print('hello,"friend"')'''
#formatting and cleaning up
#name = name.strip()
#name = name.capitalize()

#name = name.strip().title()
# split users name
first, last = name.split(" ")

print(f'hello,"{name}"')
print(f'hello,"{last}"')
print(f'hello,"{first}"')

