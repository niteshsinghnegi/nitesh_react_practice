class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
e1=Employee("nitesh",18)  
print(e1.name)   
print(e1.age)   

print(dir())
# print(help(Employee))

print(e1.__dict__)



x = 5
y = 10
print(x + y * 2)




def add(a, b=5):
    return a + b

print(add(10))



x = "hello"
print(x*3)



















