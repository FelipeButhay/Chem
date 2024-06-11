import pygame
import tabla_periodica as tp
import math

dificultades_nombre = ["FACIL", "NORMAL", "DIFICL", "COMPLETA"]

table_pos = tp.SX*.6, tp.SY*.22
sq = int((tp.SX*.35/18 +.5)*0.9)
gap = int((tp.SX*.35/18 +.5)*0.1)

t_background = tuple(50 for x in range(3))

sq_colors = [[255 for x in range(3)],
             [ 27, 242,  37],
             [255,  50,  55],
             [100 for x in range(3)]]

hover = lambda r_value, m_pos: 120 if r_value[0] < m_pos[0] < r_value[0]+r_value[2] and \
                                      r_value[1] < m_pos[1] < r_value[1]+r_value[3] else 50

button_rect = table_pos[0], tp.SY*.74, tp.SX*.35, tp.SY*.16

def game_over(mouse_data: list, game_data: list, grid: list, grid_data:list) -> list:
    # DATA
    mouse_pos, mouse_save, mouse = mouse_data
    stage, game_mode, dificulty, nom_sim, element, t, cword = game_data
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stage = None
            pygame.quit()
            exit()
    
    if mouse and not mouse_save:
        if hover(button_rect, mouse_pos) == 120:
            stage = 0
    
    right = 0
    total = len(tp.dificultades[dificulty])
    for x in grid_data:
        if x[4] == 1:
            right += 1
    
    match game_mode:
        case 0: # ESCRIBIR
            if nom_sim == 0: # NOMBRE
                score = 3*(60*8100*(right/total)*(3**math.log2(dificulty+1)))/t
            elif nom_sim == 1: # SIMBOLO
                score = 1.5*(60*8100*(right/total)*(3**math.log2(dificulty+1)))/t
        case 1: # SEÑALAR EN LA TABLA
            score = (60*8100*(right/total)*(3**math.log2(dificulty+1)))/t
        
    tp.screen.fill("white")
    
    t_txt = tp.font[0].render("Fin del Juego", True, tuple(50 for x in range(3)))
    tp.screen.blit(t_txt, t_txt.get_rect(midleft = (tp.SX*.06, tp.SY*0.12)))
    
    pygame.draw.rect(tp.screen, tuple(50 for x in range(3)), (tp.SX*.06, tp.SY*.22, tp.SX*.5, tp.SY*.46))
    
    t_txt = tp.font[1].render(f"Respuestas: {right}/{total}", True, tuple(255 for x in range(3)))
    tp.screen.blit(t_txt, t_txt.get_rect(midleft = (tp.SX*.1, tp.SY*0.3)))
    
    t_txt = tp.font[1].render(f"Tiempo:     {tp.time_format(t)}", True, tuple(255 for x in range(3)))
    tp.screen.blit(t_txt, t_txt.get_rect(midleft = (tp.SX*.1, tp.SY*0.45)))
    
    t_txt = tp.font[1].render(f"Dificultad: {dificultades_nombre[dificulty]}", True, tuple(255 for x in range(3)))
    tp.screen.blit(t_txt, t_txt.get_rect(midleft = (tp.SX*.1, tp.SY*0.6)))
    
    t_txt = tp.font[1].render(f"Puntaje:    {int(score)}", True, tuple(50 for x in range(3)))
    tp.screen.blit(t_txt, t_txt.get_rect(midleft = (tp.SX*.1, tp.SY*0.82)))
    
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
                
    pygame.draw.rect(tp.screen, tuple(hover(button_rect, mouse_pos) for x in range(3)), button_rect)
    
    t_txt = tp.font[1].render(f"Voler al Menu", True, tuple(255 for x in range(3)))
    tp.screen.blit(t_txt, t_txt.get_rect(center = (table_pos[0] + tp.SX*.35/2, tp.SY*.74 + tp.SY*.16/2)))
    
    return stage, game_mode, dificulty, nom_sim, element, t, cword