import pygame
import random
import math
pygame.init() #initialization
screen = pygame.display.set_mode((800,600)) #size of the screen
run = True
#background
background = pygame.image.load('background.png')
#title
pygame.display.set_caption("V K T s - SPACE SHOOTING GAME")
icon = pygame.image.load('monster1.png')
pygame.display.set_icon(icon)


#adding image in space
playerImg = pygame.image.load('spaceship.png')
playerx = 370
playery = 480
playerChange = 0


# ADDING ENEMIES
enemyImg = []
enemyx = []
enemyy = []
enemyxChange = []
enemyyChange = []
numOfEnemies = 6

for i in range(numOfEnemies):
    enemyImg.append(pygame.image.load('monster1.png'))
    enemyx.append(random.randint(0,800))
    enemyy.append(random.randint(0,150))
    enemyxChange.append(20)
    enemyyChange.append(20)

bullet = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletxChange = 0
bulletyChange = 10
bulletState = 'ready'
#firing a bullet
def firing(x,y):
    global bulletState
    bulletState = 'fire'
    screen.blit(bullet,(x,y))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx,2)) + (math.pow(enemyy - bullety,2)))
    if distance < 27:
        return True
    else:
        return False
#score
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf',50)
textx = 10
texty = 10
#game over
gameover = pygame.font.Font('freesansbold.ttf',100)


def showScore(x,y):
    score = font.render("SCORE :" + str(scoreValue),True,(0,255,255))
    screen.blit(score,(x,y))
def enemyf(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def player(x,y):
    screen.blit(playerImg,(x,y))
#game over function
def gameOverText():
    gameOver = gameover.render("GAME OVER" , True, (255, 0, 0))
    screen.blit(gameOver,(80,250))

#game loop
while run:
    # R G B values = 255
    screen.fill((0,0,0))
    #background
    screen.blit(background,(120,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # check for movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChange = -3
            if event.key == pygame.K_RIGHT:
                playerChange = 3
            if event.key == pygame.K_SPACE:
                bulletx = playerx
                firing(bulletx,bullety)
        if event.type == pygame.KEYUP:
            if  event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChange = 0
    playerx += playerChange
    if playerx <= 1:
        playerx = 1
    elif playerx >= 730:
        playerx = 730

    #bullet movement
    if bullety <= 0:
        bullety = 480
        bulletState = 'ready'

    if bulletState is 'fire':
        firing(bulletx,bullety)
        bullety -= bulletyChange
    for i in range(numOfEnemies):
        #game over
        if enemyy[i] > 430:
            for j in range(numOfEnemies):
                enemyy[j] = 2000
            gameOverText()
            break
        enemyx[i] += enemyxChange[i]
        if enemyx[i] <= 1:
            enemyxChange[i] = 4
            enemyy[i] += enemyyChange[i]
        elif enemyx[i] >= 730:
            enemyxChange[i] = -4
            enemyy[i] += enemyyChange[i]
        collision = iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:
            bullety = 480
            bulletState = 'ready'
            scoreValue += 1
            enemyx[i] = random.randint(0, 800)
            enemyy[i] = random.randint(0, 150)
        enemyf(enemyx[i], enemyy[i], i)
    player(playerx,playery)
    showScore(texty,texty)
    pygame.display.update()


