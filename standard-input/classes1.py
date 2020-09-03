#start class with Capital Letter
class Planet:
    def __init__(self,name,radius,gravity,system): #self is parameter in init fun ction
        self.name=name
        self.radius=radius
        self.gravity=gravity
        self.system=system
    
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

adam=Planet("Adam",200000,5.5,'adam theory') #self pass to adam with parameter
print(f'Name is:{adam.name}')
print(f'Radius is: {adam.radius}')
print(f'the gravity is: {adam.gravity}')
print(adam.orbit())

allisa=Planet('allisa',400000,9.0,'allisa system')
print(f'Name is:{allisa.name}')
print(f'Radius is: {allisa.radius}')
print(f'the gravity is: {allisa.gravity}')
print(allisa.orbit())

#create multiple instances of class by making multiple object and pass data with different attribute
