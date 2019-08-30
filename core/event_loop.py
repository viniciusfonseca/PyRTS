import pygame
from core.app_state import app_state
from core.select_objects import select_objects
from core.command_units import command_units
from core.modes import Modes
from core.quit import quit

def game():
    global app_state
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                quit()
        elif event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (leftclick, middleclick, rightclick) = pygame.mouse.get_pressed()
            mouse_pos = tuple(x/app_state.scaling_factor for x in pygame.mouse.get_pos())
            if leftclick:
                app_state.selecting = True
                app_state.select_origin = mouse_pos
            elif rightclick:
                command_units(mouse_pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            (leftclick, middleclick, rightclick) = pygame.mouse.get_pressed()
            if app_state.selecting and not leftclick:
                app_state.selecting = False
                second_select_rect_pos = tuple(x/app_state.scaling_factor for x in pygame.mouse.get_pos())
                select_objects(app_state.select_origin, second_select_rect_pos)

def ui():
    pass

def event_loop():
    global modes
    if app_state.mode == Modes.GAME:
        game()
    elif app_state.mode == Modes.UI:
        ui()
