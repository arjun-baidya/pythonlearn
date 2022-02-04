##########################################
# 5 Types of Arguments in Python Function Definition:
# default arguments
# keyword arguments
# positional arguments
# arbitrary positional arguments
# arbitrary keyword arguments
###########################################

#################################
# default arguments:
# Default arguments are values that are provided while defining functions.
# The assignment operator = is used to assign a default value to the argument.
# Default arguments become optional during the function calls.
# If we provide a value to the default arguments during function calls, it overrides the default value.
# The function can have any number of default arguments
# Default arguments should follow non-default arguments.
def add(a,b=5,c=10):
    return (a+b+c)

################################################

################################################
# Keyword Arguments:
# Functions can also be called using keyword arguments of the form kwarg=value.
# During a function call, values passed through arguments need not be in the order of parameters in the function definition. This can be achieved by keyword arguments. But all the keyword arguments should match the parameters in the function definition.

def add(a,b=5,c=10):
    return (a+b+c)

#####################################################

###############################################
# Positional Arguments
# During a function call, values passed through arguments should be in the order of parameters in the function definition. This is called positional arguments.
# Keyword arguments should follow positional arguments only.

def add(a,b,c):
    return (a+b+c)

############################# @@@@@@@@@@ Important points to remember: @@@@@@@@@####################

# 1. default arguments should follow non-default arguments
def add(a=5,b,c):
    return (a+b+c)

#Output:SyntaxError: non-default argument follows default argument

# 2. keyword arguments should follow positional arguments
def add(a,b,c):
    return (a+b+c)

print (add(a=10,3,4))
#Output:SyntaxError: positional argument follows keyword argument

# 3. All the keyword arguments passed must match one of the arguments accepted by the function and their order is not important.
def add(a,b,c):
    return (a+b+c)

print (add(a=10,b1=5,c=12))
#Output:TypeError: add() got an unexpected keyword argument 'b1'

# 4. No argument should receive a value more than once
def add(a,b,c):
    return (a+b+c)

print (add(a=10,b=5,b=10,c=12))
#Output:SyntaxError: keyword argument repeated

# 5. Default arguments are optional arguments
def add(a,b=5,c=10):
    return (a+b+c)

print (add(2))
#Output:17

################@@@@@@@@@@@@@@@@@@@#################################

#############################
# Variable-length arguments
# Variable-length arguments are also known as arbitrary arguments. If we don’t know the number of arguments needed for the function in advance, we can use arbitrary arguments

# Two types of arbitrary arguments
# arbitrary positional arguments
# arbitrary keyword arguments
######################################
#4. arbitrary positional arguments:
# For arbitrary positional argument, an asterisk (*) is placed before a parameter in function definition which can hold non-keyword variable-length arguments. These arguments will be wrapped up in a tuple. Before the variable number of arguments, zero or more normal arguments may occur.

def add(*b):
    result=0
    for i in b:
         result=result+i
    return result

print (add(1,2,3,4,5))
#Output:15
print (add(10,20))
#Output:30

###########################################

##########################

# 5.arbitrary keyword arguments:
# For arbitrary positional argument, a double asterisk (**) is placed before a parameter in a function which can hold keyword variable-length arguments.

def fn(**a):
    for i in a.items():
        print (i)
fn(numbers=5,colors="blue",fruits="apple")
'''
Output:
('numbers', 5)
('colors', 'blue')
('fruits', 'apple')
'''

########################################################
# Special Parameters:
# By default, arguments may be passed to a Python function either by position or explicitly by keyword. For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.

###########################

#################@@@@@@@Important points to remember: @@@@@@@@@@@####################
# Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning.

# Use positional-only if you want to enforce the order of the arguments when the function is called.

# Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names.

# Use keyword-only when you want to prevent users from relying on the position of the argument being passed.


############################# @@@@@@@@@@@@@@@@@@@@@@@@@@@#########################
