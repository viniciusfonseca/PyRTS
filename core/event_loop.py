import pygame
from core.app_state import app_state
from core.quit import quit

def event_loop():
    global app_state
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                quit()
        elif event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (leftclick, middleclick, rightclick) = pygame.mouse.get_pressed()
            if leftclick:
                app_state.selecting = True
            app_state.select_origin = tuple(x/app_state.scaling_factor for x in pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            (leftclick, middleclick, rightclick) = pygame.mouse.get_pressed()
            if not leftclick:
                app_state.selecting = False