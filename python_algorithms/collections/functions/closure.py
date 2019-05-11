# As Function Factory
def divide_numbers(x, y):
    return x / y
 # divide_numbers(2, 1) #=> 2

# closure
def divide_closure(x):
    def wrap(y): # wrap closes over y
        return x / y

# close over 2
div_by_2 = divide_closure(2)

print(div_by_2(10)) #=> 5
