# template for "Stopwatch: The Game"
import simplegui

# define global variables
count = 0
proper_stops = 0
total_stops = 0
is_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tens = t % 10
    t = t / 10
    seconds = t % 60
    minutes = t / 60
    b = seconds / 10
    c = seconds % 10
    a = minutes
    d = tens
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
#    pass

# define event handlers for buttons; "Start", "Stop", "Reset"
def reset_handler():
    global count, proper_stops, total_stops
    print count, proper_stops, total_stops
    count = 0
    proper_stops = 0
    total_stops = 0
    timer.stop()

def start_handler():
    global is_running
    is_running = True
    timer.start()

def stop_handler():
    global proper_stops, total_stops, count, is_running
    if is_running == True:
        if count % 10 == 0:
            proper_stops += 1
        total_stops += 1
        is_running = False
        timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(count), (100, 160), 50, "White")
    stops = str(proper_stops) + "/" + str(total_stops)
    canvas.draw_text(stops, (260, 20), 20, "Green")

# create frame
frame = simplegui.create_frame("StopWatch", 300, 300)

# register event handlers
frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)


# start frame
frame.start()

# Please remember to review the grading rubric
