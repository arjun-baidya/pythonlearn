# A decorator in Python is a function that takes another function as its argument, and returns yet another function . Decorators can be extremely useful as they allow the extension of an existing function, without any modification to the original function source code.

#decorator example
def formatGreet(func):
    def innerfunc(name):
        print("***************")
        func(name)
        print("***************")
    return innerfunc
    
# def greetFirstName(name):
#         print("Hello ",name)


# prettyGreet = formatGreet(greetFirstName)
# prettyGreet("Sandip")

#or represent with @ as it's a syntactic sugar to implement decorators

@formatGreet
def greetFirstName(name):
        print("Hello ",name)

greetFirstName("Viewer")