class Travelbooking:
    def __init__(self,fromloc,to):
        self.fromloc=fromloc
        self.to=to
        self.amt=0
    def farecal(self):
        if ((self.fromloc=="Bangalore" and self.to=="Chennai") or 
        (self.fromloc=="Bangalore" and self.to=="Hyderabad") ):
            self.amt=3000
        elif ((self.fromloc=="Bangalore" and self.to=="Delhi") or 
              (self.fromloc=="Bangalore" and self.to=="Kolkatta") ):
            self.amt=6000
        elif ((self.fromloc=="Chennai" and self.to=="Bangalore") or 
              (self.fromloc=="Chennai" and self.to=="Hyderabad")):
            self.amt=4000
        elif ((self.fromloc=="Chennai" and self.to=="Delhi") or 
        (self.fromloc=="Chennai" and self.to=="Kolkatta")):
            print("to dest is",to)
            self.amt=7000
        else:
            print("Sorry No flights avaqilable")
       
fromloc=input("enter the from location: Bangalore or Chennai\n")
to=input("enter the detination: select among Chennai,Hyderabad,Delhi\n")
t=Travelbooking(fromloc,to)
t.farecal()
print("Your total fare is ",t.amt)
