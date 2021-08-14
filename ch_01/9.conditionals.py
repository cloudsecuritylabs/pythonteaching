x = 99
y = 99

if x > y:
    print('x > y, x is {} and y is {}'.format(x, y))
elif x<y:
    print('x < y, x is {} and y is {}'.format(x, y))
else:
    print('they are the same')

# Python does not have a switch or case statement

# interesting in operator
print('hello' in 'hello world')

programming_languages = ['C', 'java', 'python']

# get iteration number
number = 1
for lang in programming_languages:
    print(number, lang)
    number = number + 1

# get iteration number
for index, lang in enumerate(programming_languages):
    print(index + 1, lang)


# zipping
list1 = [1,2,3]
list2 = ['a', 'b', 'c']
for item in zip(list1, list2):
    print(item)

for number, letter in zip(list1, list2):
    print(number, letter)

print(min(list1))


# print('=>'.join(list1))