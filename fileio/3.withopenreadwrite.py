'''
with
'''

with open("samplecreditcard.txt", 'r') as f:
    print(type(f))
    f.close()

with open("test.txt", 'w') as f:
    f.write("writing from code")
    f.close()

with open("test.txt", 'r') as f:
    content = f.read()
    f.close()

print(content)

# append a file
with open("test.txt", 'a') as f:
    f.write("writing from code 2")
    f.close()

with open("samplecreditcard.txt", 'r') as f:
    lines = f.readline()
    print(lines)
    print(type(lines))
    f.close()
