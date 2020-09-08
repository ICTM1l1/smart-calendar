from sense_hat import SenseHat

# Object constructions.

sense = SenseHat()

# End object constructions.


# Application configurations.

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 128, 0)
red = (255, 0, 0)

week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

february_month = 29
even_month = 30
uneven_month = 31

week_days_position_y = 0
month_day_y = 2

# End application configurations.


# Functions.

def get_week_day_color(day):
    switcher = {
        "Sunday": blue,
        "Monday": green,
        "Tuesday": blue,
        "Wednesday": green,
        "Thursday": blue,
        "Friday": green,
        "Saturday": blue
    }
    
    return switcher.get(day, "Invalid day")

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
    for x in range(0, even_month):
        sense.set_pixel(month_day_x, month_day_y, green)
        
        month_day_x += 1
        if (month_day_x == 8):
            month_day_y += 1
            month_day_x = 0

# End functions.


# Main Program.

sense.clear(0,0,0)

draw_week_days()
draw_month_days()

# End Main Program.
