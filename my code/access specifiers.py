#concept of class and object 

class Details:
    name='nitesh'
    age= 18
obj=Details()
print(obj.name)
print(obj.age)

# concept of self parameter 
class Employee:
    employeename = "hari"
    employeesalary = 18000
    employeedepartment = 'finance'

    def desc(self):
        print(f"My name is {self.employeename}, my salary is {self.employeesalary}, "
              f"and my department is {self.employeedepartment}")

# object creation
object1 = Employee()
object1.desc()

# concept of constructors

# 1.paramenterized construrcter 
class detail:
    def __init__(self,subject,marks):
        self.subject="maths"
        self.marks=98
a=detail("maths",98)
b=detail("science",97)  
print(a.subject,"name of subject",a.marks,"i got marks")      

# 2 . default constractor
class detail:
    def __init__(self):
        print("nitesh is a good boy its become a data manger in microsoft")
object=detail()


# decorater in python 
def Greet (fx):
    def mfx(*args,**kwargs):
        print('good morming sir')
        fx(*args , **kwargs)
    print('thanks for using this function ')
    return mfx
@Greet
def hello():
    print('hello world')
@Greet
def add(a,b)  :
    print(a+b)  
hello()
add(1,2)
import logging
def log_function_call(func):
    def decorated (*args ,**kwargs):
        logging.info(f"calling{func.__name__}with args{args},kwargs{kwargs}")
        result=func(*args,**kwargs)
        logging.info(f"{func.__name__}returned {result}")
        return result
    return decorated
@log_function_call
def my_function(a,b):
    return a+b
 
# getter and setter in python 
class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10


obj = Myclass(10)
obj.ten_value = 67   # setter call hoga -> self._value = 67/10 = 6.7
print(obj.ten_value) # getter call hoga -> 10 * 6.7 = 67.0

#inheritance in python
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def ShowDetails(self):  
        print(f"the name of employee {self.name}and his id {self.id}.")  
        class Programmer(Employee):
            def ShowDetails(self):
                print("default laguage is python")

e1=Employee("nitesh",400)
e2=Employee("hari",410)
e3=Employee("dinesh",440)

e1.ShowDetails()
e2.ShowDetails()
e3.ShowDetails()

# #access sepicifiers
# #1.public sepicifierss

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# object=Student(21,"nitesh")    
# print(object.age)  
# print(object.name)  

# # 2:private specifiers
# class Student: 
#     def __init__(self, age, name): 
#         self.__age = age      # An indication of private variable
        
#         def __funName(self):  # An indication of private function
#             self.y = 34
#             print(self.y)

# class Subject(Student):
#     pass

# obj = Student(21,"Harry")
# obj1 = Subject

# # calling by object of class Student
# print(obj.__age)
# print(obj.__funName())

# # calling by object  of class Subject
# print(obj1.__age)
# print(obj1.__funName())

# # #name mangling in python 
# class MyClass:
#     def __init__(self):
#         self._nonmangled_attribute = "I am a nonmangled attribute"
#         self.__mangled_attribute = "I am a mangled attribute"

# my_object = MyClass()

# print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
# print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute

# #protacted sepicifiers
# class Student:
#     def __init__(self):
#         self._name = "Harry"

#     def _funName(self):      # protected method
#         return "CodeWithHarry"

# class Subject(Student):       #inherited class
#     pass

# obj = Student()
# obj1 = Subject()

# # calling by object of Student class
# print(obj._name)      
# print(obj._funName())     
# # calling by object of Subject class
# print(obj1._name)    
# print(obj1._funName())

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())