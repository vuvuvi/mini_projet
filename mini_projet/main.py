# Hello c'est marie
# Hello c'est daria - collision du kunai avec fruit et bombe


kunai = Actor("kunai")
fruit1 = Actor("fruit1")
bombe = Actor("bombe")

all_fruits = []
all_bombs = []

def draw():

    if kunai != None:
        kunai.draw()

    if fruit1 != None:
        fruit1.draw()
    
for fruit1 in all_fruits:
    if kunai.colliderect(fruit1):
        fruit1.remove()
    
for bombe in all_bombs:
    if kunai.colliderect(bombe):
        bombe.remove()

    


            