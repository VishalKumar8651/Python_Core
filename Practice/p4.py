class Student:
    
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def average(self):
        average = (self.marks1 +self.marks2 +self.marks3)/3
        return self.average
    
s1 = Student("Vishal" ,90,95,99)
s2= Student("Aman",10,15,18)
print(s1.name)
print(s1.average())
