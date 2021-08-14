'''
Let's learn about filter
'''
def filter_get_even(num):
    return num % 2 == 0

num = [1,2,3,4,5,6,7,8,9,10]

# using filter
# note we are passing the function name only. no parameters
for n in filter(filter_get_even, num):
    print(n)