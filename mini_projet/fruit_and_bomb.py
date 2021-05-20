from random import randint

WIDTH = 800
HEIGHT = 600

random_x=randint(0,800)
time_object = 1
nbr_object = 100
all_fruit = []
all_bombe = []




# if random_object ==0:
#     bombe.pos = [random_x, 0]
# else:
#     fruit.pos = [random_x,0]


def draw():
    screen.clear()
    for bombe in all_bombe:
        bombe.draw()
    for fruit in all_fruit:
        fruit.draw()

def update(dt):
    global time_object
    global nbr_object

    if time_object <= 0:
        time_object = 1
        random_x=randint(0,800)
        random_object = randint(1,2)
        if random_object == 2:
            fruit = Actor("fruit1")
            fruit.pos = [random_x,-100]
        elif random_object == 1:
            bombe = Actor("bombe")
            bombe.pos= [random_x,-100]
        
    if time_object <=0 and nbr_object > 0:
        

        for bombe in all_bombe:
            bombe = Actor("bombe")
            bombe_speed = [0,100]
            new_x = bombe.pos[0] + bombe_speed[0]
            new_y = bombe.pos[1] + bombe_speed[1]
            nbr_object -= 1

            bombe.pos = [new_x, new_y]
            all_bombe.append(bombe)

        
        for fruit in all_fruit:
            fruit = Actor("fruit1")
            fruit_speed = [0,100]
            new_x = fruit.pos[0] + fruit_speed[0]
            new_y = fruit.pos[1] + fruit_speed[1]

            fruit.pos = [new_x, new_y]
            nbr_object -= 1
            all_fruit.append(fruit)
    time_object -= dt
        

    


    
    
    