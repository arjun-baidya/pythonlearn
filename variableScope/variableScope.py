# What do you mean by scope?
# The scope defines the accessibility of the python object. To access the particular variable in the code, the scope must be defined as it cannot be accessed from anywhere in the program. The particular coding region where variables are visible is known as scope.




#global scope example
# x = "I am a Global Variable"
# def someFunction():
#     print("x inside function:", x)
# someFunction()
# print("x outside function:", x)


# Global Scope conflict reslution: Treating global and local variables as different variable name

# x = "I am a Global Variable"
# def someFunction():
#     x = "I am a Local Variable"
#     print("x inside function:", x)
# someFunction()
# print("x outside function:", x)

# Global valiable using global keyword
# def someFunction():
#   global x
#   x = 500
#   print("x inside function:", x)
# someFunction()
# print("x outside function:", x)



#local scope example
# def someSimpleFunction():
#   x = 500
#   print("x inside function:", x)
# someSimpleFunction()
#error will be raised as x is not defined in global scope
#print("x outside function:", x)

#nonlocal variable example
def outerFunction():
    x = "I am local value"
    def innerFuntion():
        nonlocal x
        x = "I am non-local value"
        print("inner function value of x:", x)
    innerFuntion()
    print("outer function value of x:", x)
outerFunction()


# Enclosing Scope in Python
def red():
                a=1
                def blue():
                                b=2
                                print(a)
                                print(b)
                blue()
                print(a)

# In this code, ‘b’ has local scope in Python function ‘blue’, and ‘a’ has nonlocal scope in ‘blue’.

# Of course, a python variable scope that isn’t global or local is nonlocal. This is also called the enclosing scope.


