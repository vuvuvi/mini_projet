
from random import randint
import time 

WIDTH = 800
HEIGHT = 600

player = Actor ("joueur", anchor = ["right", "top"] )
player.pos = [520, 500]

kunai_speed = [0, - 3]
all_kunai = []
time_kunai = 10
last_kunai = time.time()

def draw():
    screen.clear()
    player.draw()

    for kunai in all_kunai:
        kunai.draw()

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]

def on_mouse_down(pos):
    global last_kunai
    print ("Click")
    if time.time() - last_kunai > 0.35:
        last_kunai = time.time()
        kunai = Actor ("kunai", anchor = ["right", "bottom"])
        kunai.pos = player.pos
        all_kunai.append(kunai)

def update(dt):
    global kunai 

    for kunai in all_kunai:
        new_x = kunai.pos [0] + kunai_speed [0]
        new_y = kunai.pos [1] + kunai_speed [1]
        kunai.pos = [new_x, new_y]

        if kunai.top <= 0:
            all_kunai.remove(kunai)

