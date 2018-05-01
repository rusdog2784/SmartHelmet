import picamera
import pygame
import io
import os, sys

directory = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
asset_dir = '/home/pi/Desktop/SmartHelmet/Assets/Images'
background_white = (255, 255, 255)

def text_to_screen(screen, text, x, y, size = 24, color = (200, 000, 000), font_type = 'Helvetica'):
    try:
        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
    except Exception, e:
        print 'Font Error, saw it coming'
        raise e

def icon_to_screen(screen, path, x, y):
    try:
        img = pygame.image.load(path)
        screen.blit(img, (x, y))
    except Exception, e:
        print 'Error adding icon to screen'
        #raise e

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

# Main loop
exitFlag = True
while(exitFlag):
    for event in pygame.event.get():
        if(event.type is pygame.MOUSEBUTTONDOWN or 
           event.type is pygame.QUIT):
            exitFlag = False
 
    stream = io.BytesIO()
    camera.capture(stream, use_video_port=True, format='rgb')
    stream.seek(0)
    stream.readinto(rgb)
    stream.close()
    img = pygame.image.frombuffer(rgb[0:(camera.resolution[0] * camera.resolution[1] * 3)], camera.resolution, 'RGB')

    screen.fill(0)
    if img:
        screen.blit(img, (x,y))
    # Adding temperature icon
    temp_surface = pygame.Surface((140, 52))
    temp_surface.fill(background_white)
    temp_surface.set_alpha(38)
    screen.blit(temp_surface, (x+20, y+20-6))
    icon_to_screen(screen, os.path.join(asset_dir, 'temp_icon.gif'), x+20, y+20)
    # Adding stopwatch icon
    icon_to_screen(screen, os.path.join(asset_dir, 'stopwatch_icon.gif'), x+1280-40-20, y+20)
    # Adding gas icon
    icon_to_screen(screen, os.path.join(asset_dir, 'toxic_gas_icon.gif'), x+20, y+720-40-100)

    pygame.display.update()

camera.close()
pygame.display.quit()
