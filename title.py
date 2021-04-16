import pygame
import pygame_menu
import game_runner
from game_constants import SCREEN_SIZE

#Windows
import settings
import ai_play_menu
import ai_train_menu

high_score = 0

height = SCREEN_SIZE[0]
width = SCREEN_SIZE[1]

pygame.init()
surface = pygame.display.set_mode((height, width))

game = game_runner.Game('data/map.csv')

def start_the_game():
    global high_score
    score = game.run(seed= settings.seed,config={'is_debug': settings.debug_option})['score']
    if score >= high_score:
        high_score = score
        high_label.set_title('High Score: ' + str(high_score))

def ai_play_window():
    ai_play_menu.menu.mainloop(surface)

def ai_train_window():
    ai_train_menu.menu.mainloop(surface)

def settings_window():
    settings.menu.mainloop(surface)

menu = pygame_menu.Menu(width, height, 'PAC-MAN',
                        theme=pygame_menu.themes.THEME_DARK)

high_label = menu.add.label('High Score: ' + str(high_score))
menu.add.button('Play', start_the_game)
menu.add.button('AI Play', ai_play_window)
menu.add.button('AI Train', ai_train_window)
menu.add.button('Settings', settings_window)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)