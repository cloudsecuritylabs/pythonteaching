'''
Let's learn about user inputs
'''
age = input("What is your age?") # always returns a string
name = input("What is your name?") # string

print(age)
print(name)

print(f'{name.upper()}')

if age < 100:
    print("You are too young!")