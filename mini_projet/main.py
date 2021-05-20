
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

WIDTH = 800
HEIGHT = 600
score = 0
player = Actor("joueur")
player.pos = [550, 550]
kunai = Actor("kunai")
fruit1 = Actor("fruit1")
bombe = Actor("bombe")

all_fruits = []
all_bombs = []

def draw():
    screen.clear()
    background.draw()
    fruit_score.draw()
    player.draw()

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]


#collide


#compteur de score 

# Hello c'est marie
# Hello c'est daria - collision du kunai avec fruit et bombe




#COLLISION FRUIT + KUNAI ET BOMBE + KUNAI

def draw():

    screen.clear()
    player.draw()
    screen.draw.text(str(score), (550, 590))

    
    if kunai != None:
        kunai.draw()

    if fruit1 != None:
        fruit1.draw()
    
for fruit1 in all_fruits:
    if kunai.colliderect(fruit1):
        fruit1.remove()
        kunai.remove()
        score +=1 
    
for bombe in all_bombs:
    if kunai.colliderect(bombe):
        bombe.remove()
        kunai.remove()
    #if bombe.colliderect(joueur):
