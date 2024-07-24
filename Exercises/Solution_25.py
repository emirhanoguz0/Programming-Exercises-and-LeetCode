class Personel_info:

    name = "Person"

    def __init__(self,name,age):
        self.name = name
        self.age = age

Dan = Personel_info("Dan",32)

print(Dan.name,Personel_info.name)