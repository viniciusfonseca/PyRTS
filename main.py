import pygame
from core.event_loop import event_loop
from core.app_state import app_state
from core.render import render

pygame.init()

while app_state.running:
    render()
    event_loop()

pygame.quit()