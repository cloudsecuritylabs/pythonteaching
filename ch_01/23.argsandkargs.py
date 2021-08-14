'''
Let's learn about args and keyword args
'''

def name(*args):
    print(args)
    print(type(args))

(name(1,3,4,'cat'))

def name2(*args):
    for arg in args:
        print(arg)

(name2(1, 3, 4, 'cat'))

def my_kwargs(**kwargs):
    print(kwargs)

my_kwargs(name='ankan', lname='basu', age=100)

def my_kwargs2(**kwargs):
    for k,v in kwargs.items():
        print(f'{k} => {v}')

my_kwargs2(name='ankan', lname='basu', age=100)