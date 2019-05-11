# use to dry up code
# when need to monkey patch a function
# dynamically build behavior by 'stacking functions'

#### For creating generators

def step(start=0, step=1, end=50):
    _start = start
    while _start < end: # if infinite loop, list(stepper) will exhaust memory
        yield _start # yield is both exit and entry point
        _start += step # this gets called after every entry

stepper = step(10, 2)

print(next(stepper)) #=> 10
print(next(stepper)) #=> 12
print(next(stepper)) #=> 14

# Generator Expression
stepper = (x * 5 for x in range(0, 10))
print(list(stepper))
#=> (0,5,10,15,...)


#### As Function Factory
def divide_numbers(x, y):
    return x / y
 # divide_numbers(2, 1) #=> 2

def divide_closure(x):
    def wrapped(y): # wrap closes over y
        return x / y

# close over 2
div_by_2 = divide_closure(2)

print(div_by_2(10)) #=> 5

#### Decorators are closures, @ is syntactic sugar for closing over a function
def logger(func_to_log):
    def wrapped(*args, **kwargs):
        print('Arguments were: %s, %s' % (args, kwargs))
        func_to_log(*args, **kwargs)
    return wrapped

@logger
def my_func(x, y):
    return x * y

print(my_func(10, 15))
#=> Arguments were (10,15), ()
#=> 150


#### Monkey patch a function
def bad_function_from_library(some_attr):
    some_attr / 0

print(bad_function_from_library(10)) #=> ZeroDivisionError

def dont_panic_closure(bad_func):
    def wrappped(some_attr):
        try:
            bad_func(some_attr)
        except:
            print('The bad function unleased zombies!')
    return wrapped

catch_it = dont_panic_closure(bad_function_from_library)
print(catch_it(10))
# => The bad function unleased zombies!
