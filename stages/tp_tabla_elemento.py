import pygame
import tabla_periodica as tp
import random as r

table_pos = tp.SX*.12, (tp.SY-tp.SX*.42)-tp.SY*.06
sq = int((tp.SX*.76/18 +.5)*0.9)
gap = int((tp.SX*.76/18 +.5)*0.1)

t_background = tuple(50 for x in range(3))

sq_colors = [[255 for x in range(3)],
             [ 27, 242,  37],
             [255,  50,  55],
             [100 for x in range(3)],
             [  0, 110, 155],]

nom_or_sim = lambda a: "nombre" if a == 0 else "simbolo"
cword_cursor = lambda cword, t: cword+"_" if (t//60)%2==0 else cword

def game(mouse_data: list, game_data: list, grid: list[list], grid_data: list) -> list:
    # DATA
    mouse_pos, mouse_save, mouse = mouse_data
    stage, game_mode, dificulty, nom_sim, element, t, cword = game_data
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stage = None
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.dict['unicode'] == '\x1b':
                stage = 0
            elif event.dict['unicode'] == "\x08" and len(cword) > 0:
                cword = cword[0:-1]
            elif event.dict['unicode'].isalpha() and len(cword) < 15:
                cword += event.dict['unicode']
            elif event.dict['unicode'] == "\r":
                if tp.normalize_words(element[nom_sim+1]) == tp.normalize_words(cword):
                    new_state = 1
                else:
                    new_state = 2
                    
                grid[element[3][0]][element[3][1]][4] = new_state
                grid_data[element[0]-1][4] = new_state
                element = [None]
                cword = ""
            
    # FUNCIONAMIENTO
    t+=1
    attempts = 0
    while element == None or element == [None]:
        attempts += 1
        element = tp.dificultades[game_data[2]][r.randint(0, len(tp.dificultades[game_data[2]])-1)]
        if grid_data[element-1][4] != 0:
            element = [None]
        else:
            element = grid_data[element-1]
            
        if attempts > 10_000:
            stage = 5
            element = [None]
            break

    # EVENTOS
    if mouse and not mouse_save:
        if tp.SX*.84  < mouse_pos[0] < tp.SX*.84 + tp.SY*.1 and \
           tp.SY*.045 < mouse_pos[1] < tp.SY*.135:
            element = [None]
                       
    tp.screen.fill("white")
    
    # pygame.draw.rect(tp.screen, t_background, (*table_pos, tp.SX*.8, tp.SX*.44))
    pygame.draw.rect(tp.screen, t_background, (table_pos[0]-gap + (sq + gap)*0,  table_pos[1]-gap + (sq + gap)*0, sq*1  + gap*2,  sq*7 + gap*8)) # ALCALINOS
    pygame.draw.rect(tp.screen, t_background, (table_pos[0]-gap + (sq + gap)*1,  table_pos[1]-gap + (sq + gap)*1, sq*1  + gap*2,  sq*6 + gap*7)) # ALCALINOS TERREOS
    pygame.draw.rect(tp.screen, t_background, (table_pos[0]-gap + (sq + gap)*2,  table_pos[1]-gap + (sq + gap)*3, sq*10 + gap*11, sq*4 + gap*5)) # TRANSICION
    pygame.draw.rect(tp.screen, t_background, (table_pos[0]-gap + (sq + gap)*12, table_pos[1]-gap + (sq + gap)*1, sq*5  + gap*6,  sq*6 + gap*7)) # NO METALES
    pygame.draw.rect(tp.screen, t_background, (table_pos[0]-gap + (sq + gap)*17, table_pos[1]-gap + (sq + gap)*0, sq*1  + gap*2,  sq*7 + gap*8)) # GASES NOBLES
    pygame.draw.rect(tp.screen, t_background, (table_pos[0]-gap + (sq + gap)*2,  table_pos[1]-gap + (sq + gap)*8, sq*15 + gap*16, sq*2 + gap*3)) # LANTANIDOS Y ACTINIDOS
    
    for yy, y in enumerate(grid):
        for xx, x in enumerate(y):
            if x != None:
                if x[0] == element[0]: 
                    pygame.draw.rect(tp.screen, sq_colors[4],    (table_pos[0] + xx*sq + (xx)*gap, table_pos[1] + yy*sq + (yy)*gap, sq, sq))
                else:
                    pygame.draw.rect(tp.screen, sq_colors[x[4]], (table_pos[0] + xx*sq + (xx)*gap, table_pos[1] + yy*sq + (yy)*gap, sq, sq))
    
                if x[4] != 3:
                    z_txt = tp.font[3].render(str(x[0]), True, tuple(50 for x in range(3)))
                    tp.screen.blit(z_txt, (table_pos[0] + xx*sq + (xx+.8)*gap, table_pos[1] + yy*sq + (yy+.8)*gap))
                if x[4] in (1, 2):
                    simbol_txt = tp.font[2].render(x[2], True, tuple(50 for x in range(3)))
                    tp.screen.blit(simbol_txt, simbol_txt.get_rect(center = (table_pos[0] + (xx+.5)*sq + (xx)*gap, table_pos[1] + (yy+.5)*sq + (yy)*gap)))
    
    cword_txt = tp.font[0].render(cword_cursor(cword, t), True, tuple(50 for x in range(3)))
    tp.screen.blit(cword_txt,(tp.SX*.12- gap, tp.SY*0.04))
    
    pygame.draw.rect(tp.screen, tuple(50 for x in range(3)), (tp.SX*.84, tp.SY*0.045, tp.SY*.10, tp.SY*.09), border_radius=int(tp.SY*.02))
    
    next_txt = tp.font[0].render(">", True, "white")
    tp.screen.blit(next_txt, next_txt.get_rect(topright = (tp.SX*.883, tp.SY*0.04)))
    
    t_txt = tp.font[1].render(tp.time_format(t), True, tuple(50 for x in range(3)))
    tp.screen.blit(t_txt, t_txt.get_rect(topright = (tp.SX*.82, tp.SY*0.06)))
    
    hint_txt = tp.font[3].render(
        f"Escribir el {nom_or_sim(nom_sim)} del elemento señalado, tocar ENTER para confirmar. Si no lo sabe puede tocar la flecha para saltarlo.", True, tuple(50 for x in range(3)))
    tp.screen.blit(hint_txt, hint_txt.get_rect(topleft = (tp.SX*.12, tp.SY*0.965)))
    
    if element == [None]:
        element = None
    return stage, game_mode, dificulty, nom_sim, element, t, cword