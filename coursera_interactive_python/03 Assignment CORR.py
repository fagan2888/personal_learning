# template for "Stopwatch: The Game"
import simplegui
# define global variables
count = 0
run = False
hit = False
x = 0
y = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D = t % 10
    C = t / 10 % 60 % 10
    B = t / 10 % 60 / 10
    A = t / 10 / 60
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global run
    run = True
    timer.start()
def stop_handler():
    global count, hit, x, y, run
    if run == True:
        if count % 10 == 0:
            hit = True
            x = x + 1
        else:
            hit = False
        y = y + 1
        run = False
    timer.stop()
    
def reset_handler():
    global count, x, y
    count = 0
    x = 0
    y = 0
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count = count + 1
    
timer = simplegui.create_timer(100, timer_handler)

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(count), (150, 100), 25, "Red")
    canvas.draw_text(str(x) + "/" + str(y), (250, 50), 15, "Red")
# create frame
frame = simplegui.create_frame("StopWatch", 300, 200)


# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_handler)
frame.add_button("Stop", stop_handler)
frame.add_button("Reset", reset_handler)

# start frame

frame.start()
# Please remember to review the grading rubric
