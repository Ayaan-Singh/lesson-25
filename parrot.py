class bird:
    species = "parrot"
    def __init__(self,name,age):
        self.name = name
        self.age = age

blu = bird("blu",12)
woo = bird("woo",13)
     
print (f"{blu.name} is a {blu.species} whose age is {blu.age}")
print (f"{woo.name} is a {woo.species} whose age is {woo.age}")
