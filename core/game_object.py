from core.app_state import app_state

class GameObject:

    position = (None, None) # type: tuple((int, int))
    
    def __init__(self, position: tuple((int, int))):
        global app_state
        self.position = position
        app_state.objects.append(self)

    def render(self):
        pass

    def __del__(self):
        global app_state
        app_state.objects.remove(self)