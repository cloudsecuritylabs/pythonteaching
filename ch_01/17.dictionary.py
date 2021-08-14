'''
Let's learn about dictionary
'''

name = "Basu"
age = 50
height = 5
kids = 2

# dictionary can be used to group data together
dict_basu = {
    'name' : "Basu",
    'age' : 50,
    'height' : 5,
    'kids' : 2,
    'grocery_list' : ['banana', 'milk', 'egg']
}

print(dict_basu)
print(dict_basu['kids'])
print(dict_basu['kids'] == 2)
print(dict_basu['grocery_list'][1])

del(dict_basu['kids'])
print(dict_basu)

keys = dict_basu.keys()
values = dict_basu.values()

print(keys)
print(values)

info = input("what is the information do you want for basu? ")
data = dict_basu.get(info)
print(data)

# looping over a dic
for key,value in dict_basu.items():
    print(key, " =>", value)