import pygame
from pygame.locals import *
from typing import List, Tuple
from core.modes import Modes

screen_width, screen_height = 400, 300
scaling_factor = 2

class AppState():
    mode = None
    screen = pygame.Surface((screen_width, screen_height))
    window = pygame.display.set_mode((
        screen_width * scaling_factor,
        screen_height * scaling_factor
    ))
    select_origin = (None, None) # type: Tuple[int, int]
    selecting = False
    running = True
    screen_width = screen_width
    screen_height = screen_height
    scaling_factor = scaling_factor
    objects = [] # type: List[GameObject]
    selected = [] # type: List[Unit]
    
app_state = AppState()