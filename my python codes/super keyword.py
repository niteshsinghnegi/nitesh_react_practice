class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer(employee)  :
    def __init__(self,name,id,lang)    :
        super.lang=lang


nitesh=employee("nitesh negi","1035") 
abhishek=employee("abhishek negi","1036")               
print (nitesh.name)
print(nitesh.id)
print(nitesh.lang)