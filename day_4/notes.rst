try exception

try:
except exception:
else:
finally:

args (no have default values), kwargs (have default values)

def function(*args, **kwargs):
    return
def function(arg0, @args, kwarg0, **kwargs)
    return

Decorators

def decorators(func):
    return func

@decorators
def add_number(a,b):
    return a+b
    