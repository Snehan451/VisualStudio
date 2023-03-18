#Costumerdetails
import sys
class Customer:
    bankname="KOTRAKBANK="
    def __init__(self,name,balance=0):
       self.name=name
       self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("after depositing the amount the balance is ", self.balance)  
    def withdraw(self,amt):
        if amt>self.balance:
            print("amount is not sufficient, withdrawal not permitted ")
            sys.exit()
        
        self.balance=self.balance-amt
        print("  the amount after withdrawl balance is ",self.balance)
print(" welcome to kotak banking system ",Customer.bankname)#calling the bankname variable 
# lets input the value for the name and balance and option deposit and withdraw
name=input(" enter your name ")
c=Customer(name) # we are sending the name
while True:
    print("  d deposit w withdraw e-exit ")
    option=input(" enter your option ")
    if option=="d" or option=="D":
        amt=float(input(" enter amount "))
        c.deposit(amt)
    elif option=="w" or option=="W":
        amt=float(input(" enter amount  to withdraw "))
        c.withdraw(amt)
    elif option=="e" or option=="E":
        print(" Thank you banking with us ")
        sys.exit()
    else:
        print(" invalid option pls choose valid option only ")
        