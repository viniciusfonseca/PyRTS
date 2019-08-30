import pygame
from core.app_state import app_state

def select_objects(
    primary_rect_pos: tuple((int, int)),
    secundary_rect_pos: tuple((int, int))):

    (x1, y1) = primary_rect_pos
    if x1 is None or y1 is None:
        return

    (x2, y2) = secundary_rect_pos
    select_region = pygame.rect.Rect(x1, y1, x2 - x1, y2 - y1)

    app_state.selected = []

    for obj in app_state.objects:
        if len(app_state.selected) >= 10:
            break
        if select_region.colliderect(obj.get_clickable_region()):
            obj.selected = True
            app_state.selected.append(obj)