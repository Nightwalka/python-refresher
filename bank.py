
class Account:
    def __init__(self):
        self._balance =0
    @property
    def balance (self):
        return self._balance
    
    def deposit(self,n):
        self._balance+=n
        

    def withdraw(self,n):
        self._balance-=n
        
        
def main():
    acc = Account()
    print("balance: ", acc.balance)
    acc.deposit(100)
    acc.withdraw(50)
    print("balance: ", acc.balance)

if __name__== "__main__":
    main()







# balance = 0

# def main():
#     print("balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("balance: ", balance)

# def deposit(n):
#     global balance
#     balance+=n
 

# def withdraw(n):
#     global balance
#     balance-=n


    