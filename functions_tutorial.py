# Creating a function
def my_function():
    print("Hello from a function")

# Calling a Function
my_function()
####################################################################################################################################################################

# Arguments
def my_function(fname):
    print(fname + " Rakojoana")
my_function("David")
my_function("Lilly")
my_function("Amo")

####################################################################################################################################################################

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
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning")

greet("Amo")



# Example of return
def abs_value(num):
    """This function returns the absolute value of the entered number"""
    if num >= 0:
        return num
    else:
        return -num

print(abs_value(-5)); print(abs_value(3))

###########################################################################################################################
print("\t")
def greet(name, msg):
    """This function greets the person with the provided message"""
    print("Hello"  + name + ", " + msg)

greet("Amo", "Top of the morning to you!")

###########################################################################################################################
# Default arguments
def greet(name, msg = "Good morning!"):
    """This function greets the person with the provided message"""
    """If the message is not provided, it defaults to 'Good morning!'"""
    print("Hello, ", name,'' + msg)

greet("Amo,")
greet("Amo,", "How are you this morning?")

###########################################################################################################################
print("\n")
# Recursive function
def factorial(x):
    """This is a recursive function to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 7
print("The factorial of num", num, "is", factorial(num))

###########################################################################################################################
print("\n")
def calc(num1, num2):
    add = num1 + num2
    print("The Sum of ", num1, "&", num2, "is", add)

calc(2, 4)
###########################################################################################################################
print("\n")
def func(a, b, c):
    lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if num in lis:
        print("The fifth number is", lis[5])
    else:
        return num
func(2, 4, 6)

###########################################################################################################################
print("\n")
def iter(a):
    x = int(input("Enter a number: "))
    while x <= 0:
        print("The number you entered is: ", x)
        break
    else:
        return x
iter(2)   

###########################################################################################################################
print("\n")
def lumelisa(name):
    print("Lumela " + name)
lumelisa("Amo")


####################################################################################################################################################################
18/11/2021

def square(number):
    """Calculate the square of number."""
    return number ** 2

square(5)


####################################################################################################################################################################
def maximum(a, b, c):
    """Return the maximum of three values."""
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value

####################################################################################################################################################################
def func(a):
    num = int(input("Enter a number: "))
    if num != 0:
        print("You entered a number that's not a zero")
    else:
        print("You hit a zero")
        return num
func(1)

####################################################################################################################################################################
def factorial(number):
    """Return factorial of a number."""
    if number <= 1:
        return 1
    return number * factorial(number - 1) # recursive call
for i in range(11):
    print(f'{i}! = {factorial(i)}')

####################################################################################################################################################################

# Lists and Tuples
a_list = []
for number in range(1, 6):
    a_list +=[number]

####################################################################################################################################################################
numbers = [3, 7, 1, 4, 2, 8, 5, 6]
key = 1000

if key in numbers:
    print(f'found {key} at index {numbers.index(search_key)}')
else:
    print(f'{key} not found')

####################################################################################################################################################################
