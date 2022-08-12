from binascii import crc32
import pygame
import os
import random
from PIL import Image
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

l0 = [0,0,0]
l1 = [237,237,237]
l2 = [98,98,98]
l3 = [162,162,162]

def generate_icon():
    
    baseImage = Image.new(mode="RGB", size=(16, 16))

    for i in range(16):
        for j in range(16):
            p = str(random.randint(0,3))
            exec("baseImage.putpixel((i,j), (l"+p+"[0], l"+p+"[1], l"+p+"[2], 255))")

    baseImage.save("images/icon.png")

generate_icon()

icon = pygame.image.load("images/icon.png")

display_width = 160
display_height = 90
fps = 15

width_half = display_width / 2
height_half = display_height / 2

os.environ['SDL_VIDEO_CENTERED'] = "1"

pygame.display.set_icon(icon)
pygame.display.set_caption("TV Static")
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

global screen_mode
screen_mode = 1

def screen_switch():
    global screen_mode
    if screen_mode == 1:
        gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
        screen_mode = 2
    else:
        gameDisplay = pygame.display.set_mode((display_width,display_height))
        screen_mode = 1

def main():

    up = True

    while up:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 or event.key == pygame.K_ESCAPE:
                    screen_switch()

        for i in range(display_width):
            for j in range(display_height):
                p = str(random.randint(0,3))
                exec("pygame.draw.rect(gameDisplay, l"+p+", (i*2, j*2, 2, 2))")

        pygame.display.update()
        clock.tick(fps)

main()