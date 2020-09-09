from sense_hat import SenseHat
from datetime import datetime
import calendar

# Object constructions.

sense = SenseHat()

# End object constructions.


# Application configurations.

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 128, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
pink = (255, 20, 147)

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

now = datetime.now()
start_year = now.year
start_month = now.month
today = datetime(now.year, now.month, now.day)

week_days_position_y = 0
month_day_y = 1

controller_pos_x = 0
controller_pos_y = 1
previous_pos_x = controller_pos_x
previous_pos_y = controller_pos_y

# End application configurations.


# Functions.

def draw_controller():
    sense.set_pixel(controller_pos_x, controller_pos_y, pink)
    
def move_up(event):
    global controller_pos_y
    if event.action == 'pressed' and controller_pos_y > 0:
        previous_pos_x = controller_pos_x
        previous_pos_y = controller_pos_y
        controller_pos_y -= 1
        sense.set_pixel(previous_pos_x, previous_pos_y, white)
        

def move_down(event):
    global controller_pos_y
    if event.action == 'pressed' and controller_pos_y < 7:
        previous_pos_x = controller_pos_x
        previous_pos_y = controller_pos_y
        controller_pos_y += 1
        sense.set_pixel(previous_pos_x, previous_pos_y, white)

def move_right(event):
    global controller_pos_x
    global previous_pos_x
    global previous_pos_y
    
    if event.action == 'pressed' and controller_pos_x < 7:
        controller_pos_x += 1
        sense.set_pixel(controller_pos_x, controller_pos_y, pink)
       
        # Changes the previous pixel back to his previous color.
        sense.set_pixel(previous_pos_x, previous_pos_y, red)
        
        # Keeps track of the previous position of the cursor.
        if previous_pos_x != controller_pos_x:
            previous_pos_x = controller_pos_x
        
        if previous_pos_y != controller_pos_y:
            previous_pos_y = controller_pos_y
        
def move_left(event):
    global controller_pos_x
    if event.action == 'pressed' and controller_pos_x > 0:
        previous_pos_x = controller_pos_x
        previous_pos_y = controller_pos_y
        controller_pos_x -= 1
        sense.set_pixel(previous_pos_x, previous_pos_y, white)

def get_month_weeks(year, month):
    return calendar.monthcalendar(year, month) 

def get_week_day_color(day):
    switcher = {
        "Monday": orange,
        "Tuesday": blue,
        "Wednesday": orange,
        "Thursday": blue,
        "Friday": orange,
        "Saturday": blue,
        "Sunday": orange,
    }
    
    return switcher.get(day, red)

def draw_week_days():
    global week_days_position_y
    x = 0
    for day in week_days:
        color = get_week_day_color(day)
        sense.set_pixel(x, week_days_position_y, color)
        
        x = x + 1

def draw_month_days():
    global month_day_y
    month_day_x = 0
    
    month_weeks = get_month_weeks(start_year, start_month)
    for weeks in month_weeks:        
        for day in weeks:            
            if day == 0:
                sense.set_pixel(month_day_x, month_day_y, white)
                month_day_x += 1
                continue
                
            if month_day_x == 8:
                continue
            
            # Changes the colors based on the current day.
            current_day = datetime(start_year, start_month, day)
            color = green
            if current_day == today:
                color = yellow
            elif current_day < today:
                color = red
                
            
            sense.set_pixel(month_day_x, month_day_y, color)
            month_day_x += 1
            
        # Create new row for displaying the days.
        month_day_y += 1
        month_day_x = 0

# End functions.


# Main Program.

sense.clear(0,0,0)

draw_week_days()
draw_month_days()

sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
sense.stick.direction_right = move_right
sense.stick.direction_left = move_left

while(True):
    draw_controller()

# End Main Program.
