import pygame
import random
pygame.init()
#initials
width,height= 1000,600
wn = pygame.display.set_mode((width, height)) #blank pygame window
pygame.display.set_caption("Ping Pong Beginner Game")
run = True
direction = [0,1]
angle = [0, 1, 2]
#colours
BLUE = (95,158,160)
PINK = (139,10,80)
DODGE = (16,78,139)
YELLOW = (255,185,15)

#for the ball
radius = 20
ball_x, ball_y = width/2 - radius, height/2 - radius
ball_vel_x, ball_vel_y = 0.7,0.7
#paddle dimensions:
paddle_width, paddle_height = 20,130
left_paddle_x , right_paddle_x = 100 - paddle_width/2, 900 - paddle_width/2
left_paddle_y = right_paddle_y = height/2 - paddle_height/2
right_paddle_vel = left_paddle_vel = 0

#gadgets
left_gadget = right_gadet = 0
left_gadget_remaining = right_gadget_remaining = 5
#...................MAIN LOOP.........................
while run:
    wn.fill(DODGE)
    for i in pygame.event.get(): #indentifying the action as events, getting it and storing it in i
        if i.type== pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN: #Checks if a key on the keyboard is being pressed
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_w and right_gadget_remaining >0:
                right_gadget = 1
            if i.key == pygame.K_LEFT:
                left_paddle_vel = -0.9
            if i.key == pygame.K_LEFT and left_gadget_remaining >0:
                left_gadget = 1
            if i.key == pygame.K_RIGHT:
                left_paddle_vel = 0.9
        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel  = 0
    #..............MOVEMENTS..........................
    ball_x+= ball_vel_x
    ball_y+= ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y  += left_paddle_vel
    #..........movement controls......................
    if ball_y <= 0 + radius or ball_y >= height - radius :
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4,0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7,0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7,1.4
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4,0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7,0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7,1.4
    if ball_x >= width - radius :
        ball_x, ball_y = width/2 - radius, height/2 -radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4,0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7,0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7,1.4
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4,0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7,0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7,1.4
        ball_vel_x *= -1
    if ball_x <= 0 +radius:
        ball_x, ball_y = width/2 -radius, height/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4,0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7,0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7,1.4
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4,0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7,0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7,1.4

    #PADDLE:
    if right_paddle_y >= height - paddle_height:
        right_paddle_y = height - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0
    if left_paddle_y >= height - paddle_height:
        left_paddle_y = height - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    #.............PADDLE COLLISIONS...................
    #LEFT PADDLE:
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
    #RIGHT PADDLE:
    if right_paddle_x <= ball_x:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1
        
    #................OBJECTS..........................
    pygame.draw.circle(wn,YELLOW, (ball_x,ball_y), radius)
    pygame.draw.rect(wn, PINK, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, PINK, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update()
