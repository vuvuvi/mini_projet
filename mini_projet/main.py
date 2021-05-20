#Hello c'est marie
#Hello c'est Reshma 

from random import randint

score = 0
player = Actor("joueur")
player.pos = [550, 550]

def draw():
    screen.clear()
    player.draw()
    screen.draw.text(str(score), (550, 590))

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]


#collide


#compteur de score 


