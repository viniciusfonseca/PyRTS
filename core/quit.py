from core.app_state import app_state

def quit():
    global app_state
    app_state.running = False