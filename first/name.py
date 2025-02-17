import sys


'''try:
    print("hello my name is", sys.argv[1])
except IndexError:
    print("no arg")'''

'''
if len(sys.argv)<2:

    sys.exit("too few arg")
elif len(sys.argv)>2:

    sys.exit("too many arg")


print("hello my name is", sys.argv[1])'''






if len(sys.argv)<2:
    
    sys.exit("too few arg")
for arg in sys.argv[1:]:   #slice[1:]  removes the firstn element 

    print("hello, my namwe is", arg)

