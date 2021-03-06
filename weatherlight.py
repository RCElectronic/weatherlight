#python3

from time import sleep
from random import randint
import unicornhat as uh

def rain():
    uh.set_layout(uh.PHAT)
    uh.brightness(0.5)
    r,g,b = 0,0,255
    x = randint(0,7)

    for y in range(3,-1,-1):
        uh.clear()
        uh.set_pixel(x,y,r,g,b)
        uh.show()
        sleep(.2)

    return

def sun():
    uh.set_layout(uh.PHAT)
    uh.brightness(1)
    uh.clear()
    r,g,b = 255,255,100 #yellow
    for x in range(8):
        uh.set_pixel(x,3,r,g,b)
    for x in range(1,7):
        uh.set_pixel(x,2,r,g,b)
    for x in range(1,7):
        uh.set_pixel(x,1,r,g,b)

    r,g,b = 200,100,0 #orange
    uh.set_pixel(0,2,r,g,b)
    uh.set_pixel(7,2,r,g,b)
    uh.set_pixel(0,1,r,g,b)
    uh.set_pixel(7,1,r,g,b)
    for x in range(2,6):
        uh.set_pixel(x,0,r,g,b)

    r,g,b = 225,100,100 #red
    uh.set_pixel(0,1,r,g,b)
    uh.set_pixel(7,1,r,g,b)
    uh.set_pixel(0,0,r,g,b)
    uh.set_pixel(1,0,r,g,b)
    uh.set_pixel(6,0,r,g,b)
    uh.set_pixel(7,0,r,g,b)

    uh.show()
    return

def cloudy():
    uh.set_layout(uh.PHAT)
    uh.brightness(1)
    uh.clear()
    r,g,b = 0,50,100 # grey blue
    for x in range(8):
        uh.set_pixel(x,3,r,g,b)
    r,g,b = 64,64,64 # grey blue
    for y in range(1,3):
        for x in range(8):
            uh.set_pixel(x,y,r,g,b)
    r,g,b = 0,50,0 # green
    for x in range(8):
        uh.set_pixel(x,0,r,g,b)

    uh.show()
    return

if __name__ == '__main__':
    while True:
        cloudy()
