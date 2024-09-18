from pygame import *

# создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
# задай фон сцены
background = transform.scale(image.load('background.png'), (700, 500))
# создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
x1 = 100
y1 = 300

x2 = 300
y2 = 300

speed = 10

# игровой цикл
run = True
clock = time.Clock()

while run:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()

    # управление 1м персонажем
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 600:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 400:
        y1 += speed

    # управление 2м персонажем
    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 600:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 400:
        y2 += speed

    display.update()
    clock.tick(60)
