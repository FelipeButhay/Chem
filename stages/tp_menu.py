import pygame
import tabla_periodica as tp

def menu(mouse_data: list, game_data: list) -> list:
    # DATA
    mouse_pos, mouse_save, mouse = mouse_data
    stage, game_mode, dificulty, nom_sim, element, t, cword = game_data
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stage = None
            pygame.quit()
            exit()
    
    if mouse and not mouse_save:
        # SELECTOR ENTRE SIMBOLO Y NOMBRE 
        if tp.SX*.50 < mouse_pos[0] < tp.SX*.94 and \
           tp.SY*.06 < mouse_pos[1] < tp.SY*.16:
            nom_sim = not nom_sim
    
        #EMPEZAR EL JUEGO
        if tp.SX*.06 < mouse_pos[0] < tp.SX*.45 and \
           tp.SY*.06 < mouse_pos[1] < tp.SY*.20:
            stage = game_mode + 1
    
        # MODO
        for x in range(2):
            if tp.SX*.12 < mouse_pos[0] < tp.SX*.5 and \
               tp.SY*(.335 + .12*x) < mouse_pos[1] < tp.SY*(.435 + .12*x):
                game_mode = x
                break
        
        # DIFICULTAD
        for x in range(4):
            if tp.SX*.56 < mouse_pos[0] < tp.SX*.94 and \
               tp.SY*(.335 + .12*x) < mouse_pos[1] < tp.SY*(.435 + .12*x):
                dificulty = x
                break
    
    # FONDO Y TITULO
    tp.screen.fill("white")
    
    pygame.draw.rect(tp.screen, tuple(50 for x in range(3)), (tp.SX*.06, tp.SY*.06, tp.SX*.39, tp.SY*.12))
    title_txt = tp.font[0].render("Lorem Ipsum", True, tuple(255 for x in range(3)))
    tp.screen.blit(title_txt, (tp.SX*.075, tp.SY*.075))
    
    # SELECTOR ENTRE SIMBOLO Y NOMBRE
    pygame.draw.rect(tp.screen, tuple(50 for x in range(3)), (tp.SX*.50, tp.SY*.06, tp.SX*.44, tp.SY*.12))
    
    if nom_sim == 0:
        pygame.draw.rect(tp.screen, tuple(200 for x in range(3)), (tp.SX*.50, tp.SY*.06, tp.SX*.22, tp.SY*.12))
    else:
        pygame.draw.rect(tp.screen, tuple(200 for x in range(3)), (tp.SX*.72, tp.SY*.06, tp.SX*.22, tp.SY*.12))
    
    nombre_txt = tp.font[1].render("Nombre", True, tuple(50 for x in range(3)))
    tp.screen.blit(nombre_txt, (tp.SX*.53, tp.SY*.093))
    simbolo_txt = tp.font[1].render("Simbolo", True, tuple(50 for x in range(3)))
    tp.screen.blit(simbolo_txt, (tp.SX*.75, tp.SY*.093))
    
    # SELECTOR
    selector_txt = tp.font[1].render(">", True, tuple(50 for x in range(3)))
    
    # MODOS
    for xx, x in enumerate(["Tabla-Elemento", "Elemento-Tabla"]):
        # pygame.draw.rect(tp.screen, "red", (tp.SX*.12, tp.SY*(.335 + .12*xx), tp.SX*.38, tp.SY*.1))
        modes_txt = tp.font[1].render(x, True, tuple(50 for x in range(3)))
        tp.screen.blit(modes_txt, (tp.SX*.12, tp.SY*(.35 + .12*xx)))
        
    tp.screen.blit(selector_txt, (tp.SX*.08, tp.SY*(.35 + .12*game_mode)))

    # DIFICULTADES
    for xx, x in enumerate(["Facil", "Normal", "Dificil", "Completa"]):
        # pygame.draw.rect(tp.screen, "red", (tp.SX*.56, tp.SY*(.335 + .12*xx), tp.SX*.38, tp.SY*.1))
        dificulties_txt = tp.font[1].render(x, True, tuple(50 for x in range(3)))
        tp.screen.blit(dificulties_txt, (tp.SX*.56, tp.SY*(.35 + .12*xx)))
    
    tp.screen.blit(selector_txt, (tp.SX*.52, tp.SY*(.35 + .12*dificulty)))
    
    return stage, game_mode, dificulty, nom_sim, element, t, cword