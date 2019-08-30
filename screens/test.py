import pygame
from pygame.locals import *
from core.app_state import app_state
from core.unit import Unit
from core.modes import Modes

class CustomUnit(Unit):

    def __init__(self, position):
        super().__init__(position, 100)

    def render(self):
        super().render()

        (x, y) = self.position

        pygame.draw.rect(
            app_state.screen,
            (255, 255, 0),
            ((x - 8, y - 22), (16, 28))
        )

        super().show_lifebar()

def test_screen():
    app_state.mode = Modes.GAME
    CustomUnit((200, 150))
    CustomUnit((100, 150))
    CustomUnit((100, 100))
    CustomUnit((200, 100))