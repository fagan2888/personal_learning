""" Template for 'Stopwatch: The Game' """

import simplegui

# define global variables
t = 0
position_timer = [60, 100]
position_score = [210, 30]
width = 250
height = 200
x = 0
y = 0

# define helper function format that converts time split
# into minutes, seconds and tenths of a second. 
# Formatted string in the form A:BC.D
def format(t):
    A = 0
    B = 0
    C = 0
    D = t
    if t >= 10:
        C = t / 10
        D = t % 10
    elif C >= 10:
        B = C / 10
        C = C % 10
    elif B >= 6:
        A = B / 6
        B = B % 6
    return "0" + str(A) + ":" + str(B) + str(C) + "." + str(D)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def output():
    global t
    t += 1
    return format(t)

def start():
    timer.start()
    output()
    
def stop():
    timer.stop()
    global x
    global y
    if t % 10 == 0:
        x = x + 1
        y = y + 1
    else:
        x
        y = y + 1
    
def reset():
    timer.stop()
    global t
    global x
    global y
    x = 0
    y = 0
    t = 0
    return format(t)

# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, output) 

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), position_timer, 50, "Yellow")
    canvas.draw_text(str(x) + "/" + str(y), position_score, 30, "Orange")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)


#frame.set_draw_handler(draw)
frame.start()
