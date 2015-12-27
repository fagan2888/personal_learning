# Friction
# Curling


# This program demonstrates the use of friction through
#	a simple reflex videogame similar to curling. The user 
#	presses the spacebar to release the ball with an initial
#	velocity in an attempt to have it land on the target.
# The code using friction can be found in the update method
#	of the Ball class.

import simplegui
import math

# Global Variables

canvas_width = 800
canvas_height = 500
target_center = [600, 250]
started = False
# Contains the last five scores
last_five = [0, 0, 0, 0, 0]
starting_vel = 0

# Classes
 
class Ball:
    def __init__(self, radius, start, color, friction):
        self.radius = radius
        self.start = start
        self.pos = list(start)
        self.vel = [0, 0]
        self.friction = friction
        self.color = color
        
    def __str__(self):
        a = "BALL" + "\n"
        a += "Radius: " + str(self.radius) + "\n"
        a += "Starting Position: " + str(self.start) + "\n"
        a += "Position: " + str(self.pos) + "\n"
        a += "Velocity: " + str(self.vel) + "\n"
        a += "Friction: " + str(self.friction) + "\n"
        a += "Color: " + str(self.color) + "\n"
        return a
        
    # The draw method does not perform any calculations; it
    #	only draws the object.
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 2, "Black", self.color)
     
    # The update method is in charge of updating the state
    #	of the object, including its position and velocity.
    # This update method uses friction to slow the object.
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        # Updates the velocity using friction.
        self.vel[0] *= self.friction
        self.vel[1] *= self.friction
     
    # get_pos and get_vel are accessor methods that return
    #	information about the object.
    def get_pos(self):
        return self.pos
        
    def get_vel(self):
        return self.vel
        
    # set_vel is a mutator method used to change the state
    #	of the object.
    def set_vel(self, vel):
        self.vel = vel
        
    def reset(self):
        self.pos = list(self.start)
        self.vel = [0, 0]
        
class Target:
    def __init__(self, num_rings, radius, colors, center):
        self.num_rings = num_rings
        # Initializes the radii from smallest to largest
        self.radii = []
        for i in range(num_rings):
            self.radii.append((i + 1) * radius / num_rings)
        self.colors = colors
        self.center = center
    
    def __str__(self):
        a = "TARGET" + "\n"
        a += "Number of Rings: " + str(self.num_rings) + "\n"
        a += "Radii: " + str(self.radii) + "\n"
        a += "Colors: " + str(self.colors) + "\n"
        a += "Center: " + str(self.center) + "\n"
        return a
    
    def draw(self, canvas):
        for i in range(self.num_rings):
            # The radii are listed from smallest to largest, but 
            #	the circles must be drawn from largest to smallest
            #	if all of them are to be visible.
            index = self.num_rings - i - 1
            canvas.draw_circle(self.center, self.radii[index], 2, "Black", self.colors[index])
     
    def get_score(self, pos):
        for r in self.radii:
            if self.distance(pos) < r:
                return (self.num_rings - self.radii.index(r)) * 10
        return 0
            
    def distance(self, point):
        return math.sqrt((point[0] - self.center[0]) ** 2 + (point[1] - self.center[1]) ** 2)
    
# Creating Class Instances

target = Target(3, 100, ["Red", "Yellow", "Blue"], [675, 250])
ball = Ball(25, [100, 250], "Black", .97)

# Event Handlers
        
def draw(canvas):
    global started, starting_vel
    
    # Displays the scores on the screen and calculates the total
    score_text = "Last five scores: "
    total = 0
    for s in last_five:
        score_text += str(s) + " "
        total += s
    score_text += " Total: " + str(total)
    canvas.draw_text(score_text, [50, 75], 30, "White")
    
    # Draws the velocity bar
    canvas.draw_polygon([(50, 400), (50, 425), (50 + starting_vel * 10, 425), (50 + starting_vel * 10, 400)], 2, "Black", "Aqua")
    
    target.draw(canvas)
    
    # If the update method is not called, the ball will not move.
    #	You can comment the line out to see for yourself.
    ball.update()
    # If the draw method is commented out instead, the game functions
    #	as expected, but the ball is not visible.
    ball.draw(canvas)
    
    if started:
        if ball.get_vel()[0] < .01:
            # Checks the position of the center of the ball and updates the score
            last_five.append(target.get_score(ball.get_pos()))
            last_five.pop(0)
            ball.reset()
            starting_vel = 0
            started = False
    else:
        starting_vel += .2

def reset():
    global last_five
    ball.reset()
    last_five = [0, 0, 0, 0, 0]
    
def keydown_handler(key):
    global started
    if key == simplegui.KEY_MAP['space'] and not started:
        ball.set_vel([starting_vel, 0])
        started = True
    
# Frame and Timer

frame = simplegui.create_frame("Curling", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_canvas_background("Green")
frame.add_button("Reset", reset)
frame.add_label("Push the space bar to send the ball flying!")

# Start
frame.start()


# Acceleration
# Balancing


# This program demonstrates angular acceleration by asking
#   the user to attempt to balance a stick using the arrow keys.
# The code using acceleration can be found in the update method
#   of the Stick class.

import simplegui
import math
import random

# Global Variables

canvas_width = 400
canvas_height = 400
# Note that the center of the image is located at the black
#   circle at the base of the stick.
stick_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/week7-stick.png")

# Classes

class Stick:
    def __init__(self, radius, center, image, image_center, image_size):
        self.radius = radius
        self.center = center
        self.angle = random.random() * random.choice([-1, 1]) * .01
        self.angle_vel = 0
        self.angle_acc = 0
        self.key_acc = 0
        self.image = image
        self.image_center = image_center
        self.image_size = image_size
        
    # Draws the image. Does not perform any calculations.
    def draw(self, canvas):
        scale = 2
        canvas.draw_image(self.image, self.image_center, self.image_size, self.center, [self.image_size[0] * scale, self.image_size[1] * scale], self.angle)
     
    # Updates the state of the object using self.angle_vel
    #   and self.angle_acc. The value of self.angle_acc 
    #   depends on whether or not the user is holding
    #   down an arrow key.
    def update(self):
        self.angle += self.angle_vel
        # Checks to see if the stick fell down too far
        #   (if this is not checked, self.get_gravity() 
        #   may return an error)
        if self.angle <= - math.pi / 4 or self.angle >= math.pi / 4:
            self.reset()
            
        # Updates the angle_vel using the acceleration.
        self.angle_vel += self.angle_acc
        self.angle_acc = self.get_gravity() + self.key_acc
        
    # Used to calculate the acceleration due to gravity
    #   of the stick. You don't need to worry about this
    #   for the project or this class.
    def get_gravity(self):
        if self.angle == 0:
            return 0
        else:
            return math.sin(self.angle) * .001
        
    # Used to change the acceleration due to the user
    def set_key_acc(self, a):
        self.key_acc = a
        
    def reset(self):
        self.angle = random.random() * random.choice([-1, 1]) * .1
        self.angle_vel = 0
        self.angle_acc = 0
        self.key_acc = 0
    
# Creating Class Instances

stick = Stick(50, [canvas_width // 2, canvas_height // 2], stick_image, [50, 50], [101, 101])

# Event Handlers
        
# Note that this draw function must draw the stick in addition
#   to telling it to update itself.
def draw(canvas):
    stick.update()
    stick.draw(canvas)
    canvas.draw_line((0, canvas_height // 2), (canvas_width, canvas_height // 2), 3, "Black")

def reset():
    stick.reset()
    
# Sets the key_acc of the stick depending on 
#   the keys pressed.
def keydown_handler(key):
    acc = .001
    if key == simplegui.KEY_MAP['left']:
        stick.set_key_acc(-acc)
    elif key == simplegui.KEY_MAP['right']:
        stick.set_key_acc(acc)
        
def keyup_handler(key):
    stick.set_key_acc(0)
    
# Frame and Timer

frame = simplegui.create_frame("Balance", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.set_canvas_background("Green")
frame.add_button("Reset", reset)
frame.add_label("Use the left and right arrow keys to balance the stick!")

# Start
frame.start()


# Vectors
# Angle Vectors


# This program draws a vector when given an angle.

import simplegui
import math
import random

# Global Variables

canvas_width = 400
canvas_height = 400
angle = 0      
length = 150
    
# Helper Functions

# This returns the x and y components
#   of a vector. When added to the origin
#   of the vector, the result is the other
#   endpoint of the vector.
def get_vector():
    x = math.cos(angle) * length
    y = math.sin(angle) * length
    return [x, y]

def print_angle():
    print "Angle in Radians: " + str(angle)
    # Note that the math module has a function that
    #   converts radians to degrees.
    print "Angle in Degrees: " + str(math.degrees(angle))
    print

# Event Handlers
        
def draw(canvas):
    canvas.draw_text("Angle: " + str(angle), [10, 25], 25, "White")
    
    # Draws the axis
    center = [canvas_width // 2, canvas_height // 2]
    canvas.draw_line((0, center[1]), (canvas_width, center[1]), 3, "White")
    canvas.draw_line((center[0], 0), (center[0], canvas_height), 3, "White")
    
    # Gets that magnitude of the x and y
    #   components of the vector.
    v = get_vector()
    canvas.draw_line((center[0], center[1]), (center[0] + v[0], center[1] + v[1]), 5, "Red")
    
def set_r_angle(text):
    global angle
    angle = float(text)
    print_angle()
    
def set_d_angle(text):
    global angle
    # Note that the math module has a function that
    #   converts degrees to radians.
    angle = math.radians(float(text))
    print_angle()
    
# Frame and Timer

frame = simplegui.create_frame("Vectors", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.add_input("Angle (in radians)", set_r_angle, 100)
frame.add_input("Angle (in degrees)", set_d_angle, 100)

# Start
frame.start()

# Sprite class emo
import simplegui
import math

# helper class to organize image information
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

# load ship image
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")


# Sprite class
class Sprite():
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

           
def draw(canvas):

    # draw ship and sprites
    a_rock.draw(canvas)
    
    # update ship and sprites
    a_rock.update()
                
# initialize frame
frame = simplegui.create_frame("Sprite demo", 800, 600)

# initialize ship and two sprites
a_rock = Sprite([400, 300], [0.3, 0.4], 0, 0.1, asteroid_image, asteroid_info)

# register handlers
frame.set_draw_handler(draw)

# get things rolling
frame.start()

# Partial example code for Spaceship

import simplegui


class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# sound assets purchased from sounddogs.com, please do not redistribute
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        pass
    
# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        pass
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
    
    def update(self):
        pass        

           
def draw(canvas):
    global time
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
            
# timer handler that spawns a rock    
def rock_spawner():
    pass
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()


# Friction
# Curling


# This program demonstrates the use of friction through
#   a simple reflex videogame similar to curling. The user 
#   presses the spacebar to release the ball with an initial
#   velocity in an attempt to have it land on the target.
# The code using friction can be found in the update method
#   of the Ball class.

import simplegui
import math

# Global Variables

canvas_width = 800
canvas_height = 500
target_center = [600, 250]
started = False
# Contains the last five scores
last_five = [0, 0, 0, 0, 0]
starting_vel = 0

# Classes
 
class Ball:
    def __init__(self, radius, start, color, friction):
        self.radius = radius
        self.start = start
        self.pos = list(start)
        self.vel = [0, 0]
        self.friction = friction
        self.color = color
        
    def __str__(self):
        a = "BALL" + "\n"
        a += "Radius: " + str(self.radius) + "\n"
        a += "Starting Position: " + str(self.start) + "\n"
        a += "Position: " + str(self.pos) + "\n"
        a += "Velocity: " + str(self.vel) + "\n"
        a += "Friction: " + str(self.friction) + "\n"
        a += "Color: " + str(self.color) + "\n"
        return a
        
    # The draw method does not perform any calculations; it
    #   only draws the object.
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 2, "Black", self.color)
     
    # The update method is in charge of updating the state
    #   of the object, including its position and velocity.
    # This update method uses friction to slow the object.
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        # Updates the velocity using friction.
        self.vel[0] *= self.friction
        self.vel[1] *= self.friction
     
    # get_pos and get_vel are accessor methods that return
    #   information about the object.
    def get_pos(self):
        return self.pos
        
    def get_vel(self):
        return self.vel
        
    # set_vel is a mutator method used to change the state
    #   of the object.
    def set_vel(self, vel):
        self.vel = vel
        
    def reset(self):
        self.pos = list(self.start)
        self.vel = [0, 0]
        
class Target:
    def __init__(self, num_rings, radius, colors, center):
        self.num_rings = num_rings
        # Initializes the radii from smallest to largest
        self.radii = []
        for i in range(num_rings):
            self.radii.append((i + 1) * radius / num_rings)
        self.colors = colors
        self.center = center
    
    def __str__(self):
        a = "TARGET" + "\n"
        a += "Number of Rings: " + str(self.num_rings) + "\n"
        a += "Radii: " + str(self.radii) + "\n"
        a += "Colors: " + str(self.colors) + "\n"
        a += "Center: " + str(self.center) + "\n"
        return a
    
    def draw(self, canvas):
        for i in range(self.num_rings):
            # The radii are listed from smallest to largest, but 
            #   the circles must be drawn from largest to smallest
            #   if all of them are to be visible.
            index = self.num_rings - i - 1
            canvas.draw_circle(self.center, self.radii[index], 2, "Black", self.colors[index])
     
    def get_score(self, pos):
        for r in self.radii:
            if self.distance(pos) < r:
                return (self.num_rings - self.radii.index(r)) * 10
        return 0
            
    def distance(self, point):
        return math.sqrt((point[0] - self.center[0]) ** 2 + (point[1] - self.center[1]) ** 2)
    
# Creating Class Instances

target = Target(3, 100, ["Red", "Yellow", "Blue"], [675, 250])
ball = Ball(25, [100, 250], "Black", .97)

# Event Handlers
        
def draw(canvas):
    global started, starting_vel
    
    # Displays the scores on the screen and calculates the total
    score_text = "Last five scores: "
    total = 0
    for s in last_five:
        score_text += str(s) + " "
        total += s
    score_text += " Total: " + str(total)
    canvas.draw_text(score_text, [50, 75], 30, "White")
    
    # Draws the velocity bar
    canvas.draw_polygon([(50, 400), (50, 425), (50 + starting_vel * 10, 425), (50 + starting_vel * 10, 400)], 2, "Black", "Aqua")
    
    target.draw(canvas)
    
    # If the update method is not called, the ball will not move.
    #   You can comment the line out to see for yourself.
    ball.update()
    # If the draw method is commented out instead, the game functions
    #   as expected, but the ball is not visible.
    ball.draw(canvas)
    
    if started:
        if ball.get_vel()[0] < .01:
            # Checks the position of the center of the ball and updates the score
            last_five.append(target.get_score(ball.get_pos()))
            last_five.pop(0)
            ball.reset()
            starting_vel = 0
            started = False
    else:
        starting_vel += .2

def reset():
    global last_five
    ball.reset()
    last_five = [0, 0, 0, 0, 0]
    
def keydown_handler(key):
    global started
    if key == simplegui.KEY_MAP['space'] and not started:
        ball.set_vel([starting_vel, 0])
        started = True
    
# Frame and Timer

frame = simplegui.create_frame("Curling", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_canvas_background("Green")
frame.add_button("Reset", reset)
frame.add_label("Push the space bar to send the ball flying!")

# Start
frame.start()

# Colors
# Fading Dots


# This program draws randomly colored fading dots that are
#   placed by the mouse clicks of the user.  

import simplegui
import random

# Global Variables

canvas_width = 300
canvas_height = 300
dots = []


# Classes for colors and dots


class RGBcolor:
    
    # create color with specified intensities
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    # make HTML color string
    def make_html(self):
        return "rgb(" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ")"
    
    # print out readable representation
    def __str__(self):
        return "Red: " + str(self.red) + ", Green: " + str(self.green) + ", Blue: " + str(self.blue)
    
    # brighten towards white
    def brighten(self):
        self.red += 1
        self.green += 1
        self.blue += 1
        
class Dot:
    def __init__(self, pos, color, radius, lifespan):
        self.pos = pos
        self.color = color
        self.radius = radius
        # Without lifespan, the number of dots would increase
        #   indefinitely, causing the program to slow down.
        self.life = lifespan
        
    def draw(self, canvas):
        color_string = self.color.make_html()
        canvas.draw_circle(self.pos, self.radius, 1, color_string, color_string)
        
    # Updates the life and causes the color to fade to white.
    def update(self):
        self.life -= 1
        self.color.brighten()
        
    def get_life(self):
        return self.life


# Event Handlers
        
def draw(canvas):
    # Iterate over list(dots) instead of dots, to make a copy.
    # This allows you to safely remove from dots inside the loop.
    for d in list(dots):
        d.update()
        d.draw(canvas)

        # Remove dot if it's too old
        if d.life <= 0:
            dots.remove(d)
 
def click(pos):
    new_color = RGBcolor(random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))
    print new_color
    print "HTML color is " + new_color.make_html()
    print
    dots.append(Dot(pos, new_color, 20, 256))
    
# Frame

frame = simplegui.create_frame("Fading Dots", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_canvas_background("White")

# Start
frame.start()

# simple music player, uses buttons and sounds
# note that .ogg sounds are not supported in Safari

import simplegui
    
# define callbacks
def play():
    """play some music, starts at last paused spot"""
    music.play()

def pause():
    """pause the music"""
    music.pause()
    
def rewind():
    """rewind the music to the beginning """
    music.rewind()
    
def laugh():
    """play an evil laugh
    will overlap since it is separate sound object"""
    laugh.play()
    
def vol_down():
    """turn the current volume down"""
    global vol
    if vol > 0:
        vol = vol - 1
    music.set_volume(vol / 10.0)
    volume_button.set_text("Volume = " + str(vol))
    
def vol_up():
    """turn the current volume up"""
    global vol
    if vol < 10:
        vol = vol + 1
    music.set_volume(vol / 10.0)
    volume_button.set_text("Volume = " + str(vol))


# create frame - canvas will be blank
frame = simplegui.create_frame("Music demo", 250, 250, 100)

# set up control elements 
frame.add_button("play", play,100)
frame.add_button("pause", pause,100)
frame.add_button("rewind",rewind,100)
frame.add_button("laugh",laugh,100)
frame.add_button("Vol down", vol_down,100)
frame.add_button("Vol up", vol_up,100)

# initialize volume, create button whose label will display the volume
vol = 7
volume_button = frame.add_label("Volume = " + str(vol))


# load some sounds
music = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")
laugh = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Evillaugh.ogg")

# make the laugh quieter so my ears don't bleed
laugh.set_volume(.1)

frame.start()

# Sound
# Bouncing Sounds


# This program draws a ball that makes sounds when it bounces
#   off the side of the canvas.

import simplegui
import math
import random

# Global Variables

canvas_width = 400
canvas_height = 400

sound_a = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/week7-bounce.m4a")
sound_b = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/week7-brrring.m4a")
sound_c = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/week7-button.m4a")

sounds = [sound_a, sound_b, sound_c]
sound_index = 0

# Classes
 
class Ball:
    def __init__(self, radius, color, bounds, sound):
        self.radius = radius
        self.pos = [bounds[0] // 2, bounds[1] // 2]
        self.vel = self.get_random_vel()
        self.color = color
        self.bounds = bounds
        self.sound = sound
        
    # Draws the ball. Does not perform calculations 
    #   or checks.
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 2, "White", self.color)
     
    # Updates the position of the ball. If the ball goes
    #   out of bounds, its velocity is reversed and its
    #   current sound is rewound and played.
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # Collision check and logic
        if self.pos[0] - self.radius < 0 or self.pos[0] + self.radius > self.bounds[0]:
            self.vel[0] = self.vel[0] * -1
            # Rewinds and plays the sound.
            self.sound.rewind()
            self.sound.play()
        if self.pos[1] - self.radius < 0 or self.pos[1] + self.radius > self.bounds[1]:
            self.vel[1] = self.vel[1] * -1
            # Rewinds and plays the sound.
            self.sound.rewind()
            self.sound.play()
        
    def get_random_vel(self):
        magnitude = random.random() * 3 + 2
        angle = random.random() * (math.pi * 2)
        return [magnitude * math.cos(angle), magnitude * math.sin(angle)]
        
    # Sets the sound that the ball uses
    def set_sound(self, s):
        self.sound = s
        
    def reset(self):
        self.pos = [self.bounds[0] // 2, self.bounds[1] // 2]
        self.vel = self.get_random_vel()
    
# Creating Class Instances

ball = Ball(25, "Red", [canvas_width, canvas_height], sounds[sound_index])

# Helper Functions

# Re-assigns the ball's sound based on the
#   new sound_index
def change_sound(sign):
    global sound_index
    sound_index = (sound_index + sign) % len(sounds)
    ball.set_sound(sounds[sound_index])

# Event Handlers
        
def draw(canvas):
    ball.update()
    ball.draw(canvas)
    
def keydown_handler(key):
    if key == simplegui.KEY_MAP["left"]:
        change_sound(-1)
    elif key == simplegui.KEY_MAP["right"]:
        change_sound(1)

def reset():
    ball.reset()
    
# Frame and Timer

frame = simplegui.create_frame("Bouncing Sounds", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.add_button("Reset", reset)
frame.add_label("Use the left and right arrow keys to change the sound!")

# Start
frame.start()