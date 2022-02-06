# what is map function in python?
# Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.). It is used when you want to apply a single transformation function to all the iterable elements. The iterable and function are passed as arguments to the map in Python.
############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#################
#Syntax of Map in Python

# map(function, iterables)

# n the above syntax:

# function: It is the transformation function through which all the items of the iterable will be passed.
# iterables: It is the iterable (sequence, collection like list or tuple) that you want to map.
# Let’s look at an example to understand the syntax of the map in Python better. The code below creates a list of numbers and then uses the Python map() function to multiply each item of the list with itself.
 
###################@@@@@@@@@@@@@@@@@@@###################

# now we see how a work in for loop or a function and it can be done by map function also 
# Example: Using For Loop
num = [3, 5, 7, 11, 13]

mul = []

for n in num:

    mul.append(n ** 2)

print (mul)


# Example: Using the Python Map() Function
def mul(i):

    return i * i

num = (3, 5, 7, 11, 13)

resu = map(mul, num)

print(resu)

# making the map object readable

mul_output = list(resu)

print(mul_output)


# Example: Using Map() With Len()
example = ["Welcome", "to", "Simplilearn"]

x = list(map(len, example))

print(x)


