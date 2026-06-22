from machine import Pin, PWM
from time import sleep

def light_repeatition():
    firstnum = 0
    secondnum = 0
    thirdnum = 0

    while(firstnum < 65535):
        firstnum += increase

        if(firstnum > 65535):
            firstnum = 65535

        redled.duty_u16(firstnum)
        greenled.duty_u16(secondnum)
        blueled.duty_u16(thirdnum)

        sleep(.1)

    while(secondnum < 65535):
        secondnum += increase

        if(secondnum > 65535):
            secondnum = 65535

        redled.duty_u16(firstnum)
        greenled.duty_u16(secondnum)
        blueled.duty_u16(thirdnum)

        sleep(.1)

    while(thirdnum < 65535):
        thirdnum += increase

        if(thirdnum > 65535):
            thirdnum = 65535

        redled.duty_u16(firstnum)
        greenled.duty_u16(secondnum)
        blueled.duty_u16(thirdnum)

        sleep(.1)

    sleep(1)

    redled.duty_u16(0)
    greenled.duty_u16(0)
    blueled.duty_u16(0)

    sleep(1)


redpin = 13
greenpin = 14
bluepin = 15

increase = 500

redled = PWM(Pin(redpin))
greenled = PWM(Pin(greenpin))
blueled = PWM(Pin(bluepin))

redled.freq(1000)
greenled.freq(1000)
blueled.freq(1000)

redled.duty_u16(0)
greenled.duty_u16(0)
blueled.duty_u16(0)

while True:
    light_repeatition()