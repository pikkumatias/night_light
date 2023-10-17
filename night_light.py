from gpiozero import LED
from datetime import datetime
import time

# Connector positions on board
green = LED(17)
yellow = LED(27)
red = LED(22)

# Loop to check time and what light should be on
while True:
    current_time = datetime.now().time()
    print(current_time)

    if current_time <= datetime.strptime("06:15:00", "%H:%M:%S").time() and current_time > datetime.strptime("19:10:00", "%H:%M:%S").time():
        green.off()
        yellow.off()
        red.on()
        print('red on')
    elif current_time >= datetime.strptime("06:00:00", "%H:%M:%S").time() and current_time < datetime.strptime("06:15:00", "%H:%M:%S").time():
        green.off()
        yellow.on()
        red.off()
        print('yellow on')
    else:
        green.on()
        yellow.off()
        red.off()
        print('green on')

    time.sleep(60)  # Check every minute
