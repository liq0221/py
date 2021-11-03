class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        print("%s的年龄是%d"%(self.name,self.age))
        

student = Student("xixi",10)
student.__str__()

        