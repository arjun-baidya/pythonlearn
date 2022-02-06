# Nested (or inner, nested) functions are functions that we define inside other functions to directly access the variables and names defined in the enclosing function. Nested functions have many uses, primarily for creating closures and decorators.

def greet(name):
    def greetFirstName():
        print("Hello " + name + "!")
    greetFirstName()
greet("arjun")
