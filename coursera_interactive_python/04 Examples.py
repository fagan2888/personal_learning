# Keyboard echo

import simplegui

# initialize state
current_key = ' '

# event handlers
def keydown(key):
    global current_key
    current_key = chr(key)
    
def keyup(key):
    global current_key
    current_key = ' '
    
def draw(c):
    # NOTE draw_text now throws an error on some non-printable characters
    # Since keydown event key codes do not all map directly to
    # the printable character via ord(), this example now restricts
    # keys to alphanumerics
    
    if current_key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        c.draw_text(current_key, [10, 25], 20, "Red")    
        
# create frame             
f = simplegui.create_frame("Echo", 35, 35)

# register event handlers
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
f.set_draw_handler(draw)

# start frame
f.start()



# control the position of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]

# define event handlers
def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    vel = 4
    if key == simplegui.KEY_MAP["left"]:
        ball_pos[0] -= vel
    elif key == simplegui.KEY_MAP["right"]:
        ball_pos[0] += vel
    elif key == simplegui.KEY_MAP["down"]:
        ball_pos[1] += vel
    elif key == simplegui.KEY_MAP["up"]:
        ball_pos[1] -= vel        
    
# create frame 
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()


""" Ball motion with an explicit timer """

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

init_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 3]  # pixels per tick
time = 0

# define event handlers
def tick():
    global time
    time = time + 1

def draw(canvas):
    # create a list to hold ball position
    ball_pos = [0, 0]

    # calculate ball position
    ball_pos[0] = init_pos[0] + time * vel[0]
    ball_pos[1] = init_pos[1] + time * vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
timer.start()


""" Ball motion with an implicit timer """

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40 / 60, 5 / 60]
#vel = [0, 1] # pixels per update (1/60 seconds)

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
    elif ball_pos[0] >= 579:
        vel[0] = vel[0]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()



""" Drawing Vectors: Collisions and Reflections """

# This program draws a vector from point_one to point_two,
#   which are given by the user, and displays the magnitude
#   (length) of the vector rounded to two decimal places.

import simplegui
import math

# Global Variables

canvas_width = 400
canvas_height = 400
point_one = [canvas_width // 2, canvas_height // 2]
point_two = [canvas_width // 2, canvas_height // 2]
magnitude = 0
angle = 0

# Helper Functions

def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# This is just for the pretty arrow at the end of the vector,
#   so don't worry about the math
def get_angle(pos1, pos2):
    if pos1[0] == pos2[0]:
        if pos2[1] - pos1[1] > 0:
            return math.pi / 2
        else:
            return math.pi * 3 / 2
    angle = math.atan((pos1[1] - pos2[1]) / (pos1[0] - pos2[0]))
    if pos2[0] - pos1[0] < 0:
        angle += math.pi
    return angle
    
# Event Handlers
        
def draw(canvas):
    canvas.draw_line(point_one, point_two, 1, "White")
    
    # Draws an arrow at the end of the vector. Don't worry
    #   about the math, this is just to make the program 
    #   look nice.
    if magnitude > 0:
        pos = (point_two[0] - 8 * math.cos(angle), point_two[1] - 8 * math.sin(angle))
        a = (math.pi * 2 / 3) * 0 + angle
        p1 = [pos[0] + math.cos(a) * 20 / 3, pos[1] + math.sin(a) * 20 / 3]
        a = (math.pi * 2 / 3) * 1 + angle
        p2 = [pos[0] + math.cos(a) * 20 / 3, pos[1] + math.sin(a) * 20 / 3]
        a = (math.pi * 2 / 3) * 2 + angle
        p3 = [pos[0] + math.cos(a) * 20 / 3, pos[1] + math.sin(a) * 20 / 3]
        canvas.draw_polygon([p1, p2, p3], 1, "White", "White")
    
    canvas.draw_text("Magnitude of Vector: " + str(round(magnitude, 2)), (50, 30), 20, "Red")
    
def update_x1(text):
    # Note that I don't have to list point_one as a global
    global magnitude, angle
    if text.isdigit() and int(text) <= canvas_width:
        point_one[0] = int(text)
        magnitude = distance(point_one, point_two)
        angle = get_angle(point_one, point_two)
    else:
        print "Invalid input"
        
def update_y1(text):
    global magnitude, angle
    if text.isdigit() and int(text) <= canvas_height:
        point_one[1] = int(text)
        magnitude = distance(point_one, point_two)
        angle = get_angle(point_one, point_two)
    else:
        print "Invalid input"
        
def update_x2(text):
    global magnitude, angle
    if text.isdigit() and int(text) <= canvas_width:
        point_two[0] = int(text)
        magnitude = distance(point_one, point_two)
        angle = get_angle(point_one, point_two)
    else:
        print "Invalid input"
        
def update_y2(text):
    global magnitude, angle
    if text.isdigit() and int(text) <= canvas_height:
        point_two[1] = int(text)
        magnitude = distance(point_one, point_two)
        angle = get_angle(point_one, point_two)
    else:
        print "Invalid input"
    
# Frame and Timer

frame = simplegui.create_frame("Drawing Lines", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
# Note that input points must be on the canvas.
frame.add_input("x1", update_x1, 50)
frame.add_input("y1", update_y1, 50)
frame.add_input("x2", update_x2, 50)
frame.add_input("y2", update_y2, 50)

# Start
frame.start()


# control the position of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]

# define event handlers
def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    vel = 4
    if key == simplegui.KEY_MAP["left"]:
        ball_pos[0] -= vel
    elif key == simplegui.KEY_MAP["right"]:
        ball_pos[0] += vel
    elif key == simplegui.KEY_MAP["down"]:
        ball_pos[1] += vel
    elif key == simplegui.KEY_MAP["up"]:
        ball_pos[1] -= vel        
    
# create frame 
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()


""" Above Code with Velocity Controls implemented (rather than position) """

# control the velocity of a ball using the arrow keys
# updates occur in the in the draw handler

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    acc = 1
    if key==simplegui.KEY_MAP["left"]:
        vel[0] -= acc
    elif key==simplegui.KEY_MAP["right"]:
        vel[0] += acc
    elif key==simplegui.KEY_MAP["down"]:
        vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        vel[1] -= acc
        
    print ball_pos
    
# create frame 
frame = simplegui.create_frame("Velocity ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()


""" Visulizing lists and mutations """

# Mutation vs. assignment

################
# Look alike, but different

a = [4, 5, 6]
b = [4, 5, 6]
print "Original a and b:", a, b
print "Are they same thing?", a is b

a[1] = 20
print "New a and b:", a, b

################
# Aliased

c = [4, 5, 6]
d = c
print "Original c and d:", c, d
print "Are they same thing?", c is d

c[1] = 20
print "New c and d:", c, d

################
# Copied

e = [4, 5, 6]
f = list(e)
print "Original e and f:", e, f
print "Are they same thing?", e is f

e[1] = 20
print "New e and f:", e, f

###################################
# Interaction with globals


a = [4, 5, 6]

def mutate_part(x):
    a[1] = x

def assign_whole(x):
    a = x

def assign_whole_global(x):
    global a
    a = x

mutate_part(100)
print a

assign_whole(200)
print a

assign_whole_global(300)
print a
