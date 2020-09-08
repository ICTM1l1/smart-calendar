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

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

week_days_position_y = 0
month_day_y = 1

# End application configurations.


# Functions.

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
    now = datetime.now()
    
    month_weeks = get_month_weeks(now.year, now.month)
    for weeks in month_weeks:        
        for day in weeks:
            if day == 0:
                sense.set_pixel(month_day_x, month_day_y, white)
                month_day_x += 1
                continue
                
            
            if month_day_x != 8:
                sense.set_pixel(month_day_x, month_day_y, green)
                
                month_day_x += 1
                continue
            
        
        # Create new row for displaying the days.
        month_day_y += 1
        month_day_x = 0

# End functions.


# Main Program.

sense.clear(0,0,0)

draw_week_days()
draw_month_days()

# End Main Program.
