# function are used to perform some action
# function is called when we call it
# A Python function is a group of code. ... A function can be called from anywhere after the function is defined. Functions can return a value using a return statement. Functions are a common feature among all programming languages

# to return a value from a function, use the return statement
# to avoid repeating the same logic over and over again, we can use functions


# parameters are variables that are used to pass values to a function
# information that is passed to a function is called an argument
# parameter are also called arguments

import os
calculation_to_units = 24
name_of_units = "hours"

def days_to_units(name_of_days):
    # dynamic print
    print("{} {}".format(name_of_days, name_of_units))
    print("ok")

days_to_units(35)

#Define a fuction
# def my_hello_world_function():
#   print("Hello World from a function")

#calling a function
# my_hello_world_function()

#Define a function with sigle parameter
# def greet_person(name):
#   print("Hi "+ name)
# greet_person("Sandip")

#Define a function with Multiple parameter
# def greet_full_name(first_name, last_name):
#   print("Hi "+ first_name + " " + last_name)
# greet_full_name("Sandip", "Das")

#Arbitrary Arguments, *args whe not sure how much parameters will be there
# def my_colours(*colours):
#   print("The second colours is " + colours[1])
# my_colours("Red", "Green", "Blue")

#Arbitrary Arguments, *args whe not sure how much parameters will be there
# def my_named_colours(**colours):
#   print("The first colours is " + colours["red"])
# my_named_colours(red = "Red Colour", blue = "Blue Colour", green = "Green Colour")

# Use return statement to return a value from a function


def sum(a, b):
  return a + b


sumValue = sum(5, 10)
print("The Sum is", sumValue)
print("Type of sumValue is", type(sumValue))

