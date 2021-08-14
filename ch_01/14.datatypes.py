# Numerics
# int, floats, complex numbers
# int = 10, 20, 99
# float = 11.11
int_num = 11
float_num = 11.11
print(type(int_num))
print(type(float_num))


## booleans
x = True
y = False

## Sequence (list)
# list is mutable
my_list = ['milk', 'banana', 'egg'] # can have one element multiple times

# tuple is immutable
my_tuples = ('milk', 'banana', 'egg')
# my_tuples.append ==> can't do'

my_sets = {'milk', 'banana', 'egg'} # can't have one item multiple times
string = "hello world"

## strings are also immutable but looks like mutable!!


## dictionary
my_dict = {
    'milk0' : "0% mill",
    'milk2' : "2% milk"
}

person = {
    'name' : 'Kalob',
    'dogs' : 3,
    'family members' : ['mom', 'dad', 'son', 'daughter']
}

# immutable -> value that can not change
# useful for data integrity, or performance

# mutable -> changeable


num = 200,000,000,000
print(type(num))

formatted_num = 100_000_000_000

my_desk_list= [ "pen", "pen", "pencil", "weight", "marker"]
print(my_desk_list[:2])


my_desk_set = { "pen", "pen", "pencil", "weight", "marker"}

print(my_desk_set)
print(my_desk_set.pop())
print(my_desk_set)


my_desk_set = ("pen", "pen", "pencil", "weight")
print(my_desk_set[2])