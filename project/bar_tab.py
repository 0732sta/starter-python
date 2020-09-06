from Tab:

    menu = {
        'tembikai':5,
        'milo':3,
        'soft_drink':2,
        'chicken':10,
        'beef':15,
        'veggie':12,
        'desert':6
    }

    def __init__(self):
        self.total=0
        self.items=[]
    
    def add(self, item):
        #append is add in list
        self.items.append(item)
        self.total+=self.menu[item]

    def print_bill(self,tax,service):
        tax=(tax/100)*self.total
        service=(service/100)*self.total
        total=self.total+tax+service

        for item in self.items:
            print(f'{item:20} RM{self.menu[item]}')
        
    #2f for 2 decimal places
    #:20 is 20 char, to make it print bill looks neat
        print(f'{Total":20} RM{total:2f}')
