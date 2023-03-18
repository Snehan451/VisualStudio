class Car:

    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
        defprinting(self):
        print("Car class is created andcalling from Employee class",self.name,self.model,self.color)
class Employee:
    def __init__(self,empname,empno):
                #self.car=car
                self.empname=empname
                self.empno=empno
    def empdetails(self):
#print("prinitng car details",self.car.name,self.car.model,self.car.color)
        print("priniting employee details",self.empname,self.empno)
#self.car.printing()

sendvalues=Car("Honda","Civic SI","Red")
assign=Employee("Sneha",15)
assign.empdetails()
        