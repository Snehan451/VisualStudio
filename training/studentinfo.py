class Studentinfo:
    def __init__(self,sname,marks):
        self.sname=sname
        self.marks=marks
    def display(self):
        print("you got",self.sname,"marks",self.marks)
    def grade(self):
        if self.marks>=90:
            print("A grade")
        elif self.marks>=60:
            print("B grade")
        else:
            print("c grade")
n=int(input("enter the number of student details "))
for i in range(n):
  name=input("enter name")
  marks=int(input("enter marks"))
  s=Studentinfo(name,marks)
  s.display()
  s.grade()


        