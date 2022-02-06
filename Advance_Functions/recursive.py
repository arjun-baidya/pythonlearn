# Recursive functions are functions that calls itself. It is always made up of 2 portions, the base case and the recursive case. The base case is the condition to stop the recursion. The recursive case is the part where the function calls on itself.


# factorial calculation using recursion
def calculateFactorial(x):
    if x == 1:
        return 1
    else:
        return (x * calculateFactorial(x-1))
num = 5
facorial_number = calculateFactorial(num)
print("Factorial of ", num, "is 1 * 2 * 3 * 4 = ", facorial_number)