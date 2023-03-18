class Student:
    def __init__(self,sname,rollno,sub1,sub2,sub3):
        self.sname=sname
        self.rollno=rollno
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def talk(self):
        print("name of the person is ",self.sname,"roll number is ",self.rollno,
              "Total marks scored is ", self.sub1+self.sub2+self.sub3)
n=input("Enter the name of the student ")
i=int(input("Enter the roll number of the student"))
j=int(input("Enter the marks of fisrt subject"))
k=int(input("Enter the marks of the second subject "))
l=int(input("Enter the marks of the third subject "))
s=Student(n,i,j,k,l)
s.x=90
print(s.__dict__)
print("value stored for x is :",s.x)
del s.sub1
del s.sub2
del s.sub3
print(s.__dict__)
