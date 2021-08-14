'''
Let's learn about list comprehensions
'''

shout = "hello python world OMG LOL!"
mylist = [letter for letter in shout]
print(mylist)

my_vowels = [l for l in shout.lower() if l in 'aeiou']
print(my_vowels)

my_numbers = [num**num for num in range(0,9)]
print(my_numbers)

# dictionary comprehension
keys = ['fname', 'lname', 'age']
values = ['ankan', 'basu', 100]
person = {}
for key, value in zip(keys, values):
    person[key]=value

print(person)

person2 = {
    key:value for key,value in zip(keys, values)
}

print(person2)