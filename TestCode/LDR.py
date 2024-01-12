from time import sleep
from CustomPymata4 import *
board = CustomPymata4(baud_rate = 57600, com_port = "COM5")
board.set_pin_mode_analog_input(2)
board.set_pin_mode_digital_output(7)
sleep(1)    #this delay is added here, so that the first value of 0 can be ignored
for x in range(200):
    sensorValue, timeStamp = board.analog_read(2)   # read the sensor value and timestamp that are returned
    print(sensorValue, " ", timeStamp)     
    #convert to resistance in Kohms         
    resistanceSensor = (1023-sensorValue)*10/sensorValue
    print(f"The resistance of the light sensor is: {resistanceSensor} KOhm")
    #convert the resitance to Lux
    klux = 325 * pow(resistanceSensor, -1.4) / 1000
    print(f"Illuminance is almost {klux} Kilo lux")
    #display on Arduino
    board.displayShow(klux)
    sleep(1)
    #if it is dark, the turn on the yellow light
    if sensorValue < 600:           #600 is the threshold value
        board.digital_pin_write(7,1)
    else:
        board.digital_pin_write(7,0)