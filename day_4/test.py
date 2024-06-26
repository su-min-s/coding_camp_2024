def function(argument1, argument2, kwarg1=3, kwarg2=2):
    print(argument1, argument2, kwarg1, kwarg2)
    return 'success'

status = function('dog', 'cat', 2, 4)
print(status)

GLOVALVARIABLE = 5
globalvariable = 3
global i
i = 5

## recursion
def factorial(number):
    if number < 0:
        raise ValueError('Negative number is not allowed!!')
    elif number == 1:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))