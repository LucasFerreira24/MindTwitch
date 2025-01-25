# Ajusta a posição de um objeto baseado na resolução da tela atual e na tela de referência.
# :param reference_pos: Posição de referência na tela projetada.
# :param screen_size: Dimensões atuais da tela.
# :param screen_reference: Dimensões da tela de referência.
# :return: Nova posição ajustada para a tela atual.

def calc_pos_objects(reference_pos: tuple, screen_size: tuple, screen_reference: tuple):
    return (
        int(reference_pos[0] * screen_size[0] / screen_reference[0]),  # x
        int(reference_pos[1] * screen_size[1] / screen_reference[1])   # y
    )