from sense_hat import SenseHat

# Object constructions.

sense = SenseHat()

# End object constructions.

sense.clear(0,0,0)

green = (0, 128, 0)
evenMonth = 30
unevenMonth = 31
day_x = 0
day_y = 0

for x in range(0, evenMonth):
	sense.set_pixel(day_x, day_y, green)
	day_x += 1
	if(day_x == 8):
		day_y += 1
		day_x = 0
