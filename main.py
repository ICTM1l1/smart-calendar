from sense_hat import SenseHat
from datetime import datetime
import weather
import calendar

# Object constructions.

sense = SenseHat()

# End object constructions.


# Application configurations.

day_is_active = False # Displays the current day on True or the current month on False.

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 128, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
pink = (255, 20, 147)
purple = (75, 0 , 130)
brown = (160, 82, 45)

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
month_days = {}

now = datetime.now()
start_year = now.year
start_month = now.month
today = datetime(now.year, now.month, now.day)

week_days_position_y = 0
month_day_y = 1

controller_pos_x = 0
controller_pos_y = 1

previous_pos_color = red
previous_pos_x = controller_pos_x
previous_pos_y = controller_pos_y

navigate_history_pos_x = 0
navigate_history_pos_y = 7
navigate_history_year_pos_x = 1
navigate_history_year_pos_y = 7
navigate_future_pos_x = 6
navigate_future_pos_y = 7
navigate_future_year_pos_x = 5
navigate_future_year_pos_y = 7
navigate_current_day_pos_x = 3
navigate_current_day_pos_y = 7

# End application configurations.


# Functions.

def draw_controller():
    global previous_pos_color
    previous_pos_color = sense.get_pixel(controller_pos_x, controller_pos_y)
    
    sense.set_pixel(controller_pos_x, controller_pos_y, pink)

def draw_navigation():
    sense.set_pixel(navigate_history_pos_x, navigate_history_pos_y, pink)
    sense.set_pixel(navigate_history_year_pos_x, navigate_history_year_pos_y, purple)
    sense.set_pixel(navigate_future_pos_x, navigate_future_pos_y, pink)
    sense.set_pixel(navigate_future_year_pos_x, navigate_future_year_pos_y, purple)
    sense.set_pixel(navigate_current_day_pos_x, navigate_current_day_pos_y, brown)

def move_up(event):
    global controller_pos_y
    global previous_pos_color
    global previous_pos_x
    global previous_pos_y
    
    if event.action == 'pressed' and controller_pos_y > 1:
        controller_pos_y -= 1
        
        # Changes the previous pixel back to his previous color.
        sense.set_pixel(previous_pos_x, previous_pos_y, previous_pos_color)
        
        # Write the color to the previous color if it is not the color from the cursor.
        previous_color = sense.get_pixel(controller_pos_x, controller_pos_y)
        if previous_color != pink:
            previous_pos_color = previous_color 
        
        sense.set_pixel(controller_pos_x, controller_pos_y, pink)
        
        # Keeps track of the previous position of the cursor.
        if previous_pos_x != controller_pos_x:
            previous_pos_x = controller_pos_x
        
        if previous_pos_y != controller_pos_y:
            previous_pos_y = controller_pos_y
    
    # Reinitialize the program.
    run_program()
            
def move_down(event):
    global controller_pos_y
    global previous_pos_color
    global previous_pos_x
    global previous_pos_y
    
    if event.action == 'pressed' and controller_pos_y < 7:
        controller_pos_y += 1
        
        # Changes the previous pixel back to his previous color.
        sense.set_pixel(previous_pos_x, previous_pos_y, previous_pos_color)
        
        # Write the color to the previous color if it is not the color from the cursor.
        previous_color = sense.get_pixel(controller_pos_x, controller_pos_y)
        if previous_color != pink:
            previous_pos_color = previous_color 
        
        sense.set_pixel(controller_pos_x, controller_pos_y, pink)
        
        # Keeps track of the previous position of the cursor.
        if previous_pos_x != controller_pos_x:
            previous_pos_x = controller_pos_x
        
        if previous_pos_y != controller_pos_y:
            previous_pos_y = controller_pos_y
    
    # Reinitialize the program.
    run_program()
        
def move_right(event):
    global controller_pos_x
    global previous_pos_color
    global previous_pos_x
    global previous_pos_y
    
    if event.action == 'pressed' and controller_pos_x < 6:
        controller_pos_x += 1
        
        # Changes the previous pixel back to his previous color.
        sense.set_pixel(previous_pos_x, previous_pos_y, previous_pos_color)
        
        # Write the color to the previous color if it is not the color from the cursor.
        previous_color = sense.get_pixel(controller_pos_x, controller_pos_y)
        if previous_color != pink:
            previous_pos_color = previous_color 
        
        sense.set_pixel(controller_pos_x, controller_pos_y, pink)
        
        # Keeps track of the previous position of the cursor.
        if previous_pos_x != controller_pos_x:
            previous_pos_x = controller_pos_x
        
        if previous_pos_y != controller_pos_y:
            previous_pos_y = controller_pos_y
    
    # Reinitialize the program.
    run_program()
        
def move_left(event):
    global controller_pos_x
    global previous_pos_color
    global previous_pos_x
    global previous_pos_y
    
    if event.action == 'pressed' and controller_pos_x > 0:
        controller_pos_x -= 1
        
        # Changes the previous pixel back to his previous color.
        sense.set_pixel(previous_pos_x, previous_pos_y, previous_pos_color)
        
        # Write the color to the previous color if it is not the color from the cursor.
        previous_color = sense.get_pixel(controller_pos_x, controller_pos_y)
        if previous_color != pink:
            previous_pos_color = previous_color 
        
        sense.set_pixel(controller_pos_x, controller_pos_y, pink)

        # Keeps track of the previous position of the cursor.
        if previous_pos_x != controller_pos_x:
            previous_pos_x = controller_pos_x
        
        if previous_pos_y != controller_pos_y:
            previous_pos_y = controller_pos_y
            
    # Reinitialize the program.
    run_program()

def click(event):
    global start_year
    global start_month
    global controller_pos_x
    global controller_pos_y
    previous_year = start_year
    previous_month = start_month
    
    if event.action != 'pressed':
        return
    
    if day_is_active:
        run_program()
        return
    
    # Go to the previous month.
    if controller_pos_x == navigate_history_pos_x and controller_pos_y == navigate_history_pos_y:
        start_month -= 1
    
    # Go to the previous year.
    if controller_pos_x == navigate_history_year_pos_x and controller_pos_y == navigate_history_year_pos_y:
        start_year -= 1
    
    # Go to the next month.
    if controller_pos_x == navigate_future_pos_x and controller_pos_y == navigate_future_pos_y:
        start_month += 1
    
    # Go to the next year.
    if controller_pos_x == navigate_future_year_pos_x and controller_pos_y == navigate_future_year_pos_y:
        start_year += 1
        
    # Go to the current year and month.
    if controller_pos_x == navigate_current_day_pos_x and controller_pos_y == navigate_current_day_pos_y:
        current_datetime = datetime.now()
        start_year = current_datetime.year
        start_month = current_datetime.month
    
    # Decrease or increase the year if the month has reached an invalid value.
    if start_month < 1:
        start_month = 12
        start_year -= 1
    elif start_month > 12:
        start_month = 1
        start_year += 1
    
    if start_month != previous_month or start_year != previous_year:
        controller_pos_x = 0
        controller_pos_y = 1
        
        # Show the current month and year.
        sense.show_message('%s %s' % (calendar.month_name[start_month], start_year))
    
    # Shows a specific date.
    day_position = '{pos_y}{pos_x}'
    day_position = day_position.format(pos_y = controller_pos_y, pos_x = controller_pos_x)
    
    selected_day = month_days.get(day_position)
    if selected_day != None:
        display_day(selected_day)
        return
        
    # Reinitialize the program.
    run_program()

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
            day_position = '{pos_y}{pos_x}'
            day_position = day_position.format(pos_y = month_day_y, pos_x = month_day_x)
            month_days[day_position] = day
            
            month_day_x += 1
            
        # Create new row for displaying the days.
        month_day_y += 1
        month_day_x = 0

def display_day(day):
    global day_is_active
    
    sense.clear(0,0,0)
    day_is_active = True
    
    selected_date = datetime(start_year, start_month, day)
    current_weather = weather.request_forecast(selected_date)
    
    # Print data for selected day.
    sense.show_message(selected_date.strftime('%d-%m-%y'))
    if current_weather:
        avg_temp_c = round(current_weather['avgtemp_c'])
        sense.show_message("%sC" % avg_temp_c)
    
    return run_program()

def run_program():
    global month_day_y
    global day_is_active
    
    day_is_active = False
    
    sense.clear(0,0,0)
    month_day_y = 1

    draw_week_days()
    draw_month_days()
    draw_navigation()
    draw_controller()
    
# End functions.


# Main Program.

if day_is_active:
    display_day(now.day)
else:
    run_program()

sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
sense.stick.direction_right = move_right
sense.stick.direction_left = move_left
sense.stick.direction_middle = click

# End Main Program.
