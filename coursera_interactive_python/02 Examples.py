# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
def increment() :
    global counter 
    counter = counter + 1
    
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,50], 20, "Red")

# Define event handler functions
def tick() :
    increment()
    print counter 

def buttonpress
	global counter
    counter = 0
    
# Create a frame
frame = simplegui.create_frame("SimpleGUI Test", 100, 100)

# Register event handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button("Click me", buttonpress)

# Start frame and timers
frame.start()
timer.start()



# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 36, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()





# global vs local examples

# num1 is a global variable

num1 = 1
print num1

# num2 is a local variable

def fun():
    num1 = 2
    num2 = num1 + 1
    print num2
    
fun()


# the scope of global num1 is the whole program, num 1 remains defined
print num1

# the scope of the variable num2 is fun(), num2 is now undefined
# print num2


# why use local variables?
# give a descriptive name to a quantity
# avoid computing something multiple times

def fahren_to_kelvin(fahren):
    celsius = 5.0 / 9 * (fahren - 32)
    zero_celsius_in_kelvin = 273.15
    return celsius + zero_celsius_in_kelvin

print fahren_to_kelvin(212)





# the risk/reward of using global variables

# risk - consider the software system for an airliner
#		critical piece - flight control system
#		non-critical piece - in-flight entertainment system

# both systems might use a variable called "dial"
# we don't want possibility that change the volume on your audio
# causes the plane's flaps to change!



# example
num = 4

def fun1():
    global num
    num = 5
    
def fun2():
    global num
    num = 6

# note that num changes after each call with no obvious explanation    
print num
fun1()
print num
fun2()
print num

# global variables are an easy way for event handlers
# to communicate game information.

# safer method - but they required more sophisticated
# object-programming techniques



### Calculator with Buttons ###

import simplegui

# intialize globals
store = 12
operand = 3

# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()

def enter(t):
    """ enter a new operand"""
    global operand
    operand = float(t)
    output()

# create frame
f = simplegui.create_frame("Calculator",300,300)

# register event handlers
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("Add", add, 100)
f.add_button("Sub", sub, 100)
f.add_button("Mult", mult, 100)
f.add_button("Div", div, 100)
f.add_input("Enter", enter, 100)

# get frame rolling
f.start()


""" THIS WEEKS PROGRAMMING TIPS """

### Example of missing "global" ###

n1 = 0

def increment():
    n1 = n1 + 1

increment()
increment()
increment()

print n1


#### Example of missing "global" ####

n2 = 0

def assign(x):
    n2 = x

assign(2)
assign(15)
assign(7)

print n2


### Example of missing "return" ####

n3 = 0

def decrement():
    global n3
    n3 = n3 - 1

x = decrement()

print "x = ", x
print "n = ", n


### Example of print debugging ####

import simplegui

x = 0

def f(n):
    print "f: n,x = ", n, x     #added for insight on even_handler of input field
    result = n ** x
    print "f: result = ",result #added for insight on even_handler of input field
    return result
    
def button_handler():
    global x
    print "bh : x = ", x    #added for insight on even_handler of button
    x += 1
    print "bh : x = ", x    #added for insight on even_handler of button

def input_handler(text):
    print "ih : text = ", text
    print f(float(text))
    
frame = simplegui.create_frame("Example", 200, 200)
frame.add_button("Increment", button_handler)
frame.add_input("Number:", input_handler, 100)

frame.start()


### Examples of simplifying conditionals ###

def f1(a, b):
    """Returns True exactly when a is False and b is True."""  
    if a == False and b == True:
        return True
    else:
        return False

def f2(a, b):
    """Returns True exactly when a is False and b is True."""  
    if not a and b:
        return True
    else:
        return False    

def f3(a, b):
    """Returns True exactly when a is False and b is True."""  
    return not a and b

def g1(a, b):
    """Returns False eactly when a and b are both True."""  
    if a == True and b == True:
        return False
    else:
        return True
    
def g2(a, b):
    """Returns False eactly when a and b are both True."""  
    if a and b:
        return False
    else:
        return True

def g3(a, b):
    """Returns False eactly when a and b are both True."""  
    return not (a and b)

print f1(True, False)
print f2(True, False)
print f3(True, False)
print g1(True, False)
print g2(True, False)
print g3(True, False)
