"""
TODO:
    - AI Controller Input Nodes
    - AI Graph class
    - AI Controller Output Nodes
"""
import pygame

import ai_controller as ai
import game_runner


if __name__ == '__main__':
    g = game_runner.Game('map.csv')
    for _ in range(100):
        print(g.run(player_controller=ai.AIController, config={'has_boosts': True,
                                                               'has_ghosts': True,
                                                               'is_visual': True,
                                                               'is_debug': True}))

    pygame.display.quit()
    pygame.quit()
