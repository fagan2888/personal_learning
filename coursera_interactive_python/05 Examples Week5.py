
""" ---------------------------- 5 A ------------------------------ """


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
# lst.index(python_indexed_nb_for_element) -returns what nb.
# lst.append(name_of element) -returns list without element
# lst.pop(python_indexed_nb_for_element) -returns element and list without element

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

""" Returns random starting points for players in a game """

import random

players = ["mary", "kate", "ashley"]

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        points.append(point)
    return points

print starting_points(players)


""" tells us if a list is ascending """

def is_ascending(numbers):
    """Returns whether the given list of numbers is in ascending order."""
    for i in range(len(numbers) - 1):
        if numbers[i+1] < numbers[i]:
            return False
    return True

print is_ascending([2, 6, 9, 12, 400]) 

""" Fibonacci numbers """

lst = [0, 1]
for i in range(2, 40):
    lst.append(lst[i-1]+lst[i-2])
    print lst 

""" ---------------------------- 5 B ------------------------------ """

""" Dictionary Example: 'Cipher' """

import simplegui

CIPHER = {'a': 'x', 'b': 'c', 'c': 'r', 'd': 'm', 'e': 'l'} #a dictionary

message = ""

# Encode button
def encode():
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]
    print message, "encodes to", emsg

# Decode button
def decode():
    dmsg = ""
    for ch in message:
        for key, value in CIPHER.items():
            if ch == value:
                dmsg += key
    print message, "decodes to", dmsg

# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label("", 200)
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)

# Start the frame animation
frame.start()


""" Images Example """

# Demonstration of a magnifier on a map

import simplegui

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Image dimensions
MAP_WIDTH = 1521
MAP_HEIGHT = 1818

# Scaling factor
SCALE = 3

# Canvas size
CAN_WIDTH = MAP_WIDTH // SCALE
CAN_HEIGHT = MAP_HEIGHT // SCALE

# Size of magnifier pane and initial center
MAG_SIZE = 120
mag_pos = [CAN_WIDTH // 2, CAN_HEIGHT // 2]


# Event handlers
# Move magnifier to clicked position
def click(pos):
    global mag_pos
    mag_pos = list(pos)

# Draw map and magnified region
def draw(canvas):
    # Draw map
    canvas.draw_image(image, 
            [MAP_WIDTH // 2, MAP_HEIGHT // 2], [MAP_WIDTH, MAP_HEIGHT], 
            [CAN_WIDTH // 2, CAN_HEIGHT // 2], [CAN_WIDTH, CAN_HEIGHT])
        'Takes the entire image and draws it onto the canvas in the middle'
    
    # Draw magnifier    
    map_center = [SCALE * mag_pos[0], SCALE * mag_pos[1]]
    map_rectangle = [MAG_SIZE, MAG_SIZE]
    mag_center = mag_pos
    mag_rectangle = [MAG_SIZE, MAG_SIZE]
    canvas.draw_image(image, map_center, map_rectangle, mag_center, mag_rectangle)
    
# Create frame for scaled map
frame = simplegui.create_frame("Map magnifier", CAN_WIDTH, CAN_HEIGHT)

# register even handlers
frame.set_mouseclick_handler(click)    
frame.set_draw_handler(draw)

# Start frame
frame.start()


""" Visualizing Iterations """

# Simple loop example where the elements in a list are squared
def square_list1(numbers):
    """Returns a list of the squares of the numbers in the input."""
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result
# print square_list1([4, 5, -2])

def square_list2(numbers):
    """Returns a list of the squares of the numbers in the input."""
    return [n ** 2 for n in numbers]

print square_list1([4, 5, -2])
print square_list2([4, 5, -2])



def is_in_range(ball):
    """Returns whether the ball is in the desired range.  """
    return ball[0] >= 0 and ball[0] <= 100 and ball[1] >= 0 and ball[1] <= 100


def balls_in_range1(balls):
    """Returns a list of those input balls that are within the desired range."""
    result = []
    for ball in balls:
        if is_in_range(ball):
            result.append(ball)
    return result

def balls_in_range2(balls):
    return [ball for ball in balls if is_in_range(ball)]

print balls_in_range1([[-5,40], [30,20], [70,140], [60,50]])
print balls_in_range2([[-5,40], [30,20], [70,140], [60,50]])


