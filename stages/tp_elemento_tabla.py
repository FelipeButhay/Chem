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
             [100 for x in range(3)]]

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
            
    # FUNCIONAMIENTO
    t+=1
    attempts = 0
    while element == None:
        attempts += 1
        element = tp.dificultades[game_data[2]][r.randint(0, len(tp.dificultades[game_data[2]])-1)]
        if grid_data[element-1][4] != 0:
            element = None
        else:
            element = grid_data[element-1]
            
        if attempts > 10_000:
            stage = 5
            break

    # EVENTOS
    if mouse and not mouse_save:
        if tp.SX*.84 < mouse_pos[0] < tp.SX*.84 + tp.SY*.10 and \
           tp.SY*0.045 < mouse_pos[1] < tp.SY*0.135:
            element = None
        
        for yy, y in enumerate(grid):
            for xx, x in enumerate(y):
                if table_pos[0] + xx*sq + (xx)*gap < mouse_pos[0] < table_pos[0] + (xx+1)*sq + (xx+1)*gap and \
                   table_pos[1] + yy*sq + (yy)*gap < mouse_pos[1] < table_pos[1] + (yy+1)*sq + (yy+1)*gap and \
                   x != None and x[4] == 0:

                    if x == element:
                        new_state = 1
                    else:
                        new_state = 2
                    grid[element[3][0]][element[3][1]][4] = new_state
                    grid_data[element[0]-1][4] = new_state
                            
                    element = None
                    break
            if element == None:
                break
                       
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
                pygame.draw.rect(tp.screen, sq_colors[x[4]], (table_pos[0] + xx*sq + (xx)*gap, table_pos[1] + yy*sq + (yy)*gap, sq, sq))
                if x[4] != 3:
                    z_txt = tp.font[3].render(str(x[0]), True, tuple(50 for x in range(3)))
                    tp.screen.blit(z_txt, (table_pos[0] + xx*sq + (xx+.8)*gap, table_pos[1] + yy*sq + (yy+.8)*gap))
                if x[4] in (1, 2):
                    simbol_txt = tp.font[2].render(x[2], True, tuple(50 for x in range(3)))
                    tp.screen.blit(simbol_txt, simbol_txt.get_rect(center = (table_pos[0] + (xx+.5)*sq + (xx)*gap, table_pos[1] + (yy+.5)*sq + (yy)*gap)))
    
    if element != None: 
        element_txt = tp.font[0].render(element[nom_sim+1], True, tuple(50 for x in range(3)))
        tp.screen.blit(element_txt,(tp.SX*.12- gap, tp.SY*0.04))
    
    pygame.draw.rect(tp.screen, tuple(50 for x in range(3)), (tp.SX*.84, tp.SY*0.045, tp.SY*.10, tp.SY*.09), border_radius=int(tp.SY*.02))
    
    next_txt = tp.font[0].render(">", True, "white")
    tp.screen.blit(next_txt, next_txt.get_rect(topright = (tp.SX*.883, tp.SY*0.04)))
    
    t_txt = tp.font[1].render(tp.time_format(t), True, tuple(50 for x in range(3)))
    tp.screen.blit(t_txt, t_txt.get_rect(topright = (tp.SX*.82, tp.SY*0.06)))
    
    hint_txt = tp.font[3].render("Ubicar el elemento nombrado en la tabla, si no lo sabe puede tocar la flecha para saltarlo.", True, tuple(50 for x in range(3)))
    tp.screen.blit(hint_txt, hint_txt.get_rect(topleft = (tp.SX*.12, tp.SY*0.965)))
    
    return stage, game_mode, dificulty, nom_sim, element, t, cword