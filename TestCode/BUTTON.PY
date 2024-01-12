from datetime import datetime
from CustomPymata4 import CustomPymata4 
import time

board = CustomPymata4(com_port = "COM4", baud_rate=57600)
RED_LED= 6
GREEN_LED = 7
board.set_pin_mode_digital_output(RED_LED)
board.set_pin_mode_digital_output(GREEN_LED)
RED_INTERVAL  = 0.125 # seconds
GREEN_INTERVAL = 0.25 # seconds
red_led_state = 0
green_led_state = 0
red_led_time = datetime.now()
green_led_time = datetime.now()

while True : 
  # Get current time.
  current_time = datetime.now()
  # Has time elapsed?
  if (current_time - red_led_time).total_seconds() >  RED_INTERVAL  :
     # Flip the state.
     red_led_state != red_led_state
     board.digital_write(RED_LED, red_led_state)
     print("red led")
     time.sleep(1)
     # Reset for next interval.
     red_led_time = current_time
  if (current_time - green_led_time).total_seconds() > GREEN_INTERVAL :
     # Flip the state.
     green_led_state != green_led_state
     board.digital_write(GREEN_LED, green_led_state)
     print("green led")
     time.sleep(1)
     # Reset for next interval.
     green_led_time = current_time