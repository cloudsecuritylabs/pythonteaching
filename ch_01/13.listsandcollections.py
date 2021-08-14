###
### list (arrays in other programming languages) is a collection of item in a particular order
### good to make the name of list variable as a plural one
###

fruits = ['apple', 'oranges', 'banana', 'pear']
print(len(fruits))
print(fruits[0])
print(fruits[-1]) # last element

message = f"My favorite fruit was a/an {fruits[0].title()}."
print(message)


# modifying element in a list
fruits[0] = "watermelon"
print(fruits)

# adding an element to the end
fruits.append('apple') # put the apple back in the list please!
print(fruits)

# adding element to a particular position
fruits.insert(1, "plum")
print(fruits)

# removing element from a list in a particular position
del(fruits[1])
print(fruits) # let's get rid of plum

# using pop
popped_fruit = fruits.pop(3)
print(popped_fruit)
fruits.append(popped_fruit)
popped_fruit = fruits.pop()
print(popped_fruit)
fruits.append(popped_fruit)


# remove item by value
fruits.remove('apple') # note: only deletes the first occurance
print(fruits)

fruits.append('apple')
fruits.append('apple')
print(fruits)
fruits.remove('apple')
print(fruits)


# sorting
