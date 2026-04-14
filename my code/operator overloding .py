class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}j"
    def __add__(self,x):
        return vector(self.i+x.i,self.j+x.j,self.k+x.k)
v1=vector(3,5,6)
print(v1)
v2=vector(5,8,9)
print(v2)
print(v1+v2)
    
class Triangle:
    def __init__(self, c, d, e):
        self.c = c
        self.d = d
        self.e = e

    def __str__(self):
        return f"{self.c}, {self.d}, {self.e}"

    def __add__(self, other):
        return Triangle(self.c + other.c, self.d + other.d, self.e + other.e)


t1 = Triangle(8, 3, 4)
print("Triangle 1:", t1)

t2 = Triangle(8, 6, 7)
print("Triangle 2:", t2)


t3 = t1 + t2
print("Sum of triangles:", t3)
