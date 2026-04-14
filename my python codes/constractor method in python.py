class person():
    def __init__(self,name,occ):
        print("my name is nitesh ")
        self.name=name
        self.occ=occ

    def info(self):
            print(f"{self.name}is a {self.occ}")

a=person("nitesh","data manager")

# a=person("nitesh","data manager")
b=person("manyata","hr")

a.info()
b.info()
