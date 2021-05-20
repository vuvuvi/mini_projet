#Hello c'est marie
#Hello c'est Reshma 

from random import randint


player = Actor("joueur")
player.pos = [550, 550]

def draw():
    screen.clear()
    player.draw()

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]


#collide

#compteur de score 

#screen.draw.text("hello world", (20, 100))