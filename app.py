# Wall GUI
# Displays an interactive GUI for the NCSSM CS Department Corkboard.

import eel
from sense_hat import SenseHat
import random

SENSE_HAT = False


eel.init("web")
sense = SenseHat()



@eel.expose
def get_temperature():
	if not SENSE_HAT:
		return 0
	return sense.get_temperature()

@eel.expose
def get_humidity():
	if not SENSE_HAT:
		return 0
	return sense.get_humidity()

@eel.expose
def get_pressure():
	if not SENSE_HAT:
		return 0
	return sense.get_pressure()

# This Sense Hat has no Color Sensor
# @eel.expose
# def get_light():
# 	return sense.color.color

@eel.expose
def get_acceleration():
	if not SENSE_HAT:
		return (0,0,0)
	return sense.get_accelerometer_raw()

# Almost Useless:
@eel.expose
def get_orientation():
	if not SENSE_HAT:
		return (0,0,0)
	return sense.get_orientation()

# Almost Useless:
@eel.expose
def get_compass():
	if not SENSE_HAT:
		return (0,0,0)
	return sense.get_compass()

#Almost Useless:
@eel.expose
def get_cardinal():
	if not SENSE_HAT:
		return '#'

	heading = get_compass()
	if heading > 315 or heading < 45:
		return 'N'
	elif heading < 135:
		return 'E'
	elif heading < 225:
		return 'S'
	else:
		return 'W'
	
@eel.expose
def get_joystick_pos():
	if not SENSE_HAT:
		return "None"
	event = sense.stick.wait_for_event()
	return event.direction

@eel.expose
def get_joystick_event():
	if not SENSE_HAT:
		return "None"
	return sense.stick.wait_for_event()



fortune_list = [
		"You have a long, happy life ahead of you...\nUnless you ate the fish last friday.", 
		"Why're ya asking me?",
		"I don't care what you said.\nYou're wrong.",
		"\"yes\"\nAre you happy now?",
		"You will find love in a hopeless place. *Dramatic singing*",
		"Refrain from rejoicing in the rain, and your reams of relegated relatives will report your recurrent reticence.",
		"Eat more cookies. Everyone feels better after cookies.",
		"Don't sleep on your work--beds are much comfier.",
		"Light trickles through the trees, a warm antagonist to the raindrops that have soaked your shoes.",
		"Copilot is now available in Microsoft notepad; things can always get worse.",
		"If the world is your oyster, you must be a pearl.",
		"Don't skip meals. Ketones smell bad.",
		"Do you ever feel like a plastic bag; getting caught in orbit, littering the ISS?",
		"Dream bigger than the giant chimichanga at Cosmic!",
		"Take a deep breath. In for three seconds, hold for two, and release.",
		"History Rhymes.",
		"To quickly staunch an emotional wound, apply a liberal serving of ice cream. Therapy is recommended for long-term recovery.",
		"Red Bull is not an adequate substitute for sleep.",
		"Trace your eye along the bark of a tree, and follow the trunk up to its leaves.",
		"Lactose intolerance is a challenge.",
		"Some day, you must choose between being good or great.",
		"Watch out for bones in your fried chicken.",
		"Love is temporary. Chicken nuggets are forever.",
		"If you feel old now, just wait.",
		"The Minecraft Movie will be the cinematic and cultural touchstone of a generation.",
		"Insert Fortune Here",
		"You will have a fortuous encounter in late May.",
		"Hey, ChatGPT, give me a fortune cookie. No, I didn't mean chocolate chip!",
		"The shower will not scald you tomorrow.",
		"If you gaze long into Hunt Kitchen, Hunt Kitchen also gazes into you.",
		"Your time here will go faster than you'd ever prepared for."
		]

@eel.expose
def app_fortune_request():
	fortune_index = random.randint(0, len(fortune_list)-1)
	return fortune_list[fortune_index]

@eel.expose
def app_environment():
	if not SENSE_HAT:
		return "No Hat"
	temp = get_temperature()
	humid = get_humidity()
	pressure = get_pressure()
	return f"Temperature: {temp:.1f} C    Humidity: {humid:.1f} %    Pressure: {pressure:.1f} mbar"

@eel.expose
def app_position():
	if not SENSE_HAT:
		return "No Hat"
	o = get_orientation()
	a = get_acceleration()
	heading = get_compass()
	direction = get_cardinal()
	pitch = o["pitch"]
	yaw = o["yaw"]
	roll = o["roll"]
	x = a["x"]
	y = a["y"]
	z = a["z"]
	return f"Orientation: {pitch:.1f}, {yaw:.1f}, {roll:.1f} deg    Accleration: {x:.1f}, {y:.1f}, {z:.1f} m/s^2    Compass {heading:.1f} ({direction}) deg" 

@eel.expose
def app_light_sensor():
	# r, g, b, c = get_light()
	# return f"Color: r{r:.1f}, g{g:.1f}, b{b:.1f}, c{c:.1f}" 
	return "This Sense Hat has no Color Sensor"

@eel.expose
def app_joystick_pos():
	if not SENSE_HAT:
		return "No Hat"
	direction = get_joystick_pos()
	return f"Joystick Pushed {direction}"


# Set up Main Window
if SENSE_HAT:
	sense.show_letter("W")
eel.start("index.html", cmdline_args=['--kiosk'])
