from sense_hat import SenseHat

# Object constructions.

sense = SenseHat()

# End object constructions.


# Application configurations.

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 128, 0)
red = (255, 0, 0)

weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

evenMonth = 30
unevenMonth = 31
day_x = 0
day_y = 2

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
    x = 0
    y = 0
    for day in weekdays:
        color = get_week_day_color(day)
        sense.set_pixel(x, y, color)
        
        x = x + 1

def draw_month_days():
	global day_x
	global day_y
	for x in range(0, evenMonth):
		sense.set_pixel(day_x, day_y, green)
		day_x += 1
		if(day_x == 8):
			day_y += 1
			day_x = 0

# End functions.


# Main Program.

sense.clear(0,0,0)

draw_week_days()
draw_month_days()

# End Main Program.
