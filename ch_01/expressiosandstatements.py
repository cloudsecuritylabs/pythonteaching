#!/usr/bin/python3
# author: Ankan Basu
# expression -> anything that returns a value
# expressions (unit of execution) -> x = y
# expressions -> x = y
# expressions -> True
# expressions -> F()

# statement --> line of code
# statement --> does not require any semicolon at the end
# statement --> usually one statement per line
print("1"); print(2);

message = "Hello World!"

# print(message)
# print("%s" % message)
# print('{}'.format(message))

def main():
    print_message()

def print_message():
    print('{}'.format(message))

if __name__ == '__main__': main()