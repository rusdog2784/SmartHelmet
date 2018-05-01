from max31855 import MAX31855, MAX31855Error
from Adafruit_AMG88xx import Adafruit_AMG88xx
from mq import *
import picamera
import pygame
import io
import os, sys
import math
import time
import numpy as np
from scipy.interpolate import griddata
from colour import Color

asset_dir = '/home/pi/Desktop/SmartHelmet/Assets/Images'
background_white = (255, 255, 255)
font_type = 'Helvetica'
font_size = 20
font_color = (000, 000, 000)
items = []

# Init pygame 
pygame.init()
pygame.display.set_caption('SmartHelmet')
screen = pygame.display.set_mode((0,0))

# Init camera
camera = picamera.PiCamera(resolution=(1280,720), framerate=30)
camera.rotation = 180
x = (screen.get_width() - camera.resolution[0]) / 2
y = (screen.get_height() - camera.resolution[1]) / 2

# Init buffer
rgb = bytearray(camera.resolution[0] * camera.resolution[1] * 3)

# Static Widgets ---------------------------------------------------------------------
#temperature
temp_surface = pygame.Surface((160, 52))
temp_surface.fill(background_white)
temp_surface.set_alpha(38)
temp_icon = pygame.image.load(os.path.join(asset_dir, 'temp_icon.png'))
items.append({'item':temp_surface, 'x':x+20, 'y':y+20-6})
items.append({'item':temp_icon, 'x':x+20+5, 'y':y+20})
#stopwatch
timer_surface = pygame.Surface((160, 52))
timer_surface.fill(background_white)
timer_surface.set_alpha(38)
timer_icon = pygame.image.load(os.path.join(asset_dir, 'stopwatch_icon.png'))
items.append({'item':timer_surface, 'x':x+1280-160-20, 'y':y+20-6})
items.append({'item':timer_icon, 'x':x+1280-40-20-5, 'y':y+20})
#gas
gas_surface = pygame.Surface((160, 104))
gas_surface.fill(background_white)
gas_surface.set_alpha(38)
#gas_icon = pygame.image.load(os.path.join(asset_dir, 'toxic_gas_icon.png'))
mq9_icon = pygame.image.load(os.path.join(asset_dir, 'CO_icon.png'))
mq4_icon = pygame.image.load(os.path.join(asset_dir, 'CH4_icon.png'))
items.append({'item':gas_surface, 'x':x+20, 'y':y+720-104-20})
#items.append({'item':gas_icon, 'x':x+20, 'y':y+720-52-20-20})
items.append({'item':mq9_icon, 'x':x+20+5, 'y':y+720-104-20+5})
items.append({'item':mq4_icon, 'x':x+20+5, 'y':y+720-52-15})
# End Of Static Widgets --------------------------------------------------------------


# Temperature Sensor Stuff -----------------------------------------------------------
cs_pin = 18            #15
clock_pin = 16         #29
data_pin = 15          #31
units = "f"
thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units)
tc = 0.0
# End Of Temperature Sensor Stuff ----------------------------------------------------


# MQ9 - CO Gas Sensor Stuff ----------------------------------------------------------
#mq = MQ()
#perc = None
# End of MQ9 - CO Gas Sensor Stuff ---------------------------------------------------


# Thermal Camera Stuff ---------------------------------------------------------------
#low range of the sensor (this will be blue on the screen)
MINTEMP = 26
#high range of the sensor (this will be red on the screen)
MAXTEMP = 32
#how many color values we can have
COLORDEPTH = 1024
os.putenv('SDL_FBDEV', '/dev/fb1')
#initialize the sensor
sensor = Adafruit_AMG88xx()
points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]
#the list of colors we can choose from
blue = Color("indigo")
colors = list(blue.range_to(Color("red"), COLORDEPTH))
#create the array of colors
colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]
displayPixelWidth = 160 / 30
displayPixelHeight = 160 / 30
#some utility functions
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))
def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
# End Of Thermal Camera Stuff --------------------------------------------------------


# Main loop
refresh_count = 0
exitFlag = True
while(exitFlag):
    for event in pygame.event.get():
        if(event.type is pygame.MOUSEBUTTONDOWN or 
           event.type is pygame.QUIT):
            exitFlag = False

    # Live streaming from the pi camera
    stream = io.BytesIO()
    camera.capture(stream, use_video_port=True, format='rgb')
    stream.seek(0)
    stream.readinto(rgb)
    stream.close()
    img = pygame.image.frombuffer(rgb[0:(camera.resolution[0] * camera.resolution[1] * 3)], camera.resolution, 'RGB')
    screen.fill(0)
    if img:
        screen.blit(img, (x, y))

    # Blit-ing static items onto display screen after live stream so they appear above
    for item in items:
        screen.blit(item['item'], (item['x'], item['y']))

    # Adding Thermal Camera to Screen
    thermal_surface = pygame.Surface((160, 160))
    thermal_surface.fill(background_white)
    pixels = sensor.readPixels()
    pixels = [map(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]
    bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
    for ix, row in enumerate(bicubic):
            for jx, pixel in enumerate(row):
                    pygame.draw.rect(thermal_surface, colors[constrain(int(pixel), 0, COLORDEPTH- 1)], (displayPixelHeight * ix, displayPixelWidth * jx, displayPixelHeight, displayPixelWidth))
    screen.blit(thermal_surface, (x+1280-160-20, y+720-160-20))

    # Updating Gas Sensor Data
    #perc = mq.MQPercentage()
    mq9_text = '0.0000 ppm'
    #mq9_text = '%0.4f ppm'% perc['CO']
    font = pygame.font.SysFont(font_type, font_size)
    mq9_text = font.render(mq9_text, True, font_color)
    screen.blit(mq9_text, (x+160+20-mq9_text.get_rect().width, y+720-104-5))

    # Updating Temperature Sensor Data
    tc = thermocouple.get()
    text = '%0.1f F' % tc
    font = pygame.font.SysFont(font_type, font_size)
    text = font.render(text, True, font_color)
    screen.blit(text, (x+160+20-text.get_rect().width-5, y+20+10))

    #refresh_count += 1
    pygame.display.update()

thermocouple.cleanup()
camera.close()
pygame.display.quit()
