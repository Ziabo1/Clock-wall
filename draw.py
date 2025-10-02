import pygame
import math
from datetime import datetime


pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
center_x, center_y = 325, 240
radius = 230
Clock_Noise = pygame.mixer.Sound("clock-ticking.wav")
last_second = +55

run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (128, 128, 128), (325, 240), 230)
    pygame.draw.circle(screen, (15, 50, 128), (325, 240), 6)

    now = datetime.now()

    if now.second != last_second:
        Clock_Noise.play()
        last_second = now.second

    for i in range(60):
        angle = i * (2 * math.pi / 60)
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle))

        if i % 5 == 0:
            pygame.draw.rect(screen, (0, 0, 0), (x-5, y-5, 10, 10))
        else:
            pygame.draw.rect(screen, (0, 255, 0), (x-2, y-2, 4, 4))

    s = datetime.now().second
    angle1 = 360 / 60 * s
    end_offset = [radius * math.cos(math.radians(angle1 - 90)),
                  radius * math.sin(math.radians(angle1 - 90))]
    end_position = (center_x + end_offset[0], center_y + end_offset[1])
    pygame.draw.line(screen, (255, 0, 0),
                     (center_x, center_y), end_position, 3)

    m = datetime.now().minute + datetime.now().second / 60
    angle1 = 360 / 60 * m
    end_offset = [radius * math.cos(math.radians(angle1 - 90)),
                  radius * math.sin(math.radians(angle1 - 90))]
    end_position = (center_x + end_offset[0], center_y + end_offset[1])
    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y), end_position, 3)

    h = datetime.now().hour % 12 + datetime.now().minute / 60
    angle1 = 360 / 12 * h
    hour_length = radius - 20
    end_offset = [hour_length * math.cos(math.radians(angle1 - 90)),
                  hour_length * math.sin(math.radians(angle1 - 90))]
    end_position = (center_x + end_offset[0], center_y + end_offset[1])
    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y), end_position, 8)

    pygame.display.flip()
pygame.quit()
