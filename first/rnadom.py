import random

coin = random.choice(["heads","tails"])
n= random.randint(1,6)
z= ["q","w","e"]
random.shuffle(z)
print(coin)
print(n)
for i in z:
    print(i)

'''from random import choice

coin = choice(["heads","tails"])


print(coin)
'''

