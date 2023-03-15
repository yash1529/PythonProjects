import pygame
import os
from pygame.constants import USEREVENT
pygame.font.init()
pygame.mixer.init()



WIDTH,HEIGHT = 900,500 #for game_window
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My_First_game")#window heading

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)


BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

EXPLODE_SOUND = pygame.mixer.Sound("E:/OLD_PC_FILES/PROJECTS_PYTHON/my_first_game_py/files/explosion.mp3")
BULLET_HIT_SOUND = pygame.mixer.Sound("E:/OLD_PC_FILES/PROJECTS_PYTHON/my_first_game_py/files/bullet_hit.mp3")
BULLET_FIRE_SOUND = pygame.mixer.Sound("E:/OLD_PC_FILES/PROJECTS_PYTHON/my_first_game_py/files/bullet_fire.mp3")


HEALTH_FONT = pygame.font.SysFont("comicsans",30)
WINNER_FONT = pygame.font.SysFont("comicsans",150)

FPS = 60
VEL = 7 #movement speed
BULLET_VEL = 10#bullet speed
MAX_BULLETS =6

SPACESHIP_WIDTH,SPACE_HEIGHT=55,40



#creating unique event id
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT +2

YELLOW_SPACESHIP_IMAGE = pygame.image.load("E:/OLD_PC_FILES/PROJECTS_PYTHON/my_first_game_py/files/spaceship_yellow.png")
YELLOW_SPACESHIP_IMAGE = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACE_HEIGHT))
YELLOW_SPACESHIP_IMAGE= pygame.transform.rotate(YELLOW_SPACESHIP_IMAGE,90)

RED_SPACESHIP_IMAGE = pygame.image.load("E:/OLD_PC_FILES/PROJECTS_PYTHON/my_first_game_py/files/spaceship_red.png")
RED_SPACESHIP_IMAGE = pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACE_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(RED_SPACESHIP_IMAGE,270)

SPACE = pygame.transform.scale(pygame.image.load("E:/OLD_PC_FILES/PROJECTS_PYTHON/my_first_game_py/files/space.png"),(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):

    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)
    red_health_text = HEALTH_FONT.render(
        "Health:"+str(red_health),1,WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health:"+str(yellow_health),1,WHITE)
    WIN.blit(red_health_text,(WIDTH - red_health_text.get_width() -10 ,10))
    WIN.blit(yellow_health_text,(10,10))
    WIN.blit(YELLOW_SPACESHIP_IMAGE,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE,(red.x,red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)

    pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow .y - VEL > 0: #upward
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: #downward
        yellow.y += VEL

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL  > BORDER.x + BORDER.width:#left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width-15 < WIDTH: #right
        red.x+= VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL - 5 > 0: #upward
        red.y-= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: #downward
        red.y+=VEL

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x>WIDTH:
            yellow_bullets.remove(bullet)


    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2  - draw_text.get_height()/2 ))
    pygame.display.update()
    pygame.time.delay(5000)#no of seconds to display * 1000

def main():
    red=pygame.Rect(700,300,SPACESHIP_WIDTH,SPACE_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACE_HEIGHT)

    red_bullets=[]
    yellow_bullets=[]

    red_health=10
    yellow_health=10

    clock = pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            
            if event.type == RED_HIT:
                red_health-=1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                    yellow_health-=1
                    BULLET_HIT_SOUND.play()


        winner_text= ""
        if red_health<=0:
            winner_text="Yellow wins !"
            EXPLODE_SOUND.play()

        if yellow_health<=0:
            winner_text="Red wins !"
            EXPLODE_SOUND.play()
            
        if winner_text !="":
            draw_winner(winner_text)
            break


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
        
    
    main()



if __name__ == "__main__":
    main() 
