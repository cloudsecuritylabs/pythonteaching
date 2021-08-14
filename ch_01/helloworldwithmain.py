#!/usr/bin/python3
# author: Ankan Basu
# using conditional at the bottom enforces python to read all of the code before
# executing anything

message = "Hello World!"

# print(message)
# print("%s" % message)
# print('{}'.format(message))

def main():
    print_message()

def print_message():
    print('{}'.format(message))

if __name__ == '__main__': main()