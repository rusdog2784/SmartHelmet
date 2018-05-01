import pygame, time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
size = [700, 500]
screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()
font = pygame.font.SysFont("Helvetica", 24)

frame_count = 0
frame_rate = 60
start_time = 90

timer_resolution = pygame.TIMER_RESOLUTION
print timer_resolution

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    print pygame.time.get_ticks()
    screen.fill(WHITE)
    timer_resolution = pygame.TIMER_RESOLUTION
    print timer_resolution
    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "%02d:%02d" % (minutes, seconds)
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 250])
    frame_count += 1
    clock.tick(frame_rate)
    pygame.display.flip()

pygame.quit()
