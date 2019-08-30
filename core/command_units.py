import math
from core.app_state import app_state

def square_formation(target: (int, int), num_obj: int):
    (tx, ty) = target
    (sx, sy) = (0, 0)
    for obj in app_state.selected:
        (x, y) = obj.position
        (sx, sy) = (sx + x, sy + y)
    (cx, cy) = (sx / num_obj, sy / num_obj)
    ang_sign = False
    even = num_obj % 2 == 0
    def swap_sign():
        global ang_sign
        ang_sign = not ang_sign
    (dx, dy) = (tx - cx, ty - cy)
    travel_angle = math.atan2(dy, dx)
    selected = app_state.selected.copy()
    gap = 5
    if not even:
        obj = selected.pop(0)
        obj.walking = True
        obj.target = target
        gap = 10
    count = 0
    for obj in app_state.selected:
        (otx, oty) = (
            tx * math.cos(travel_angle) - ty * math.sin(travel_angle),
            ty * math.cos(travel_angle) + tx * math.sin(travel_angle))

def command_units(position: (int, int)):
    global app_state
    num_obj = len(app_state.selected)
    if num_obj == 0:
        return
    elif num_obj == 1:
        obj = app_state.selected[0]
        obj.walking = True
        obj.target = position
    else:
        square_formation(position, num_obj)