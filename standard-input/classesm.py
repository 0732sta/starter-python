#start class with Capital Letter
class Planet:

    shape='round' #attribute shape

    def __init__(self,name,radius,gravity,system): #self is parameter in init fun ction
        self.name=name
        self.radius=radius
        self.gravity=gravity
        self.system=system

#instance method
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

#class method
    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

#static method
    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'The planet spins and spins a {speed}'

allisa=Planet('allisa',400000,9.0,'allisa system')

#can be access class and static method but not instance method
print(Planet.commons())
print(Planet.spin())
print(Planet.spin('a very high speed')) #overwrite

#create multiple instances of class by making multiple object and pass data with different attribute
