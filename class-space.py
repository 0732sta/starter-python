#import package from space folder
#planet is a class name from space
from space.planet import Planet 
#import calc.py
from space.calc import planet_mass,planet_vol

allisa=Planet('allisa',400000,9.0,'allisa system')

allisa_mass=planet_mass(allisa.gravity,allisa.radius)
allisa_vol=planet_vol(allisa.radius)

print(f'{allisa.name} has a mass of {allisa_mass} and a volume of {allisa_vol} ')
