from machine import pin
import time

led = Pin(25, Pin.OUT)

while True:
    led(1)
    time.Sleep(1)
    led(0)
    time.sleep(1)
