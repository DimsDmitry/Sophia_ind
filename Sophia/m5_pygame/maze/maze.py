from pygame import *

# окно игры
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')
# фон сцены
background = transform.scale(image.load('background.jpg'), (win_width, win_height))
