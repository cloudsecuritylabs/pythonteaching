x = 99
y = 77

if x > y:
    print("x > y")
    print(x)
    print(y)
    z = 55
    print(z)
    # needs to be indented at the same level
    print('x < y, x is {} and y is {}'.format(x, y))

print('Blocks do not define scope of variables in python, functions, objects and modules do')
print(z)