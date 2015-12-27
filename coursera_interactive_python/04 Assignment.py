"""  Assignement week 4 - Pong """

#http://codeskulptor.appspot.com/save/

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [random.randrange(-5, 5), random.randrange(-5, 5)]
position_score1 = [WIDTH / 2.2, 30]
position_score2 = [WIDTH / 1.9, 30]
paddle1_pos = 0
paddle2_pos = 0
paddle1_vel = 0
paddle2_vel = 0
player_1_score = 0
player_2_score = 0


# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if ball_vel <= 0:
        direction == 'LEFT'
        ball_pos == ball_pos 
        ball_vel == - ball_vel
    elif direction >= 0:
        direction == 'RIGHT'
        ball_pos == ball_pos
        ball_vel == ball_vel


# Define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    if ball_pos[0] <= WIDTH - 1:
        direction = 'LEFT'
    elif ball_pos[0] >= 0:
        direction = 'RIGHT'
    spawn_ball(direction)


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # collide and reflect off of top and bottom
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
    elif ball_pos[1] >= 379:
        vel[1] = - vel[1]
    # collide and run off of canvas right and left (incl. gutter)
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        spawn_ball(RIGHT)
    elif ball_pos[1] <= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS:
        spawn_ball(LEFT)

    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos > HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    elif paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos -= paddle1_vel
    elif paddle2_pos > HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    elif paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos -= paddle2_vel 

    # draw paddles
    canvas.draw_line([PAD_WIDTH + 1, paddle1_pos], [PAD_WIDTH + 1, paddle1_pos + 80], PAD_WIDTH, "Red")
    canvas.draw_line([WIDTH - PAD_WIDTH - 1, paddle2_pos], [WIDTH - PAD_WIDTH - 1, paddle2_pos + 80], PAD_WIDTH, "Blue")

    # draw scores
    canvas.draw_text('p.1', position_score1, 35, "Red")
    canvas.draw_text('p.2', position_score2, 35, "Blue")


def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["down"]:
        paddle1_vel += paddle1_vel
    elif key==simplegui.KEY_MAP["s"]:
        paddle2_vel += paddle2_vel

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["up"]:
        paddle1_vel -= paddle1_vel
    elif key==simplegui.KEY_MAP["w"]:
        paddle2_vel -= paddle2_vel

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
