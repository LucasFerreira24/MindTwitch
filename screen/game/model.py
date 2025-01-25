from shared.save_user_data import save_user_data


class Model:
    def __init__(self, screen):
        self.screen = screen

    def compare_sequence_game(self, game, object_rect):
        expected_object = game.order_choosing_game_objects[game.current_sequence_index]

        if object_rect == expected_object.rect:
            game.current_sequence_index += 1
        else:
            game.current_sequence_index = 0
            self.advance_state_screen(game=game)

        if game.current_sequence_index == len(game.order_choosing_game_objects):
            game.next_level()

    def save_data_game(self, game):
        file_path = 'data/json/user_points.json'
        points = game.get_level() * 10
        save_user_data(file_path=file_path, points=points)

    def advance_state_screen(self, game):
        self.save_data_game(game=game)
        self.screen.state = 'screen.lose'

    def close_game(self):
        self.screen.state = 'screen.endgame'