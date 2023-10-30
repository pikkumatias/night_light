
from gpiozero import LED
from datetime import datetime, timedelta
import time

# Initialize LEDs
green = LED(17)
yellow = LED(27)
red = LED(16)

# Define the time intervals for each LED color
GREEN_START_TIME = datetime.strptime("06:09", "%H:%M").time()
GREEN_END_TIME = datetime.strptime("19:09", "%H:%M").time()

RED_START_TIME = datetime.strptime("19:10", "%H:%M").time()
RED_END_TIME = datetime.strptime("05:54", "%H:%M").time()

YELLOW_START_TIME = datetime.strptime("05:55", "%H:%M").time()
YELLOW_END_TIME = GREEN_START_TIME  # Using the start of the green period as the end of yellow period for clarity

while True:
    current_time = datetime.now().time()

    # Check the times based on the defined intervals
    if RED_START_TIME <= current_time or current_time <= RED_END_TIME:  # This condition handles the time wrapping midnight for red
        green.off()
        yellow.off()
        red.on()
        print('Red is on')
    elif YELLOW_START_TIME <= current_time < YELLOW_END_TIME:
        green.off()
        yellow.on()
        red.off()
        print('Yellow is on')
    elif GREEN_START_TIME <= current_time < GREEN_END_TIME:
        green.on()
        yellow.off()
        red.off()
        print('Green is on')

    time.sleep(60)  # Check every minute
