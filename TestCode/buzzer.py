import time
from CustomPymata4 import *

board = CustomPymata4(baud_rate = 57600, com_port = "COM4")
BUZZER = [3]
def buzzerOn():
    for PIN in BUZZER:
        board.digital_pin_write(PIN, 1)
        board.play_tone(1450,3000)
        time.sleep(0.5)
        board.digital_pin_write(PIN, 0)
        time.sleep(0.5)
while True:
    buzzerOn()