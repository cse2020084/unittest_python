class DivisionError(Exception): ...
def add(a,b):
    # add function
    return a+b;

def subtract(a,b):
    # subtract 
    return a-b;

def multiply(a,b):
    # multiplication
    return a*b;
def divide(a,b):
    # division
    if b==0:
        raise DivisionError('Denomiator can not be zero')
    return a // b

