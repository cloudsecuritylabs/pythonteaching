numbers = ['one', 'two', 'three', 'four', 'five']

n = 0

while n < 5:
    print(numbers[n])
    n = n + 1

print("Another loop")
for num in numbers:
    print(num)

# Python does not have a switch or case statement

my_tuple = ('honey', 'rice', 'lemon')
for item in my_tuple:
    print(item)

my_double_tuple = (
    ('ab', "50"),
    ("sb", "44"),
    ("ob", "7"),
    ("mb", 6)
)

# an example of unpacking
# inside tuples must be consistent in number of items
for (person, age) in my_double_tuple:
    print(f'{person} is {age} old')


person = {
    "first_name" : "Ankan",
    "last_name" : "Basu",
    "age" : 100,
    "occupation" : "teacher"
}

for key in person:
    value = person[key]
    print(key, value)

print(person.items())
print(person.items())

for key, value in person.items():
    print(f'{key} is {value}')


# let's understand break and continue
num = ['one', 'two', 'three', 'four', 'five']

for n in num:
    if n == 'three':
        continue
    print(n)


for n in num:
    if n == 'three':
        break
    print(n)

# you can also use break and continue with while
