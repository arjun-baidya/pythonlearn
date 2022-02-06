# A closure is a nested function which has access to a free variable from an enclosing function that has finished its execution.

# Three characteristics of a Python closure are:
#  it is a nested function.
#  it has access to a free variable in outer scope.
#  it is returned from the enclosing function.

# eample closure
def greet(name):
    # here is non-local variable
    def greetFirstName():
        # nested function
        print("Hello " + name + "!")
    return greetFirstName
    # in closure function time we use return keyword and nested time call the function
firstName = greet("arjun")
firstName()
