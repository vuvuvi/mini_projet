# Hello c'est marie

from random import randint

WIDTH = 800
HEIGHT = 600

player = Actor ("joueur", anchor = ["right", "top"] )
player.pos = [520, 500]

kunai_speed = [0, - 3]
all_kunai = []

def draw():
    screen.clear()
    player.draw()

    for kunai in all_kunai:
        kunai.draw()

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]

def on_mouse_down(pos):
    print ("Click")
    kunai = Actor ("kunai", anchor = ["right", "bottom"])
    kunai.pos = player.pos
    all_kunai.append(kunai)

def update(dt):
    dt += 1
    for kunai in all_kunai:
        new_x = kunai.pos [0] + kunai_speed [0]
        new_y = kunai.pos [1] + kunai_speed [1]
        kunai.pos = [new_x, new_y]

