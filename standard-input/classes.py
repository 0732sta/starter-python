#start class with Capital Letter
class Planet:
    def __init__(self): #self is parameter in init fun ction
        self.name="Adam"
        self.radius=200000
        self.gravity=5.5
        self.system='adam theory'
    
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

adam=Planet() #self pass to adam
print(f'Name is:{adam.name}')
print(f'Radius is: {adam.radius}')
print(f'the gravity is: {adam.gravity}')
print(adam.orbit())
