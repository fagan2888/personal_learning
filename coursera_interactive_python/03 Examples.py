# convert xx.yy to xx dollars and yy cents
def convert(val):
    dollars = int(val)
    cents = int(100 * (val - dollars))
    return str(dollars) + " dollars and " + str(cents) + " cents"
    
# Tests
print convert(11.23)
print convert(1.12)
print convert(1.01)
print convert(0.01)
print convert(0)
print convert(-1.40)


### String Processing

# String literals
s1 = "Rixner's funny"
s2 = 'Warren wears nice ties!'
s3 = " t-shirts!"
#print s1, s2
#print s3

# Combining strings
a = ' and '
s4 = "Warren" + a + "Rixner" + ' are nuts!'
print s4

# Characters and slices
print s1[3]
print len(s1)
print s1[0:6] + s2[6:]
print s2[:13] + s1[9:] + s3

# Converting strings
s5 = str(375)
print s5[1:]
i1 = int(s5[1:])
print i1 + 38


# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
    
## Tests
print convert(11.23)
print convert(1.12)
print convert(1.01)
print convert(0.01)
print convert(0)
print convert(-1.40)



# example of drawing operations in simplegui
# standard HMTL color such as "Red" and "Green"
# note later drawing operations overwrite earlier drawing operations

import simplegui


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_circle([90, 200], 20, 10, "White", "White")
    canvas.draw_circle([210, 200], 20, 10, "White", "White")
    canvas.draw_line([50, 180],[250, 180], 40, "Red")
    canvas.draw_line([55, 170],[90, 120], 5, "Red")
    canvas.draw_line([90, 120],[130, 120], 5, "Red")
    canvas.draw_line([180, 108],[180, 160], 140, "Red")
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 300)
frame.set_draw_handler(draw)
frame.set_canvas_background("Yellow")


# Start the frame animation
frame.start()



#circles with radius 20 and white lines of width 10. 
#One is centered at (90,200) and one at (210,200).
#Draw a red line of width 40 from (50,180) to (250,180).
#Draw two red lines of width 5 from (55,170) to (90,120) 
#and from (90,120) to (130,120).
#Draw a red line of width 140 from (180,108) to (180,160).




# Simple "screensaver" program.

# Import modules
import simplegui
import random

# Global state
message = "Python is Fun!"
position = [50, 50]
width = 500
height = 500
interval = 2000

# Handler for text box
def update(text):
    global message
    message = text
    
# Handler for timer
def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")

# Create a frame 
frame = simplegui.create_frame("Home", width, height)

# Register event handlers
text = frame.add_input("Message:", update, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start()
timer.start()


# The Collatz conjecture

# divide by two if the number is even or
# multiply by 3 and add 1 if the number is odd.


import simplegui
import time

n = 217

# helper function
    
def update():
    global n
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n * 3) + 1
    print n

# register timer handlers
timer = simplegui.create_timer(500, update)

# start program
timer.start()
