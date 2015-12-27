""" Objects, classes and their terminology — Object-oriented programming """

class Character:
    #methods (not functions) - as they only operate on objects of the type Character
    #the self parameter is created by Python
    def __init__(self, name, initial_health):
        self.name = names               #self : object - to create fields
        self.health = initial_health
        self.inventory = []
        
    def __str__(self):
        s  = "Name: " + self.name
        s += " Health: " + str(self.health)
        s += " Inventory: " + str(self.inventory)
        return s
    
    #these are behaviours
    def grab(self, item):
        self.inventory.append(item)
        
    def get_health(self):
        return self.health
    
def example():
    me = Character("Bob", 20)
    print str(me)
    me.grab("pencil")
    me.grab("paper")
    print str(me)
    print "Health:", me.get_health()
    
example()
 

# ball physics code for generic 2D domain
# the functions inside() and normal() encode the shape of the ennvironment

import simplegui
import random
import math

# Canvas size
width = 600
height = 400

# Ball traits
radius = 20
color = "White"

# math helper function
def dot(v, w):
    return v[0] * w[0] + v[1] * w[1]

class RectangularDomain:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.border = 2

    # return if bounding circle is inside the domain    
    def inside(self, center, radius):
        in_width = ((radius + self.border) < center[0] < 
                    (self.width - self.border - radius))
        in_height = ((radius + self.border) < center[1] < 
                     (self.height - self.border - radius))
        return in_width and in_height

    # return a unit normal to the domain boundary point nearest center
    def normal(self, center):
        left_dist = center[0]
        right_dist = self.width - center[0]
        top_dist = center[1]
        bottom_dist = self.height - center[1]
        if left_dist < min(right_dist, top_dist, bottom_dist):
            return (1, 0)
        elif right_dist < min(left_dist, top_dist, bottom_dist):
            return (-1, 0)
        elif top_dist < min(bottom_dist, left_dist, right_dist):
            return (0, 1)
        else:
            return (0, -1)

    # return random location
    def random_pos(self, radius):
        x = random.randrange(radius, self.width - radius - self.border)
        y = random.randrange(radius, self.height - radius - self.border)
        return [x, y]

    # Draw boundary of domain
    def draw(self, canvas):
        canvas.draw_polygon([[0, 0], [self.width, 0], 
                             [self.width, self.height], [0, self.height]],
                             self.border*2, "Red")
        
class CircularDomain:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.border = 2
        
    # return if bounding circle is inside the domain    
    def inside(self, center, radius):
        dx = center[0] - self.center[0]
        dy = center[1] - self.center[1]
        dr = math.sqrt(dx ** 2 + dy ** 2)
        return dr < (self.radius - radius - self.border)

    # return a unit normal to the domain boundary point nearest center
    def normal(self, center):
        dx = center[0] - self.center[0]
        dy = center[1] - self.center[1]
        dr = math.sqrt(dx ** 2 + dy ** 2)
        return [dx / dr, dy / dr]
    
    # return random location
    def random_pos(self, radius):
        r = random.random() * (self.radius - radius - self.border)
        theta = random.random() * 2 * math.pi
        x = r * math.cos(theta) + self.center[0]
        y = r * math.sin(theta) + self.center[1]
        return [x, y]
        
    # Draw boundary of domain
    def draw(self, canvas):
        canvas.draw_circle(self.center, self.radius, self.border*2, "Red")
    
class Ball:
    def __init__(self, radius, color, domain):
        self.radius = radius
        self.color = color
        self.domain = domain
        
        self.pos = self.domain.random_pos(self.radius)
        self.vel = [random.random() + .1, random.random() + .1]
        
    # bounce
    def reflect(self):
        norm = self.domain.normal(self.pos)
        norm_length = dot(self.vel, norm)
        self.vel[0] = self.vel[0] - 2 * norm_length * norm[0]
        self.vel[1] = self.vel[1] - 2 * norm_length * norm[1]
    

    # update ball position
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if not self.domain.inside(self.pos, self.radius):
            self.reflect()

    # draw
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 1, 
                           self.color, self.color)
        

# generic update code for ball physics
def draw(canvas):
    ball.update()
    field.draw(canvas)
    ball.draw(canvas)

field = RectangularDomain(width, height)
# field = CircularDomain([width/2, height/2], 180)
ball = Ball(radius, color, field)
        
frame = simplegui.create_frame("Ball physics", width, height)

frame.set_draw_handler(draw)

frame.start()


# Object Oriented Programming
# Class Structure


# Classes

# Classes are defined using the word 'class' instead of 'def'.
#   By convention, their names are in camel case, which means
#   that there are no spaces or underlines, and the first
#   letter of each word is capitalized.

class ClassOne:
    def __init__(self):
        print "You made a ClassOne object!"
 
print "Ex. ClassOne:"
print
c = ClassOne()
# Printing a class lets you know what type of object it is.
print c
print
    
    
# Classes can contain methods. Methods are just functions 
#   inside of a class. They may or may not contain return
#   and/or print statements. The first parameter of every
#   method is the variable 'self', which refers to the 
#   object that is calling the class.

class ClassTwo:
    # This is the special method that initializes the object
    #   that is being created.
    def __init__(self):
        print "HI"
        
    # This method runs whenever an object is printed.
    def __str__(self):
        return "Hello"
        
    def another_method(self):
        print "Good job!"
        
    def adding_method(self, a, b):
        return a + b
    
print "Ex. ClassTwo"
print
c = ClassTwo()
# Notice that when you call methods, you don't explicitly
#   give them the parameter 'self'. 'self' is passed in 
#   by the program as the object calling the method, which
#   in this case is c.
c.another_method()
print c.adding_method(1, 2)
# Here the __str__ method is called by the program.
print c
print
    
# Classes can be used to keep track of variables and perform
#   operations on them. The values of the class' variables
#   are known as its state. To tell the class to keep track
#   of a variable, the first parameter, self, is used. Global
#   statements are not needed to change class variables.
    
class ClassThree:
    # Class variables should be defined and initialized inside
    #   this method.
    def __init__(self, start):
        self.number = start
        
    def __str__(self):
        return str(self.number)
        
    def increment(self):
        # self.number is not a global variable, so there is
        #   no global declaration.
        self.number += 1
        
    def get_number(self):
        return self.number
    
    def set_number(self, n):
        self.number = n

print "Ex. ClassThree:"
print
c = ClassThree(3)
print c.get_number()
c.increment()
c.increment()
print c.get_number()
c.set_number(8)
print c.get_number()
print c
print
        
      
# Classes can also call other methods of the same class.

class ClassFour:
    def __init__(self):
        self.num = 5
     
    def __str__(self):
        return str(self.num)
        
    def add_num(self, n):
        self.num += n
        
    def print_num(self, w):
        print w, self.num
        
    # The parameters for both methods are required.
    def two_in_one(self, w, n):
        # self is used to call the other methods
        self.add_num(n)
        self.print_num(w)
        
c = ClassFour()
c.add_num(2)
c.print_num("One:")
c.two_in_one("Two:", 4)

        
        
  # Object Oriented Programming
# Class Errors


# Here are some errors to look out for while using classes.

# Classes are created using the keyword 'class', not 'def',
#   although they still require the ':' at the end of the 
#   line.

#def ClassOne:
#    def __init__(self):
#        print "You created a ClassOne object."
   
#class X
#    def __init__(self):
#        pass
    
class ClassOne:
    def __init__(self):
        print "You created a ClassOne object."
        
    def p(self):
        print "HI"

print "Ex. 1 (ClassOne):"
c = ClassOne()
c.p()
print


# Instantiating an object of a class is done using the class
#   name and parenthesis only.

print "Ex. 2 (ClassOne):"
c = ClassOne()

#c = new ClassOne()
#c = ClassOne.__init__()
#c = ClassOne.__init__(self)

# Don't forget the parenthesis
c = ClassOne
print "Error:", c
#c.p()
print


# Class and method names must follow the same rules that
#   variable names do.

#class print:   
#class so-this:
#class _9
#class 4th:

class Test:
    def __init__(self):
        pass
    
#    def print(self):
#        print "HI"

#    def a&b(self):
#        print "A"
   
    
# Self always needs to be the first parameter in any method.
#   Uncomment the methods to see the error messages.
        
class Example1:
    def __init__():
        print "HI"
        
#e = Example1()
    
class Example2:
    def __init__(self):
        pass
        
    def add(a, b):
        return a + b
    
    def correct_add(self, a, b):
        return a + b
    
print "Ex. 3 (Example2):"
e = Example2()
#print e.add(4, 5)
# In the next call, the Example object e is being added to 
#   the number 5, which causes the error.
#print e.add(5)
print "Correct Addition:", e.correct_add(4, 5)
print


# Self also does not need to be passed as a parameter when
#   calling methods.

class Example3:
    def __init__(self):
        pass
    
    def f(self):
        print "HI"
        
print "Ex. 4 (Example3):"
e = Example3()
#e.f(self)
#e.f(e)
e.f()
print
        
        
# Forgetting to use 'self' when referencing class variables
#   causes issues similar to forgetting the 'global'
#   statement in functions.
     
class Example4:
    def __init__(self, n):
        num = n
        
    def get_num1(self):
        return num
    
    def get_num2(self):
        return self.num
    
c = Example4(5)
#print c.get_num1()
#print c.get_num2()
    
class Example5:
    def __init__(self, num):
        self.num = num
        
    def get_num(self):
        return num
    
    def actual_get_num(self):
        return self.num
    
    def set_num(self, new):
        num = new
        
    def actual_set_num(self, new):
        self.num = new
  
print "Ex. 5 (Example5):"
e = Example5(3)
#print e.get_num()
print "E num:", e.actual_get_num()
e.set_num(5)
print "Nothing Changed:", e.actual_get_num()
e.actual_set_num(5)
print "Now it did:", e.actual_get_num()
print

# However, using self.something outside of a class doesn't 
#   work.

#print self.num
#print self.get_num()

# To call methods of a class, an object of the class needs
#   to be used.

print "Ex. 6 (Example5):"
#print actual_get_num()
print e.actual_get_num()
#print actual_get_num(e)
print

# You also need to remember the parenthesis

print "Ex. 7 (Example6):"
print "Here it is:"
x = e.actual_get_num
#print x + 2
print e.actual_get_num
print
    
    
print "------------------------"
print
    
# Methods follow the same rules as functions, but the indentation
#   is different.

class B:
    # Forgot the 'def'
#    __init__(self):
#        print "HI"
   
    # Bad indentation
#def __init__(self):
#    print "HI"

    # Missing ':'
#    def __init__(self)
#        print "HI"
        
    # Missing (self)
#    def __init__:
#        print "HI"
     pass
 
    
# Be careful not to give multiple methods the same name.

class C:
    def __init__(self):
        self.num1 = 0
        self.num2 = 2
        
    def get_num(self):
        return self.num1
      
    def get_num(self):
        return self.num2

print "Ex. 8 (C):"
c = C()
print c.get_num()
print c.get_num()
print
        
        
# You can reference global variables inside of your class, 
#   but you need to declare them as such if you plan on
#   modifying them.

my_num = 7

class D:
    def __init__(self):
        self.num = my_num
        
    def add_num(self):
        self.num += 1
    
    def print_num(self):
        print self.num
        
    def bad_add_global(self):
        my_num += 1
        
    def add_global(self, n):
        n += 1
        print "add_global:", n
        
    def good_add_global(self):
        global my_num
        my_num += 1
   
print "Ex. 9 (D):"        
c = D()
c.print_num()
c.add_num()
c.print_num()
print "1:", my_num
#c.bad_add_global()
c.add_global(my_num)
print "2:", my_num
c.good_add_global()
print "3:", my_num
print
        

# When calling one method of a class from a different method
#   of the class, other issues can occur.

class E:
    def __init__(self):
        self.num = 2
    
    def add_num(self, n):
        self.num += n
        
    def print_num(self):
        print self.num
        
    def print_and_add_num_1(self, n):
        self.add_num(n)
        self.print_num()
        
    def print_and_add_num_2(self, n):
        E.add_num(self, n)
        E.print_num(self)
    
    # Forgot to take all of the arguments for the methods
    #   it will be calling.
    def print_and_add_num_3(self):
        self.add_num()
        self.print_num()
    
    # Forgot to include self
    def print_and_add_num_4(self, n):
        add_num(n)
        print_num()
  
print "Ex. 10. (E):"
c = E()
c.print_num()
c.add_num(3)
c.print_num()
c.print_and_add_num_1(6)
c.print_and_add_num_2(-10)
#c.print_and_add_num_3()
#c.print_and_add_num_4(4)
    
    
# One last note: While the following is valid python, if you
#   have never used python or classes before, we highly 
#   recommend that you avoid using this type of variable.
#   They are not necessary for any of the work in this class.

class F:
    # While the following statements do not cause errors, you
    #   should avoid using them.
    num = 9
    my_variable = "HELLO"
    def __init__(self):
        pass
    
c = F()
    

""" Create and working with objects — Object-oriented programming  """

class Character:
    def __init__(self, name, initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []
        
    def __str__(self):
        s  = "Name: " + self.name
        s += " Health: " + str(self.health)
        s += " Inventory: " + str(self.inventory)
        return s
    
    def grab(self, item):
        self.inventory.append(item)
        
    def get_health(self):
        return self.health
    
def example():
    me = Character("Bob", 20)
    print str(me)
    me.grab("pencil")
    me.grab("paper")
    print str(me)
    print "Health:", me.get_health()
    
example()


# Particle class example used to simulate diffusion of molecules

import simplegui
import random

# global constants
WIDTH = 600
HEIGHT = 400
PARTICLE_RADIUS = 5
COLOR_LIST = ["Red", "Green", "Blue", "White"]
DIRECTION_LIST = [[1,0], [0, 1], [-1, 0], [0, -1]]


# definition of Particle class
class Particle:
    
    # initializer for particles
    def __init__(self, position, color):
        self.position = position
        self.color = color
        
    # method that updates position of a particle    
    def move(self, offset):
        self.position[0] += offset[0]
        self.position[1] += offset[1]
        
    # draw method for particles
    def draw(self, canvas):
        canvas.draw_circle(self.position, PARTICLE_RADIUS, 1, self.color, self.color)
    
    # string method for particles
    def __str__(self):
        return "Particle with position = " + str(self.position) + " and color = " + self.color


# draw handler
def draw(canvas):
    for p in particle_list:
        p.move(random.choice(DIRECTION_LIST))
        #remember to call class methods via object_name.method()
    
    for p in particle_list:
        p.draw(canvas)


# create frame and register draw handler
frame = simplegui.create_frame("Particle simulator", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# create a list of particles
particle_list = []
for i in range(100):
    p = Particle([WIDTH / 2, HEIGHT / 2], random.choice(COLOR_LIST))
        #an object is created via class_obj = ClassName()
    particle_list.append(p)

    #print type(p) - to find the data type you've created
    #the first paramater to all class methods is self
    #objects fields are referenced in class methods via self.field_name

# start frame
frame.start()



# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        pass    # create Hand object

    def __str__(self):
        pass    # return a string representation of a hand

    def add_card(self, card):
        pass    # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        pass    # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        pass    # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        pass    # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        pass    # use random.shuffle()

    def deal_card(self):
        pass    # deal a card object from the deck
    
    def __str__(self):
        pass    # return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play

    # your code goes here
    
    in_play = True

def hit():
    pass    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    pass    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric

# Object Oriented Programming
# Flowers


# This program creates instances of the flower class every
#   time the mouse is clicked, which are then put in a list
#   and drawn on the screen.

import simplegui
import random
import math

# Global Variables

width = 600
height = 600
flowers = []
colors = ["aqua", "blue", "fuchsia", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white"]

# Classes

class Flower:
    def __init__(self, pos, radius, color, num_petals, border, angle = 0, angle_vel = 0):
        self.pos = pos
        self.radius = radius
        self.color = color
        self.angle = angle
        self.angle_vel = angle_vel
        self.num_petals = num_petals
        self.border = border
        
    # Causes the flower to rotate 
    def update(self):
        self.angle += self.angle_vel
    
    # Draws a flower using equally spaced circles
    def draw(self, canvas):
        i = 0
        while i < self.num_petals:
            a = (math.pi * 2 / self.num_petals) * i + self.angle
            p = [self.pos[0] + math.cos(a) * self.radius / 3, self.pos[1] + math.sin(a) * self.radius / 3]
            canvas.draw_circle(p, self.radius / 3, 2, self.border, self.color)
            i += 1
        # Draws the center of the flower
        canvas.draw_circle(self.pos, self.radius / 4, 2, "Yellow", "Yellow")

# Helper Functions

def random_color():
    return random.choice(colors)

# Event Handlers

def draw(canvas):
    for f in flowers:
        f.update()
        f.draw(canvas)
       
# Creates a new flower with a random radius (size), color,
#   number of petals, angle, and angular velocity. The 
#   flower's border is white.
def create_flower(pos):
    radius = random.random() * 30 + 20
    num_petals = random.randrange(4, 9)
    angle = random.random() * math.pi
    angular_vel = random.random() * .08 + .01
    flowers.append(Flower(pos, radius, random_color(), num_petals, "White", angle, angular_vel))
    
# Frame

frame = simplegui.create_frame("Flowers :)", width, height)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(create_flower)
frame.set_canvas_background("Lime")

# Start

frame.start()


# Object Oriented Programming
# Bubbles


# This program creates bubbles at random on the bottom of the
#   screen and at clicked locations on the screen. The 
#   bubbles then accelerate toward the top of the screen.

import simplegui
import random
import math

# Global Variables

width = 600
height = 600
bubbles = []

# Classes

class Bubble:
    def __init__(self, pos, radius, color):
        self.pos = list(pos)
        self.radius = radius
        self.color = color
        # Note that the user does not input or influence the
        #   velocity in any way because the __init__ method
        #   does not use a given parameter to initialize it.
        self.vel = [0, 0]
        # The user never inputs the acceleration either.
        #   The initializer calculates it based on the given
        #   radius.
        self.accel = [0, radius ** 3 / radius ** 2 * -0.001]
        
    def update(self):
        self.vel[0] += self.accel[0]
        self.vel[1] += self.accel[1]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
    
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 2, self.color)
    
    # These methods allow the rest of the program to get 
    #   information about the state of the bubble.
    def get_pos(self):
        return self.pos
        
    def get_radius(self):
        return self.radius
        
# Event Handlers

def draw(canvas):
    for b in list(bubbles):
        b.update()
        b.draw(canvas)
        # Removes bubbles if they leave the screen to limit
        #   the number of objects being updated and drawn
        #   (If this is removed, the program gradually slows
        #   down. Feel free to try)
        if b.get_pos()[1] + b.get_radius() < 0:
            bubbles.remove(b)
    generate_bubbles()
        
# Creates a bubble with a random radius at the specified
#   position. Note that this is both the specified mouseclick
#   handler and also called by the generate_bubbles() function.
def create_bubble(pos):
    r = random.random() * 20 + 10
    bubbles.append(Bubble(pos, r, "Aqua"))
  
# Has a chance of creating a bubble at a random position
#   along the bottom of the screen.
def generate_bubbles():
    if random.random() < .07:
        pos = [random.random() * width, height]
        create_bubble(pos)
    
# Frame

frame = simplegui.create_frame("Bubbles :)", width, height)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(create_bubble)
frame.set_canvas_background("Blue")

# Start

frame.start()


# Object Oriented Programming
# Class Errors


# Here are some errors to look out for while using classes.

# Classes are created using the keyword 'class', not 'def',
#   although they still require the ':' at the end of the 
#   line.

#def ClassOne:
#    def __init__(self):
#        print "You created a ClassOne object."
   
#class X
#    def __init__(self):
#        pass
    
class ClassOne:
    def __init__(self):
        print "You created a ClassOne object."
        
    def p(self):
        print "HI"

print "Ex. 1 (ClassOne):"
c = ClassOne()
c.p()
print


# Instantiating an object of a class is done using the class
#   name and parenthesis only.

print "Ex. 2 (ClassOne):"
c = ClassOne()

#c = new ClassOne()
#c = ClassOne.__init__()
#c = ClassOne.__init__(self)

# Don't forget the parenthesis
c = ClassOne
print "Error:", c
#c.p()
print


# Class and method names must follow the same rules that
#   variable names do.

#class print:   
#class so-this:
#class _9
#class 4th:

class Test:
    def __init__(self):
        pass
    
#    def print(self):
#        print "HI"

#    def a&b(self):
#        print "A"
   
    
# Self always needs to be the first parameter in any method.
#   Uncomment the methods to see the error messages.
        
class Example1:
    def __init__():
        print "HI"
        
#e = Example1()
    
class Example2:
    def __init__(self):
        pass
        
    def add(a, b):
        return a + b
    
    def correct_add(self, a, b):
        return a + b
    
print "Ex. 3 (Example2):"
e = Example2()
#print e.add(4, 5)
# In the next call, the Example object e is being added to 
#   the number 5, which causes the error.
#print e.add(5)
print "Correct Addition:", e.correct_add(4, 5)
print


# Self also does not need to be passed as a parameter when
#   calling methods.

class Example3:
    def __init__(self):
        pass
    
    def f(self):
        print "HI"
        
print "Ex. 4 (Example3):"
e = Example3()
#e.f(self)
#e.f(e)
e.f()
print
        
        
# Forgetting to use 'self' when referencing class variables
#   causes issues similar to forgetting the 'global'
#   statement in functions.
     
class Example4:
    def __init__(self, n):
        num = n
        
    def get_num1(self):
        return num
    
    def get_num2(self):
        return self.num
    
c = Example4(5)
#print c.get_num1()
#print c.get_num2()
    
class Example5:
    def __init__(self, num):
        self.num = num
        
    def get_num(self):
        return num
    
    def actual_get_num(self):
        return self.num
    
    def set_num(self, new):
        num = new
        
    def actual_set_num(self, new):
        self.num = new
  
print "Ex. 5 (Example5):"
e = Example5(3)
#print e.get_num()
print "E num:", e.actual_get_num()
e.set_num(5)
print "Nothing Changed:", e.actual_get_num()
e.actual_set_num(5)
print "Now it did:", e.actual_get_num()
print

# However, using self.something outside of a class doesn't 
#   work.

#print self.num
#print self.get_num()

# To call methods of a class, an object of the class needs
#   to be used.

print "Ex. 6 (Example5):"
#print actual_get_num()
print e.actual_get_num()
#print actual_get_num(e)
print

# You also need to remember the parenthesis

print "Ex. 7 (Example6):"
print "Here it is:"
x = e.actual_get_num
#print x + 2
print e.actual_get_num
print
    
    
print "------------------------"
print
    
# Methods follow the same rules as functions, but the indentation
#   is different.

class B:
    # Forgot the 'def'
#    __init__(self):
#        print "HI"
   
    # Bad indentation
#def __init__(self):
#    print "HI"

    # Missing ':'
#    def __init__(self)
#        print "HI"
        
    # Missing (self)
#    def __init__:
#        print "HI"
     pass
 
    
# Be careful not to give multiple methods the same name.

class C:
    def __init__(self):
        self.num1 = 0
        self.num2 = 2
        
    def get_num(self):
        return self.num1
      
    def get_num(self):
        return self.num2

print "Ex. 8 (C):"
c = C()
print c.get_num()
print c.get_num()
print
        
        
# You can reference global variables inside of your class, 
#   but you need to declare them as such if you plan on
#   modifying them.

my_num = 7

class D:
    def __init__(self):
        self.num = my_num
        
    def add_num(self):
        self.num += 1
    
    def print_num(self):
        print self.num
        
    def bad_add_global(self):
        my_num += 1
        
    def add_global(self, n):
        n += 1
        print "add_global:", n
        
    def good_add_global(self):
        global my_num
        my_num += 1
   
print "Ex. 9 (D):"        
c = D()
c.print_num()
c.add_num()
c.print_num()
print "1:", my_num
#c.bad_add_global()
c.add_global(my_num)
print "2:", my_num
c.good_add_global()
print "3:", my_num
print
        

# When calling one method of a class from a different method
#   of the class, other issues can occur.

class E:
    def __init__(self):
        self.num = 2
    
    def add_num(self, n):
        self.num += n
        
    def print_num(self):
        print self.num
        
    def print_and_add_num_1(self, n):
        self.add_num(n)
        self.print_num()
        
    def print_and_add_num_2(self, n):
        E.add_num(self, n)
        E.print_num(self)
    
    # Forgot to take all of the arguments for the methods
    #   it will be calling.
    def print_and_add_num_3(self):
        self.add_num()
        self.print_num()
    
    # Forgot to include self
    def print_and_add_num_4(self, n):
        add_num(n)
        print_num()
  
print "Ex. 10. (E):"
c = E()
c.print_num()
c.add_num(3)
c.print_num()
c.print_and_add_num_1(6)
c.print_and_add_num_2(-10)
#c.print_and_add_num_3()
#c.print_and_add_num_4(4)
    
    
# One last note: While the following is valid python, if you
#   have never used python or classes before, we highly 
#   recommend that you avoid using this type of variable.
#   They are not necessary for any of the work in this class.

class F:
    # While the following statements do not cause errors, you
    #   should avoid using them.
    num = 9
    my_variable = "HELLO"
    def __init__(self):
        pass
    
c = F()
    
    
    
# Object Oriented Programming
# Class Structure


# Classes

# Classes are defined using the word 'class' instead of 'def'.
#   By convention, their names are in camel case, which means
#   that there are no spaces or underlines, and the first
#   letter of each word is capitalized.

class ClassOne:
    def __init__(self):
        print "You made a ClassOne object!"
 
print "Ex. ClassOne:"
print
c = ClassOne()
# Printing a class lets you know what type of object it is.
print c
print
    
    
# Classes can contain methods. Methods are just functions 
#   inside of a class. They may or may not contain return
#   and/or print statements. The first parameter of every
#   method is the variable 'self', which refers to the 
#   object that is calling the class.

class ClassTwo:
    # This is the special method that initializes the object
    #   that is being created.
    def __init__(self):
        print "HI"
        
    # This method runs whenever an object is printed.
    def __str__(self):
        return "Hello"
        
    def another_method(self):
        print "Good job!"
        
    def adding_method(self, a, b):
        return a + b
    
print "Ex. ClassTwo"
print
c = ClassTwo()
# Notice that when you call methods, you don't explicitly
#   give them the parameter 'self'. 'self' is passed in 
#   by the program as the object calling the method, which
#   in this case is c.
c.another_method()
print c.adding_method(1, 2)
# Here the __str__ method is called by the program.
print c
print
    
# Classes can be used to keep track of variables and perform
#   operations on them. The values of the class' variables
#   are known as its state. To tell the class to keep track
#   of a variable, the first parameter, self, is used. Global
#   statements are not needed to change class variables.
    
class ClassThree:
    # Class variables should be defined and initialized inside
    #   this method.
    def __init__(self, start):
        self.number = start
        
    def __str__(self):
        return str(self.number)
        
    def increment(self):
        # self.number is not a global variable, so there is
        #   no global declaration.
        self.number += 1
        
    def get_number(self):
        return self.number
    
    def set_number(self, n):
        self.number = n

print "Ex. ClassThree:"
print
c = ClassThree(3)
print c.get_number()
c.increment()
c.increment()
print c.get_number()
c.set_number(8)
print c.get_number()
print c
print
        
      
# Classes can also call other methods of the same class.

class ClassFour:
    def __init__(self):
        self.num = 5
     
    def __str__(self):
        return str(self.num)
        
    def add_num(self, n):
        self.num += n
        
    def print_num(self, w):
        print w, self.num
        
    # The parameters for both methods are required.
    def two_in_one(self, w, n):
        # self is used to call the other methods
        self.add_num(n)
        self.print_num(w)
        
c = ClassFour()
c.add_num(2)
c.print_num("One:")
c.two_in_one("Two:", 4)

        
 
 """ Tiled images — Tiled images  """

 # demo for drawing using tiled images

import simplegui

# define globals for cards
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
SUITS = ('C', 'S', 'H', 'D')

# card sprite - 950x392
CARD_CENTER = (36.5, 49)
CARD_SIZE = (73, 98)
card_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")



# define card class
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def draw(self, canvas, loc):
        i = RANKS.index(self.rank)
        j = SUITS.index(self.suit)
        card_pos = [CARD_CENTER[0] + i * CARD_SIZE[0],
                    CARD_CENTER[1] + j * CARD_SIZE[1]]
        canvas.draw_image(card_image, card_pos, CARD_SIZE, loc, CARD_SIZE)

# define draw handler        
def draw(canvas):
    one_card.draw(canvas, (155, 90))

# define frame and register draw handler
frame = simplegui.create_frame("Card draw", 300, 200)
frame.set_draw_handler(draw)

# createa card
one_card = Card('S', '6')

frame.start()


# Tiled Images
# Bunny Emotions


# This program draws a bunny and allows the user to pet or
#   poke it, which changes its emotion. The user can also
#   switch the color of the bunny between brown and white.

import simplegui

# Global Variables

canvas_width = 200
canvas_height = 200

# It might be helpful to look at the full image to better
#   understand what is going on.
image_center = (12, 12)
image_size = (24, 24)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/week6-emotions.png")
emotions = ["happy!", "indifferent.", "sad..."]
emotions_index = 1
color = 0

# Event Handlers
        
def draw(canvas):
    # The horizontal tile of the image is determined by the
    #   emotions_index, while the vertical tile of the image
    #   is determined by the color.
    tile_center = [image_center[0] + emotions_index * (image_size[0] + 1), image_center[1] + color * (image_size[1] + 1)]
    canvas.draw_image(image, tile_center, image_size, [canvas_width / 2, canvas_height / 2], [100, 100])
    
def pet():
    global emotions_index
    if emotions_index > 0:
        emotions_index -= 1    
    print "You petted the bunny!"
    print "The bunny is now " + emotions[emotions_index]
    print

def poke():
    global emotions_index
    # Note: len(emotions) should be the same as the number
    #   of tiles per row in the image.
    if emotions_index < len(emotions) - 1:
        emotions_index += 1
    print "You poked the bunny. That wasn't nice."
    print "The bunny is now " + emotions[emotions_index]
    print
        
def switch_color():
    global color
    color = 1 - color
    
# Frame

frame = simplegui.create_frame("Bunny Emotions", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.add_button("Pet", pet, 100)
frame.add_button("Poke", poke, 100)
frame.add_button("Switch Color", switch_color, 100)
frame.set_canvas_background("Green")

# Start
frame.start()        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


