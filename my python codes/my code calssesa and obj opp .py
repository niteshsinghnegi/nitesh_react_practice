#class and object in python oops concepts 

class person:
    name="nitesh singh negi"
    occ="data manager"
    salary=3500000
    age=24

    def info(self):
        print(f"my name is {self.name}is {self.occ}and his salary {self.salary} and his age {self.age }")
 
a=person()
b=person()
c=person()


a.name="shubham"
a.occ="data anylistcis "
a.salary=1000000
a.age=23

b.name="manyata"      
b.occ="hr"  
b.salary=100000
b.age=22

a.info()
b.info()
c.info()
        