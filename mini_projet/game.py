from random import randint

WIDTH = 800
HEIGHT = 600
#center = [400, 300]


#kick = pygame.mixer.Sound("kick")
music.play("feedback")
lines = 7
power_up_apparition = 20 
double_ball_apparition = 80
time_bigger_player = 0
time_double_ball = 0
#time_reboot = 0
time_play = 120
time_play_2 = 180


all_bricks = []
all_super_bricks = []
all_last_bricks = []
all_power_up_bigger_player = []
#all_new_ball = []
#all_list = [all_bricks, all_last_bricks, all_super_bricks]

game_over = Actor("game_over")
game_over.pos = [400, 300]
win = Actor("win")
win.pos = [400,300]
loose = False
player = Actor("player")
player.pos = [400, 550]

ball = Actor("ball")
ball.pos = [400, 500]
ball_speed = [3, -3]

power_up_speed = [0, 3]

new_ball = None
new_ball_speed = [-4, 4]

for x in range (0,800, 100):
    for y in range (0, 60, 30):
        last_brick = Actor("brick3", anchor= ["left", "top"])
        last_brick.pos = [x, y]
        all_last_bricks.append(last_brick)


for x in range(0, 800, 100):

    for y in range (60, 210, 30):
        brick = Actor("brick", anchor=["left", "top"])
        brick.pos = [x,y]
        all_bricks.append(brick)


for x in range (0, 800, 100):
    super_brick = Actor("brick2-1", anchor = ["left", "top"])
    super_brick.pos = [x, 30 * lines + 1]
    all_super_bricks.append(super_brick)

def reboot():
    global lines
    global power_up_apparition
    global double_ball_apparition
    global time_bigger_player
    global time_double_ball
    #global time_reboot
    global time_play

    global all_bricks
    global all_super_bricks
    global all_last_bricks
    global all_power_up_bigger_player
    global game_over
    global win
    global loose
    global player
    global ball
    global ball_speed
    global new_ball
    global new_ball_speed
    global power_up_apparition
    global power_up_speed
    global sounds
    global time_play_2
    
    music.play("feedback")
    lines = 7
    power_up_apparition = 20 
    double_ball_apparition = 80
    time_bigger_player = 0
    time_double_ball = 0
    #time_reboot = 0
    time_play = 120
    time_play_2 = 180


    all_bricks = []
    all_super_bricks = []
    all_last_bricks = []
    all_power_up_bigger_player = []
    #all_new_ball = []
    #all_list = [all_bricks, all_last_bricks, all_super_bricks]

    game_over = Actor("game_over")
    game_over.pos = [400, 300]
    win = Actor("win")
    win.pos = [400,300]
    loose = False
    player = Actor("player")
    player.pos = [400, 550]

    ball = Actor("ball")
    ball.pos = [400, 500]
    ball_speed = [3, -3]

    power_up_speed = [0, 3]

    new_ball = None
    new_ball_speed = [-4, 4]

    for x in range (0,800, 100):
        for y in range (0, 60, 30):
            last_brick = Actor("brick3", anchor= ["left", "top"])
            last_brick.pos = [x, y]
            all_last_bricks.append(last_brick)


    for x in range(0, 800, 100):

        for y in range (60, 210, 30):
            brick = Actor("brick", anchor=["left", "top"])
            brick.pos = [x,y]
            all_bricks.append(brick)


    for x in range (0, 800, 100):
        super_brick = Actor("brick2-1", anchor = ["left", "top"])
        super_brick.pos = [x, 30 * lines + 1]
        all_super_bricks.append(super_brick)
    
def on_key_down(key):
    if key == keys.SPACE:
        reboot()


def draw():
    screen.clear()
    #screen.draw.circle(center, 50, "blue")
    for brick in all_bricks:
        brick.draw()

    for super_brick in all_super_bricks:
        super_brick.draw()
    
    for last_brick in all_last_bricks:
        last_brick.draw()
    
    for power_up_bigger_player in all_power_up_bigger_player:
        power_up_bigger_player.draw()
    
    
    
    if new_ball != None:
        new_ball.draw()
            

    player.draw()
    ball.draw()

    if ball.bottom > HEIGHT:
        game_over.draw()
        sounds.bounce.stop()

    if all_bricks == [] and all_last_bricks == [] and all_super_bricks == []:
        #music.play("winner")
        sounds.bounce.stop()
        win.draw()
        



 


    #if all_bricks == []:
        #win.draw()
    
    
def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]

def invert_horizontal_speed():
    ball_speed[0] = ball_speed[0] * -1

def invert_horizontal_new_ball_speed():
    if new_ball != None:
        new_ball_speed[0] = new_ball_speed[0] * -1

def invert_vertical_speed():
    ball_speed[1] = ball_speed[1] * -1

def invert_vertical_new_ball_speed():
    if new_ball != None:
        new_ball_speed[1] = new_ball_speed[1] * -1


def upgrade_ball_speed(upgrade):
    if ball_speed[0] > 0:
        ball_speed[0] = ball_speed[0] + upgrade
    else:
        ball_speed[0] = ball_speed[0] - upgrade

    if ball_speed[1] > 0:
        ball_speed[1] = ball_speed[1] + upgrade
    else:
        ball_speed[1] = ball_speed[1] - upgrade
#def upgrade_ball_speed():
 #   global ball_speed
  #  ball_speed = [6, -6]

def update(dt):
    global time_bigger_player
    global player
    global ball
    global ball_speed
    global new_ball
    global new_ball_speed
    global time_double_ball
    global last_brick
    global all_last_bricks
    #global time_reboot
    global time_play
    global time_play_2

    if time_play > 0:
        time_play = time_play - dt
        
        if time_play <= 0:
            ball = Actor("ball_3", ball.pos)
            upgrade_ball_speed(1)
            
    if time_play_2 > 0:
        time_play_2 = time_play_2 - dt

        if time_play_2 <= 0:
            ball = Actor("ball_4", ball.pos)
            upgrade_ball_speed(1)

    if time_bigger_player > 0:
        time_bigger_player = time_bigger_player - dt

        if time_bigger_player <= 0:
            player = Actor("player", player.pos)
            ball = Actor("ball", ball.pos)
            upgrade_ball_speed(-2)
    
    if time_double_ball > 0:
        time_double_ball = time_double_ball - dt

        if time_double_ball <= 0:
            new_ball = None
    
    

    if new_ball != None:
        new_xx = new_ball.pos[0] + new_ball_speed[0]
        new_yy = new_ball.pos[1] + new_ball_speed[1]

        new_ball.pos = [new_xx, new_yy]

    new_x = ball.pos[0] + ball_speed[0]
    new_y = ball.pos[1] + ball_speed[1]

    ball.pos = [new_x, new_y]

    

    for power_up_bigger_player in all_power_up_bigger_player:
        new_x = power_up_bigger_player.pos[0] + power_up_speed[0]
        new_y = power_up_bigger_player.pos[1] + power_up_speed[1]

        power_up_bigger_player.pos = [new_x,new_y]


    if ball.right >= WIDTH or ball.left <= 0:
        sounds.bounce.play()
        invert_horizontal_speed()
    
    if new_ball != None:
        if new_ball.right >= WIDTH or new_ball.left <= 0:
            sounds.kick1.play()
            invert_horizontal_new_ball_speed()
    
    if ball.top <= 0:
        sounds.bounce.play()
        invert_vertical_speed()
    if new_ball != None and new_ball.top <= 0:
        sounds.bounce.play()
        invert_vertical_new_ball_speed()
    
    

    if ball.colliderect(player):
        sounds.bounce.play()
        if ball.pos[0] >= player.left and ball.pos[0] <= player.right:
            invert_vertical_speed()
        else:
            invert_horizontal_speed()

    if new_ball != None and new_ball.colliderect(player):
        sounds.bounce.play()
        if new_ball.pos[0] >= player.left and new_ball.pos[0] <= player.right:
            invert_vertical_new_ball_speed()
        else:
            invert_horizontal_new_ball_speed()
        
    
    for brick in all_bricks:
        if ball.colliderect(brick):
            sounds.kick1.play()
            all_bricks.remove(brick)
            invert_vertical_speed()
            
            



            rnd = randint(0, 100)

            if rnd <= power_up_apparition:
                power_up = Actor("powerup1", anchor=["left", "top"])
                power_up.pos = brick.pos
                all_power_up_bigger_player.append(power_up)

            if rnd >= double_ball_apparition:
                new_ball = Actor("new_ball")
                new_ball.pos = brick.pos
                time_double_ball = 6
                #all_new_ball.append(new_ball) 
            
        if new_ball != None:
            if new_ball.colliderect(brick):
                if brick in all_bricks:
                    invert_vertical_new_ball_speed()
                    all_bricks.remove(brick)
                    sounds.kick1.play()

            #code double balle ici
            
                
    for last_brick in all_last_bricks:
        if ball.colliderect(last_brick):
            sounds.others.play()
            upgrade_ball_speed(0.25)
            all_last_bricks.remove(last_brick)
            invert_vertical_speed()
            

        if new_ball != None:
            if new_ball.colliderect(last_brick):
                if last_brick in all_last_bricks:
                    invert_vertical_new_ball_speed()
                    all_last_bricks.remove(last_brick)
                    sounds.others.play()

    for super_brick in all_super_bricks:
        if ball.colliderect(super_brick):
            all_super_bricks.remove(super_brick)
            sounds.kick.play()
            invert_vertical_speed()
    
        
            brick = Actor("brick2-2", anchor = ["left", "top"])
            brick.pos = super_brick.pos
            all_bricks.append(brick)
    
        if new_ball != None and super_brick.colliderect(new_ball):
            invert_vertical_new_ball_speed()
            all_super_bricks.remove(super_brick)
            sounds.kick.play()

                
            brick = Actor("brick2-2", anchor = ["left", "top"])
            brick.pos = super_brick.pos
            all_bricks.append(brick)
          


    for power_up_bigger_player in all_power_up_bigger_player:
        if player.colliderect(power_up_bigger_player):
            all_power_up_bigger_player.remove(power_up_bigger_player)
            time_bigger_player = 6
            upgrade_ball_speed(2)
            ball = Actor("ball_2", ball.pos)
            player = Actor("player_2", player.pos)


    
     
    
