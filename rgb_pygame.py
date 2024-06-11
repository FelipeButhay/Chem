import pygame
import os

import tkinter as tk

resolution_screen = tk.Tk()
SX = resolution_screen.winfo_screenwidth()
SY = resolution_screen.winfo_screenheight()
direc = os.path.dirname(os.path.abspath(__file__)).replace('\'', '/')

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SX, SY))
pygame.display.set_caption("Lorem Ipsum")
pygame.mouse.get_visible
        
font = tuple(pygame.font.Font(f"{direc}/CONSOLA.TTF", int(x*SY)) for x in [.1, .07, .028, .015])

rgb = [0, 0, 0]
rgb_selected = 0
select = lambda n, rgb_n: "> " if n == rgb_n else "  "
cword = ""

while True:
    rgb_selected_save = rgb_selected
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stage = None
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.dict['unicode'] == "\x08":
                cword = cword[0:-1]
            elif event.dict['unicode'].isnumeric():
                cword += event.dict['unicode']
                
            if event.dict["scancode"] == 82:
                rgb_selected -= 1
            if event.dict["scancode"] == 81:
                rgb_selected += 1
    
    screen.fill("white")
    
    if rgb_selected != rgb_selected_save:
        if cword == "":
            cword = 0
        rgb[rgb_selected_save%3] = int(cword)
        cword = str(rgb[rgb_selected%3])
    
    red_txt   = font[0].render(f"{select(rgb_selected%3, 0)}Red:   {rgb[0]}", True, tuple(50 for x in range(3)))
    screen.blit(red_txt, red_txt.get_rect(midleft = (SX*.1, SY*.3)))
    
    green_txt = font[0].render(f"{select(rgb_selected%3, 1)}Green: {rgb[1]}", True, tuple(50 for x in range(3)))
    screen.blit(green_txt, green_txt.get_rect(midleft = (SX*.1, SY*.5)))
    
    blue_txt  = font[0].render(f"{select(rgb_selected%3, 2)}Blue:  {rgb[2]}", True, tuple(50 for x in range(3)))
    screen.blit(blue_txt, blue_txt.get_rect(midleft = (SX*.1, SY*.7)))
    
    cword_txt  = font[1].render(cword, True, tuple(50 for x in range(3)))
    screen.blit(cword_txt, cword_txt.get_rect(midleft = (SX*.1, SY*.9)))
    
    pygame.draw.rect(screen, "black", (SX*.5875, (SY-SX*.375)/2, SX*.375, SX*.375))
    try:
        pygame.draw.rect(screen, rgb, (SX*.6, (SY-SX*.35)/2, SX*.35, SX*.35))
    except:
        pass
            
    pygame.display.update()
    clock.tick(60)