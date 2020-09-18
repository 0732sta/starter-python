#function must match with decoretor
def cough_dec(func):

    def func_wrapper():
        #code before function
        print('*cough*')
        func()
        #code after function
        print('*cough*')

    return func_wrapper

#if not apply decoretor the code not run the behavour
@cough_dec
def question():
    print('can you give me a discount on that?')


@cough_dec
def answer():
    print("it's only 50p you cheapskate")

question()
answer()