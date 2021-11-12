# Creating a function
def my_function():
    print("Hello from a function")

# Calling a Function
my_function()

# Arguments
def my_function(fname):
    print(fname + " Rakojoana")
my_function("David")
my_function("Lilly")
my_function("Amo")

# Number of Parameters
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Deiv", "Rakojoana")

# Arbitrary Arguments, *args
"""
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
"""
def my_function(*cities):
    print("The capital city is " + cities[2])

my_function("Mafeteng", "Mohale's Hoek", "Maseru", "Quthing", "Mokhotlong", "Thaba-Tseka", "Berea", "Qacha's Nek", "Leribe")

# Keyword Arguments
"""You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter."""
def my_function(city3, city2, city1):
    print("The 3rd city is " + city3)

my_function(city1="Mafeteng", city2="Berea", city3="Maseru")

# Passing a list as an argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return values
def my_function(x):
    return 5 * x

print(my_function(10000))
print(my_function(4))
print("\t", my_function("Deiv"))

# Recursion
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

##########################################################################################################################
def greet(name):
    print("Hello " + name)

greet("Amo")