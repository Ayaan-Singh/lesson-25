class veh :
    def __init__(self,name,maxspeed,mileage):
       
        self.maxspeed = maxspeed
        self.mileage = mileage
        self.name = name
modelx = veh("modelx",240,18)
modelx2_0 = veh ("modelx2_0",256,25)

print (f"the max speed of {modelx.name} is",modelx.maxspeed)
print (f"the mileage  of {modelx.name} is",modelx.mileage)
print (f"the max speed of {modelx2_0.name} is",modelx2_0.maxspeed)
print (f"the mileage  of {modelx2_0.name} is",modelx2_0.mileage)


