#decorate like function that receive a function as argument and return a another function

def decorator_01(inner_function_01):

    def wrapper():
        print(inner_function_01()+ ' ' + 'result with inner function')
    
    return wrapper

@decorator_01
def inner_function_01():
    return 'inner_function_01'

inner_function_01()




#another example with arguments

def decorator_02(inner_function_02):

    def wrapper(*args, **kwargs):
        print(f'{inner_function_02(*args, **kwargs)} result with inner function')
    
    return wrapper

@decorator_02
def inner_function_02(x,y):
    return x + y

inner_function_02(8,9)