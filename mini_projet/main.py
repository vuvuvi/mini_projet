#Hello c'est marie

#affichage écran
WIDTH = 800
HEIGHT = 600
background = Actor("background")
background.pos = [400, 300]
fruit_score = Actor("fruit1_score")
fruit_score.pos = [720,50]


#Hello c'est Reshma 

from random import randint


player = Actor("joueur")
player.pos = [550, 550]

def draw():
    screen.clear()
    background.draw()
    fruit_score.draw()
    player.draw()

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]


#collide

#compteur de score 

#screen.draw.text("hello world", (20, 100))