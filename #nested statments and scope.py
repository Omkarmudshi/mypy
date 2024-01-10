#nested statments and scope
x=50
def func(x):
    print(f"X is {x}")
    #local reassignment
    x=200
    print(f"X is localy change to {x}")
print(func(x))

#############################################


x=50
def func():
    global x
    print(f"X is {x}")
    #local reassignment
    x="new value"
    print(f"X is localy change to global {x}")
    return x

print(x)
print(func())
print(x)
