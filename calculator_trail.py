import math
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def square(a):
    return a**2
def square_root(a):
    return math.sqrt(a)
def cube(a):
    return a**3


a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(square(a))
print(square_root(a))
print(cube(a))

