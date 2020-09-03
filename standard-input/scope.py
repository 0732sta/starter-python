my_name='ats' #global

def print_name():
    global my_name #overwrite my_name in local
    my_name='ila' #local
    print('the name inside the function is',my_name)

print_name()
print('outside the function the name is',my_name)