# A string is a series of characters. Anything inside quotes is considered a string in Python

message1 = 'this is a string my friend'
message2 = 'this is also a string my friend'

name = 'crystal ball'
print(name.title())

print(name.upper())
print(name.lower())

# using variables in strings

firstname = 'crystal'
lastname = 'ball'
fullname = f'{firstname} {lastname}'  # f-strings were introduced on Python 3.5
print('{}'.format(firstname + " " + lastname))
print(fullname.upper())

# newlines and tabs
print("Languages:\nPython3\nC\nJavaScript")
print("Languages:\n\tPython3\n\tC\n\tJavaScript")

# strip out extra spaces
favorite_language = 'python3 '
print(favorite_language.rsplit())