""" Math Module """

# Python modules - extra functions implemented outside basic Python
import simplegui    # access to drawing operations for interactive applications
import math         # access to standard math functions, e.g; trig
import random       # functions to generate random numbers
# look in Docs for useful functions
print math.pi


# Here are some examples of the functions in the Math Module.
#   For explanations of what they do, please check the
#   documentation. Feel free to change these ones around
#   and try more of them from the module.

print "Ex. 1:", math.ceil(.2), math.ceil(-1.4)
print "Ex. 2:", math.floor(4.9999), math.floor(-3.2)

# Note: math.pow() is the same as the '**' symbol
print "Ex. 3:", math.pow(3, 4), 3 ** 4
print "Ex. 4:", math.fabs(-5), math.fabs(5)
print "Ex. 5:", math.sqrt(9), math.sqrt(2)

# Note: all trig function parameters are in radians
print "Ex. 6:", math.sin(0), math.sin(4.5)
print "Ex. 7:", math.radians(180), math.degrees(3.1415926)
print

# The Math Module also contains important constants
# Note: Because they are constants, they do not require ()'s
print "Pi:", math.pi
print "e:", math.e

# Pythagorean Theorem (finding the hypotenuse of a right triangle)

def pythagorean(a, b):
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    return c

print "Pythagorean Theorem:", pythagorean(3, 4)

# Radioactive decay (approximation)

def radioactive_decay(initial_amount, half_life, time_elapsed):
    x = -0.693 * time_elapsed / half_life
    amount = initial_amount * math.exp(x)
    return amount

print "Radioactive Decay:", radioactive_decay(100, 17.9, 10)


# Remainder - modular arithmetic

# systematically restrict computation to a range
# long division - divide by a number, we get a quotient plus a remainder
# quotient is integer division //, the remainder is % (Docs)


# problem - get the ones digit of a number
num = 49
tens = num // 10
ones = num % 10
print tens, ones
print 10 * tens + ones, num

# application - 24 hour clock
# http://en.wikipedia.org/wiki/24-hour_clock

hour = 20
shift = 8
print (hour + shift) % 24


# application - screen wraparound
# Spaceship from week seven
width = 800
position = 797
move = 5
position = (position + move) % width
print position


# Data conversion operations

# convert an integer into string - str
# convert an hour into 24-hour format "03:00", always print leading zero

hour = 3
ones = hour % 10
tens = hour // 10
print tens, ones, ":00"
print str(tens), str(ones), ":00"
print str(tens) + str(ones) + ":00"
# convert a string into numbers using int and float


""" Conversion Function """

# Functions - take an input(s) and return an output
# Structure


# Functions have two parts: a header and a body. The header
#   of a function is made up of the keyword 'def' followed by
#   the function name, parameters in parenthesis, and a colon.
#   The body is indented 4 spaces after the header.

def function_name(parameters):
    print "This is the body!!!"
    
# Functions can have 0 or more parameters.

def no_parameters():
    print "The parenthesis were empty this time!!!"
    
def more_parameters(a, b, c):
    print "There are three parameters now!!!"

# Functions can have multiple lines in the body as well.
    
def more_lines():
    print "This function is longer."
    print "It has multiple lines."
    print "Three, to be exact."
    
  
# If you try to run the program, you will see that nothing
#   is printed to the screen. The lines inside the body of
#   a function are not used by the computer until the
#   function is called.

# These are function calls. Try them out by uncommenting them.
#no_parameters()
#more_lines()

# If there are parameters in the method header, the call
#   must also have parameters in the parenthesis.
#function_name(1)
#more_parameters(1, 2, 3)


# The word 'pass' can be used in the body of a function to
#   cause the function to do nothing. This can be useful
#   when you know you will need a function, but are not 
#   quite sure how you want it to work.

def pointless_function():
    pass

pointless_function()

# Another special word is 'return'. If you place the word
#   'return' followed by some value, the function will
#   return that value. Nothing after the return statement
#   is executed.

def returning_function():
    print "Ex. 1: First"
    return 4
    print "Second"

# Uncomment these to try it for yourself.
#x = returning_function()
#print "Ex. 2:", x

# Function names have the same limitations as variable
#   names. As a reminder: valid names consist of 
#   letters, numbers, and / or underscores (_), 
#   and start with a letter or underscore. They should also
#   be descriptive, and not change color.

# Good names
def add_two(x):
    pass
def print_strings(s_one, s_two, s_three):
    pass
def multiply_by_4(x):
    pass

# Bad names (commented ones produce errors)
def a_t(x):
    pass
def prstr(o, t, th):
    pass
def m4(x):
    pass
def i_hate_comp_sci():
    pass
#def -a(a):
#    pass
#def x&y(x, y):
#    pass
#def 4ever():
#    pass
#def print(x):
#    pass
#def True(x):
#    pass

# These two re-define pre-existing functions, which is not
#   a very good idea. Don't do it, please. 
def max(x, y):
    pass
def int(x):
    pass
 






# computes the area of a triangle
def triangle_area(base, height):     # header - ends in colon
    area = (1.0 / 2) * base * height # body - all of body is indented
    return area                      # body - return outputs value

a1 = triangle_area(3, 8)
print a1
a2 = triangle_area(14, 2)
print a2

# converts fahrenheit to celsius
def fahrenheit2celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius

# test!!!
c1 = fahrenheit2celsius(32)
c2 = fahrenheit2celsius(212)
print c1, c2

# converts fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

# test!!!
k1 = fahrenheit2kelvin(32)
k2 = fahrenheit2kelvin(212)
print k1, k2

# prints hello, world!
def hello():
    print "Hello, world!"

# test!!!
hello()      # call to hello prints "Hello, world!"
h = hello()  # call to hello prints "Hello, world!" a second time
print h      # prints None since there was no return value



""" Conditional """

def greet(friend, money):
    if friend and (money > 20):
        print "Hi!"
        money = money - 20
    elif friend:
        print "Hello"
    else:
        print "Ha ha"
        money = money + 10
    return money



""" Logic and Comparisons """
# Expressions


# The comparison operations can be used at the same time as
#   the logic operations. The comparison operations are after
#   'not,' but before 'and' in the order of operations. 

a = True
b = False
x = 4
y = 6

print "Ex. 1:", a or b == False
print "Ex. 2:", (a or b) == False
print "Ex. 3:", x < y or x > 2
print "Ex. 4:", x == y and x > 0
print "Ex. 5:", x != y and x > 7
print "Ex. 6:", not b and x > 1



""" Logic and Comparisons """
# Examples


# Utilizing if-elif-else statements greatly expands the types
#   of functions you can make. Note that the test cases try
#   to test all of the different possibilities.

# Absolute value

def absolute_value(num):
    if num < 0:
        num = num * -1
    return num

print "Absolute Value:", absolute_value(9)
print "Absolute Value:", absolute_value(-4)
print "Absolute Value:", absolute_value(0)
print

# Number of real solutions to a quadratic equation

def num_solutions(discriminant):
    if discriminant > 0:
        return 2
    elif discriminant < 0:
        return 0
    else:
        return 1
    
print "Number of Solutions:", num_solutions(1)
print "Number of Solutions:", num_solutions(-1)
print "Number of Solutions:", num_solutions(0)
print

# Prints the type of triangle given the largest angle 
#   measurement in degrees

def print_triangle_type(degrees):
    if degrees > 90 and degrees < 180:
        print "Triangle is obtuse!"
    elif degrees == 90:
        print "Triangle is right!"
    elif degrees < 90 and degrees > 0:
        print "Triangle is acute!"
    else:
        print "Triangle does not exist!"
        
print_triangle_type(137)
print_triangle_type(90)
print_triangle_type(54)
print_triangle_type(-1)
print_triangle_type(180)

# Returns True if a triangle can be made with the given 
#   side lengths, False otherwise.
#   (if the two smallest sides add up to be greater than
#    the largest one)

def is_triangle(side_1, side_2, side_3):
    max_side = max(side_1, side_2, side_3)
    if max_side == side_1:
        return (side_2 + side_3) > side_1
    elif max_side == side_2:
        return (side_1 + side_3) > side_2
    else:
        return (side_1 + side_2) > side_3

print "Triangle:", is_triangle(3, 4, 5)
print "Triangle:", is_triangle(5, 3, 4)
print "Triangle:", is_triangle(4, 5, 3)
print "Triangle:", is_triangle(1, 1, 2)
print "Triangle:", is_triangle(5, 6, 19)

