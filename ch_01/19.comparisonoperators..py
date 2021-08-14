'''
Let's learn about comparison operators
'''

age = 0
if age <= 100:
    print("You are too young")
elif age >100:
    print("You are a strong kid")
else:
    print("We need to talk")

if True:
    print("hey there")

# this does not print anything
if False:
    print("Oh No!")


string = "he he"

if string:
    print("dont smile")
if not string:
    print("can't smile")


mylist = []
if mylist:
    print("dont smile")
if not mylist:
    print("can't smile")

myDict = {}
if myDict:
    print("dont smile")
if not myDict:
    print("can't smile")

list1 = [1,2,3]
list2 = [4,5,6]

if list1 == list2:
    print("hello identical")


cat = "tom"
dog = 'jerry'

if cat == 'tom':
    if dog == 'jerry':
        print("Hi cartoon")

if cat == 'tom' and dog == 'jerry':
        print("Hi cartoon")

# truth table
