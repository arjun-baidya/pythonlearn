###########@@@@@@@@@################
# what is anonymous function in python?

# Python Lambda Functions are anonymous function means that the function is without a name.
# This function can have any number of arguments but only one expression, which is evaluated and returned

############@@@@@@@@@@@@##########

doSum = lambda a, b: a + b
print(doSum(10, 20))


# same as normal afunction
def doSum(a, b):
    return a + b
aa = doSum(10, 20)
print(aa)

# list filter example to list values greater than 15
# my_custom_list = [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]
# my_filter_list = list(filter((lambda x: x>my_custom_list[2] ),my_custom_list))
# my_filter_list = list(filter((lambda x: x>5 ),my_custom_list))
# print(my_filter_list)


my_custom_list = [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]
my_manipulated_list = list(map(lambda x:x+x, my_custom_list))
print(my_manipulated_list)