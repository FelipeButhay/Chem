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
        
font = tuple(pygame.font.Font(f"{direc}/CONSOLA.TTF", int(x*SY)) for x in [.1, .07, .028, .016])

mouse_data = (0,0), False, False

r_open = lambda start, end: [x for x in range(start, end+1)]

FACIL = r_open(1, 20) + [22, 26, 28, 29, 30]
NORMAL = r_open(1, 20) + r_open(31, 36) + r_open(49, 54) + r_open(81, 86) + [22, 25, 26, 27, 28, 29, 30, 37, 38, 47, 55, 56, 76, 78, 79, 80, 87, 88, 92, 94]
DIFICL = r_open(1, 56) + r_open(72, 88) + [92, 94]
COMPLETA = r_open(1, 118)

dificultades = [FACIL, NORMAL, DIFICL, COMPLETA]

# 0 = menu, 1 = tabla-elemento, 2 = elemento-tabla, 3 = fin del juego
stage = 0

# stage, game_mode, dificulty, nombre-simbolo, elemento, tiempo, cword
game_data = 0, 0, 0, 0, None, 0, ""

def time_format(seconds: int)->str:
    time_s = int(seconds%60**2/60**1)
    if time_s < 10:
        time_s = "0"+ str(time_s)
    else:
        time_s = str(time_s)
        
    time_min = int(seconds%60**3/60**2)
    if time_min < 10:
        time_min = "0"+ str(time_min)
    else:
        time_min = str(time_min)
        
    time_h = int(seconds%60**4/60**3)
    if time_h < 10:
        time_h = "0"+ str(time_h)
    else:
        time_h = str(time_h)
        
    return f"{time_h}:{time_min}:{time_s}"

def mouse_data_reader(mouse_data):
    mouse_pos, mouse_save, mouse = mouse_data
    
    mouse_pos = pygame.mouse.get_pos()
    mouse_save = mouse
    mouse = pygame.mouse.get_pressed()[0]   
    
    return mouse_pos, mouse_save, mouse

def normalize_words(word: str) -> str:
    word = word.strip().lower()
    tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    new_word = ''.join(tildes.get(l, l) for l in word)
    
    return new_word

if __name__ == "__main__":
    import stages.tp_menu
    import stages.txt_elementos
        
    import stages.tp_tabla_elemento
    import stages.tp_elemento_tabla
    import stages.tp_simbolo_elemento_both
    
    import stages.tp_gameover
        
    while stage != None:
        while stage == 0: # MENU
            mouse_data = mouse_data_reader(mouse_data)
            game_data = stages.tp_menu.menu(mouse_data, game_data)
            stage = game_data[0] 

            pygame.display.update()
            clock.tick(60)

        grid, grid_data = stages.txt_elementos.tabla_to_grid(dificultades[game_data[2]])
        while stage == 1: # TABLA - ELEMENTO
            mouse_data = mouse_data_reader(mouse_data)
            game_data = stages.tp_tabla_elemento.game(mouse_data, game_data, grid, grid_data)
            stage = game_data[0]

            pygame.display.update()
            clock.tick(60) 

        while stage == 2: # ELEMENTO - TABLA
            mouse_data = mouse_data_reader(mouse_data)
            game_data = stages.tp_elemento_tabla.game(mouse_data, game_data, grid, grid_data)
            stage = game_data[0]

            pygame.display.update()
            clock.tick(60)
            
        while stage == 3: # ELEMENTO - SIMBOLO
            mouse_data = mouse_data_reader(mouse_data)
            game_data = stages.tp_simbolo_elemento_both.game(mouse_data, game_data, grid, grid_data)
            stage = game_data[0]

            pygame.display.update()
            clock.tick(60)
            
        while stage == 4: # SIMBOLO - ELEMENTO
            mouse_data = mouse_data_reader(mouse_data)
            game_data = stages.tp_simbolo_elemento_both.game(mouse_data, game_data, grid, grid_data)
            stage = game_data[0]

            pygame.display.update()
            clock.tick(60)

        while stage == 5: # GAME OVER
            mouse_data = mouse_data_reader(mouse_data)
            game_data = stages.tp_gameover.game_over(mouse_data, game_data, grid, grid_data)
            stage = game_data[0]

            pygame.display.update()
            clock.tick(60)
            pass
