class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name.strip(), int(age.strip()))

# Create the instance outside the class
person = Person.from_string("john doe ,20")
print(person.name, person.age)

class Rectangle:
    def __init__(self,width,hight):
        self.width=width
        self.hight=hight

    @classmethod
    def square(cls,size):
            return cls(size,size)
        
Rectangle=  Rectangle.square(10)
print("width:",Rectangle.width)
print("hight:",Rectangle.hight)

class Employee:
     def __init__(self,name,salary):
          self.name=name
          self.salary=salary
@classmethod
def fromstr(cls,string)  :
     return cls (string.split ("-")[0],int (string.split("-)[1]")))

e1=Employee("nitesh",25000)
print(e1.name)
print(e1.salary)

string="khushal-15000"
e2=Employee.fromstr(string)
print(e2.name)
print(e2.salary)
                 
         
