# class shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def add(self)  :
#         return self.x+self.y
# num1=shape(3,5)      
# print(num1.add())
class shape:
    def __init__(self,x,y)  :
        self.x=x
        self.y=y
    def area(self)  :
        return self.x*self.y

rec=shape(5,8) 
print(rec.area())    
class circle (shape) :
    def __init__(self,radius)  :
        self.radius=radius
        super() .__init__(radius,radius)
def area(self):

    return 3.14*super().area()
c=circle(5)
print(c.area())