import pygame
from core.app_state import app_state

fps = 50
clock = pygame.time.Clock()

def render():
    global app_state
    clock.tick(fps)

    app_state.screen.fill((0, 0, 0))

    for obj in app_state.objects:
        obj.render()

    if app_state.selecting:
        (m_x, m_y) = tuple(x/app_state.scaling_factor for x in pygame.mouse.get_pos())
        (o_x, o_y) = app_state.select_origin
        pygame.draw.rect(
            app_state.screen,
            (255, 255, 255),
            (app_state.select_origin, (m_x - o_x, m_y - o_y)), 1
        )

    app_state.window.blit(
        pygame.transform.scale(
            app_state.screen,
            app_state.window.get_rect().size), (0, 0))
    pygame.display.update()