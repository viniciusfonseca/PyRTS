import pygame
from core.event_loop import event_loop
from core.app_state import app_state
from core.render import render

from screens.test import test_screen

pygame.init()
pygame.display.set_caption('PyRTS')

test_screen()

while app_state.running:
    render()
    event_loop()

pygame.quit()