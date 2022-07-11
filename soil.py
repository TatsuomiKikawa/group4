import RPi.GPIO as GPIO
from time import sleep
 
def readadc(adcnum,clk,mosi,miso,cs):
    if adcnum >= 0  and adcnum <= 7:#読み込むチャンネルが0～7の場合
        GPIO.output(cs,GPIO.HIGH)
        GPIO.output(clk,GPIO.LOW)
        GPIO.output(cs,GPIO.LOW)
 
        cmdout=adcnum
        cmdout |=0x18
        cmdout <<=3
        for i in range(5):
            if cmdout & 0x80:
                GPIO.output(mosi,GPIO.HIGH)
            else:
                GPIO.output(mosi,GPIO.LOW)
            cmdout <<=1
            GPIO.output(clk,GPIO.HIGH)
            GPIO.output(clk,GPIO.LOW)
        adcout=0
        for i in range(11):#MCP3008の10ビットとヌルビットを足した１１
            GPIO.output(clk,GPIO.HIGH)
            GPIO.output(clk,GPIO.LOW)
            adcout <<=1
            if i>0 and GPIO.input(miso)==GPIO.HIGH:
                adcout |=0x1
        GPIO.output(cs,GPIO.HIGH)
        return adcout#0～1023の値を返す
    
    else:#読み込むチャンネルが0～7に無ければ-1を返す
        return -1
 
GPIO.setmode(GPIO.BCM)
 
spiclk=11 #GPIOピン
spimosi=10
spimiso=9
spics=8
 
GPIO.setup(spiclk,GPIO.OUT)
GPIO.setup(spimosi,GPIO.OUT)
GPIO.setup(spimiso,GPIO.IN)
GPIO.setup(spics,GPIO.OUT)
 
try:
    while True:
        value=readadc(0,spiclk,spimosi,spimiso,spics)#valueに0～1023の値がくる   value　入力される値
        print(value)
        sleep(1)#1秒間隔
except KeyboardInterrupt:
    pass
GPIO.cleanup()
