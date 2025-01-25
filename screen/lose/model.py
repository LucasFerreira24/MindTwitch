class Model:
    def __init__(self, screen):
        self.screen = screen

    def advance_state_screen(self):
        self.screen.state = 'screen.endgame'