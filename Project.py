import time
import utime
import random
import machine
from pimoroni import Button, RGBLED
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_RGB332

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_RGB332, rotate=0)
w,h=display.get_bounds()
display.set_backlight(1.0)

#buttons fetched from pins
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()

led = RGBLED(6, 7, 8)
#RGB (R, G, B)
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)
RED = display.create_pen(255, 0, 0)
BLUE = display.create_pen(0, 0, 255)
ORANGE = display.create_pen(255, 102, 0)
color = display.create_pen(0,100,100)



while True:
    clear()
    led.set_rgb(0, 0, 0)
    display.set_pen(WHITE)
    display.set_font("serif_italic")
    display.text("TIME ZONE", 30, 65, scale=1)
    
    display.update()
    time.sleep(1.0)

    while True:
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        display.set_font("serif_italic")
        display.text("A-Eastern Time", 20, 35, scale=0.7)
        display.text("B-Central Time", 20,55, scale=0.7)
        display.text("X-Mountain Time", 20, 75, scale=0.7)
        display.text("Y-Pacific Time", 20, 95, scale=0.7)
        display.update()
    
        
        if button_a.read(): #button A pressed
            display.set_pen(RED) #background color.
            led.set_rgb(9,0,0)
            display.clear()
            display.set_pen(WHITE)
            display.set_font("serif_italic")
            display.text("EASTERN TIME", 25, 65, scale=0.7) #display 
            display.update()
            utime.sleep(1.0)
            display.set_pen(RED) #background color.
            display.clear()
            
            while True:
                time = utime.localtime()[3:6] #gets localtime from machine.RTC
                timestring="%02d:%02d:%02d"%(time)
                date = utime.localtime()[0:3]
                datestring="%04d-%02d-%02d"%(date)
                display.set_pen(WHITE)
                display.set_font("serif_italic")
                display.text("EASTERN TIME", 35, 35, scale=0.7)
                display.text(timestring, 35, 65, scale=1.2)
                display.text(datestring, 45, 100, scale=0.6)
                display.text("A - Menu", 10, 120, scale = 0.5)
                display.update()
                display.set_pen(RED) #background color.
                display.clear()
                if button_a.read():
                    led.set_rgb(0,0,0)
                    display.clear()
                    break
    
        if button_b.read(): #button B pressed
            display.set_pen(ORANGE) #background color.
            led.set_rgb(9,4,0)
            display.clear()
            display.set_pen(BLACK)
            display.set_font("serif_italic")
            display.text("CENTRAL TIME", 25, 65, scale=0.7) #display 
            display.update()
            utime.sleep(1.0)
            display.set_pen(ORANGE) #background color.
            display.clear()
            while True:
                time_CT = utime.gmtime(utime.time()-3600)[3:6]
                timestring="%02d:%02d:%02d"%(time_CT)
                date = utime.gmtime(utime.time()-3600)[0:3]
                datestring="%04d-%02d-%02d"%(date)
                display.set_pen(BLACK)
                display.set_font("serif_italic")
                display.text("CENTRAL TIME", 25, 35, scale=0.7)
                display.text(timestring, 35, 65, scale=1.2)
                display.text(datestring, 45, 100, scale=0.6)
                display.text("B - Menu", 10, 120, scale = 0.5)
                display.update()
                display.set_pen(ORANGE) #background color.
                display.update()
                display.clear()
                if button_b.read():
                    led.set_rgb(0,0,0)
                    display.clear()
                    break
    
        if button_x.read(): #button X pressed
            display.set_pen(WHITE) #background color.
            led.set_rgb(9,9,9)
            display.clear()
            display.set_pen(BLACK)
            display.set_font("serif_italic")
            display.text("MOUNTAIN TIME", 25, 65, scale=0.7)
            display.update()
            utime.sleep(1.0)
            display.set_pen(WHITE) #background color.
            display.clear()
            while True:
                time = utime.gmtime(utime.time()-7200)[3:6]
                timestring="%02d:%02d:%02d"%(time)
                date = utime.gmtime(utime.time()-7200)[0:3]
                datestring="%04d-%02d-%02d"%(date)
                display.set_pen(BLACK)
                display.set_font("serif_italic")
                display.text("MOUNTAIN TIME", 25, 35, scale=0.7)
                display.text(timestring, 35, 65, scale=1.2)
                display.text(datestring, 45, 100, scale=0.6)
                display.text("X - Menu", 10, 120, scale = 0.5)
                display.update()
                display.set_pen(WHITE) #background color.
                display.update()
                display.clear()
                if button_x.read():
                    led.set_rgb(0,0,0)
                    display.clear()
                    break
    
        if button_y.read(): #button Y pressed
            display.set_pen(CYAN) #background color.
            led.set_rgb(0,9,9)
            display.clear()
            display.set_pen(BLACK)
            display.set_font("serif_italic")
            display.text("PACIFIC TIME", 45, 65, scale=0.7) #display 
            display.update()
            utime.sleep(1.0)
            display.set_pen(CYAN) #background color.
            display.clear()
            while True:
                time_PT= utime.gmtime(utime.time()-10800)[3:6]
                timestring="%02d:%02d:%02d"%(time_PT)
                date = utime.gmtime(utime.time()-10800)[0:3]
                datestring="%04d-%02d-%02d"%(date)
                display.set_pen(BLACK)
                display.set_font("serif_italic")
                display.text("PACIFIC TIME", 35, 35, scale=0.7)
                display.text(timestring, 35, 65, scale=1.2)
                display.text(datestring, 45, 100, scale=0.6)
                display.text("Y - Menu", 10, 120, scale = 0.5)
                display.update()
                display.set_pen(CYAN) #background color.
                display.update()
                display.clear()
                if button_y.read():
                    led.set_rgb(0,0,0)
                    display.clear()
                    break