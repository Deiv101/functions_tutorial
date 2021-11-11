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
