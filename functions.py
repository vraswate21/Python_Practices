'''def greet():
    print("hello world")

# call the function
greet()

print("outside the function")
'''

'''def greet(name):
    print("hello", name)



#pass argument
greet("john")
'''
'''
# function call with two values
def add_number(num1, num2):
    sum = num1 + num2
    print("sum:", sum)

# function call with two values
add_number(5, 4)
'''
#the return statement
# it return a value from the function using the return statement
#function defination
'''
def find_square(num):
    result = num*num
    return result

#function call 
square = find_square(9)

print("square:",square)
'''
'''
#the pass statement
def future_function():
    pass

# this will execute without any action or error
future_function()
'''
#built-in functions
#print()
#sqrt() returns square root of a number
#pow() retuens power of a number
import math
'''
# sqrt computes the square root
square_root = math.sqrt(4)

print("square root of 4 is", square_root)

#poe() computes the power
power = pow(2, 3)

print("2 to the power 3 is",power)
'''
'''
# function to sum any number of argument
def add_all(*numbers):
    returnsum(numbers)
    
    
# pass any number of arguments
print(add_all(1,2,3,4))'''

# function to printkeyword argument
def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")

# pass any number of keyword arguments
greet(name="john", greeting="hello")

