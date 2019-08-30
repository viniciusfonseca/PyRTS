import math
import pygame
from pygame.locals import *
from core.app_state import app_state
from core.game_object import GameObject
from core.sign import sign

class Unit(GameObject):

    walking = False
    target = (None, None)
    life = 0
    max_life = 0
    selected = False
    selecting = False
    speed = 3

    def __init__(self, position: tuple((int, int)), max_life: int):
        super().__init__(position)
        self.life = self.max_life = max_life

    def render(self):
        global app_state

        if not self.selecting and app_state.selecting:
            rect = self.get_clickable_region()
            self.selected = self.selecting = rect.collidepoint(app_state.select_origin)
        elif self.selecting:
            self.selected = True
            self.selecting = False

        if self.walking:
           self.walk()

        if not self.selected:
            return

        (x, y) = self.position
        pygame.draw.ellipse(
            app_state.screen,
            (255, 255, 255),
            (
                (x - 12, y),
                (24, 12)
            ), 1
        )

    def walk(self):
        (x, y) = self.position
        (tx, ty) = self.target
        (sx, sy) = (tx - x, ty - y)
        (sigx, sigy) = (sign(sx), sign(sy))
        (dx, dy) = (
            sigx * self.speed,
            sigy * self.speed)
        (cmpx, cmpy) = (
            max if sigx == -1 else min,
            max if sigy == -1 else min)
        (nx, ny) = (
            x + cmpx(dx, sx),
            y + cmpy(dy, sy))
        self.position = (nx, ny)
        self.walking = nx != tx or ny != ty

    def get_clickable_region(self) -> pygame.rect.Rect:
        (x, y) = self.position
        rect = pygame.rect.Rect(x - 8, y - 22, 16, 28)
        return rect

    def show_lifebar(self):
        if not self.selected:
            return
            
        global app_state
        (x, y) = self.position
        pygame.draw.rect(
            app_state.screen,
            (255, 255, 255),
            (
                (x - 12, y - 28),
                (24, 4)
            ), 1
        )
        max_life_width = 24 - 2
        pygame.draw.rect(
            app_state.screen,
            (0, 255, 0),
            (
                (x - 12 + 1, y - 28 + 1),
                (max_life_width, 2)
            )
        )