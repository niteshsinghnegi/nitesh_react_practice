class Person:
    name="nitesh singh negi "
    occupation="data anyltics"
    networth=10000
    def info(self):
        print (f"{self.name}is a {self.occupation} his salary ")


a= Person()     
b= Person()   
c= Person()     

a.name="shubham"
a.occupation="accountant"

b.name="manyata "
b.occupation="hr"
a.info()
b.info()
c.info()