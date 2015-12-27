""" Examples of mouse input """

import simplegui
import math

# intialize globals
WIDTH = 450
HEIGHT = 300
ball_pos = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt( (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
# the parameter (position) is a tuple, ie an immutable list
def click(pos):
    global ball_pos, ball_color
    if distance(pos, ball_pos) < BALL_RADIUS:
        ball_color = "Green"
    else:
        ball_pos = list(pos)
        ball_color = "Red"

def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Black", ball_color)

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()


""" Simple task list """

# if x in lst = T/F
# lst.index(python_indexed_nb_for_element)
# lst.append(name_of element)
# lst.pop(python_indexed_nb_for_element)

import simplegui

tasks = []

# Handler for button
def clear():
    global tasks
    tasks = []
    
# Handler for new task
def new(task):
    tasks.append(task)
    
# Handler for remove number
def remove_num(tasknum):
    n = int(tasknum)
    if n > 0 and n <= len(tasks):
        tasks.pop(n-1)

# Handler for remove name
def remove_name(taskname):
    if taskname in tasks:
        tasks.remove(taskname)
        #alternatively: tasks.pop(tasks.index(taskname))
    
# Handler to draw on canvas
def draw(canvas):
    n = 1
    for task in tasks:
        pos = 30 * n
        canvas.draw_text(str(n) + ": " + task, [5, pos], 24, "White")
        n += 1
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Task List", 600, 400)
frame.add_input("New task:", new, 200)
frame.add_input("Remove task number:", remove_num, 200)
frame.add_input("Remove task:", remove_name, 200)
frame.add_button("Clear All", clear)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()



""" Examples of mouse input """

import simplegui
import math

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    ball_list.append(pos)
#    if distance(ball_pos, pos) < ball_radius:
#        if ball_color == "Red":
#            ball_color = "Green"
#    else:
#        ball_pos = [pos[0], pos[1]]
#        ball_color = "Red"

def draw(canvas):
    for ball_pos in ball_list:		# loop - note this "in" is different from the "in" for lists bool
        canvas.draw_circle(ball_pos, ball_radius, 1, "Black", ball_color)
    
    """
    loop:The loop body will execute once for each element of the list y 
    and the loop body will have access to that element as x.
    More examples staring line 234
    """

# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()


""" Examples of mouse input  / first program diff: makes balls clicked twice green """

import simplegui
import math

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    changed = False		#boolean flag to indicate whether or not an event has ocurred
    for ball in ball_list:			
        if distance([ball[0], ball[1]], pos) < ball_radius:
            ball[2] = "Green"
            changed = True

    if not changed:
        ball_list.append([pos[0], pos[1], "Red"])

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "Black", ball[2])
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()



""" Examples of mouse input  / first program diff: removes balls clicked twice"""


import simplegui
import math

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    remove = []					#you need to make a new list of things you want to remove
    for ball in ball_list:		#in a loop you cannot append elements!!
        if distance(ball, pos) < ball_radius:
            remove.append(ball)

#loop

    if remove == []:
        ball_list.append(pos)
    else:
        for ball in remove:
            ball_list.pop(ball_list.index(ball))

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "Black", ball_color)
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()


""" Iterating over lists """
#loop examples

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count

def check_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            return True
    return False

##### The Above example w/loop
def check_odd(numbers):
    odd = False
    for num in numbers:
        if num % 2 == 1:
        		odd = True
    return odd
####################################

def remove_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)


def remove_odd2(numbers):    #doesn't work: hence the odd3 and odd4 functions
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(numbers.index(num))
            
    for idx in remove:
        numbers.pop(idx)
        
def remove_odd3(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)
            
    for num in remove:
        numbers.remove(num)
        
def remove_odd4(numbers):
    newnums = []
    for num in numbers:
        if num % 2 == 0:
            newnums.append(num)
    return newnums
   
""" doesnt work as the remove method removed the first occurrence
 of 7 in the list. The for loop should have iterated over 
 range(len(numbers)) and set last_odd to the position of the last 
 odd number. Using numbers.pop(last_odd) in line 304 would then delete 
 the last odd number."""
def remove_last_odd(numbers): 		
    has_odd = False		#boolean flag
    last_odd = 0
    for num in numbers:
        if num % 2 == 1:
            has_odd = True
            last_odd = num
            
    if has_odd:
        numbers.remove(last_odd)
        

def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    print count_odd(numbers)
    print check_odd(numbers)
    remove_last_odd(numbers)
    print numbers
    
run()


