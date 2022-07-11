import RPi.GPIO as GPIO
import dht11       # ・・・ ①
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)       # ・・・ ②
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=24)      # ・・・ ③

while True:
    result = instance.read()    # ・・・ ④
    if result.is_valid():    # ・・・ ⑤
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)    # ・・・ ⑥
        print("Humidity: %d %%" % result.humidity) 

    time.sleep(1)
