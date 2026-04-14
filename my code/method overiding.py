class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self) :
        return self.x* self.y
class cricle (shape)  :
    def __init__(self,radius):
        self.radius=radius
        super(). __init__(radius,radius)
    def _area(self):
            return 3.14*super().area()
rec=shape(3,5)
print(rec.area())
c=cricle(5)
print(c.area())
class square:
     def __init__(self,a):
          self.a=a

        #   super(). __init__(a,a)
     def area(self) :
          return self.a*self.a
s =square(5)
print(s.area())    
               
          
     


        
    

                     






