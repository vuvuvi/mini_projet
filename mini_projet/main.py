# Hello c'est marie

from random import randint

WIDTH = 800
HEIGHT = 600

player = Actor ("joueur")
player.pos = [520, 500]

kunai = Actor ("kunai")
kunai_speed = [0, 3]
all_kunai = []

def draw():
    screen.clear()
    player.draw()

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]


def on_mouse_down(pos):
    print ("Click")
    kunai.draw()
    kunai.pos = player.pos


def update(dt):

    new_x = kunai.pos [0] + kunai_speed [0]
    new_y = kunai.pos [1] + kunai_speed [1]

    kunai.pos = [new_x, new_y]
