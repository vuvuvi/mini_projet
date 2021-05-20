
from random import randint

WIDTH = 800
HEIGHT = 600
background = Actor("background")
background.pos = [400, 300]
game_over_screen = Actor("game_over")
game_over_screen.pos = [400, 300]
fruit_score = Actor("fruit1_score")
fruit_score.pos = [720,50]
score = 0
player = Actor("joueur")
player.pos = [550, 550]
kunai = Actor("kunai")
fruit1 = Actor("fruit1")
bombe = Actor("bombe")

game_over = False

all_fruits = []
all_bombs = []
kunai_speed = [0, 3]
all_kunai = []


def draw():
    screen.clear()
    background.draw()
    fruit_score.draw()
    player.draw()
    screen.draw.text(str(score), (720, 45))
    
    if kunai != None:
        kunai.draw()

    if fruit1 != None:
        fruit1.draw()

    if game_over:
        game_over_screen.draw()

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]


def on_mouse_down(pos):
    print ("Click")
    kunai.draw()
    kunai.pos = player.pos


def update(dt):
    global game_over
    global fruit1

    new_x = kunai.pos [0] + kunai_speed [0]
    new_y = kunai.pos [1] + kunai_speed [1]

    kunai.pos = [new_x, new_y]
    
    for fruit1 in all_fruits:
        if kunai.colliderect(fruit1):
            fruit1.remove()
            kunai.remove()
            score +=1 
        
    for bombe in all_bombs:
        if kunai.colliderect(bombe):
            bombe.remove()
            kunai.remove()
        if player.colliderect(bombe) and not game_over:
                game_over = True

    if fruit1.bottom > HEIGHT and not game_over:
        #sounds.game_over_fart.play()
        game_over = True



    
    


