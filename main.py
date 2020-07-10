import pygame
import random

pygame.init()

win = pygame.display.set_mode((800, 500))

pygame.display.set_caption('PONG!')

font = pygame.font.SysFont('Snap ITC', 70)


def getB(xVal, yVal, slope):
    return yVal - slope * xVal


# ball variables
m = random.uniform(-1, 1)
b = getB(400, 250, m)
ballX = 400
xMove = random.choice([-3, 3])
ballY = int(m * ballX + b)
speedUp = 0.3

# boards
board1X = 45
board1Y = 215
board2X = 745
board2Y = 215

# score
p1Score = 0
p2Score = 0

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and board1Y - 3 > -3:
        board1Y -= 3
    if keys[pygame.K_s] and board1Y + 3 < 433:
        board1Y += 3

    if keys[pygame.K_UP] and board2Y - 3 > -3:
        board2Y -= 3
    if keys[pygame.K_DOWN] and board2Y + 3 < 433:
        board2Y += 3

    if int(m * (ballX + xMove) + b) < 8 or int(m * (ballX + xMove) + b) > 492:
        m = -m
        b = getB(ballX, ballY, m)

    if ballX > 792:
        p1Score += 1
        text1 = font.render(str(p1Score), 10, (255, 255, 255))
    if ballX < 8:
        p2Score += 1
        text2 = font.render(str(p2Score), 10, (255, 255, 255))

    if ballX > 792 or ballX < 8:
        board1X = 45
        board1Y = 215
        board2X = 745
        board2Y = 215
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255, 255, 255), (board1X, board1Y, 10, 70))
        pygame.draw.rect(win, (255, 255, 255), (board2X, board2Y, 10, 70))
        win.blit(text1, (270, 25))
        win.blit(text2, (480, 25))
        for i in range(0, 701, 40):
            pygame.draw.line(win, (255, 255, 255), (400, i), (400, i + 20), 5)
        pygame.display.update()

        pygame.time.delay(300)
        m = random.uniform(-1, 1)
        b = getB(400, 250, m)
        ballX = 400
        xMove = random.choice([-3, 3])
        ballY = int(m * ballX + b)

    ballX = int(ballX + xMove)
    ballY = int(m * ballX + b)

    if pygame.draw.rect(win, (255, 255, 255), (board1X - 2, board1Y, 10, 70)).collidepoint(ballX - 8, ballY):
        xMove = -xMove + speedUp
        m = 1.5 * (ballY - board1Y - 35) / 70
        b = getB(ballX, ballY, m)

    if pygame.draw.rect(win, (255, 255, 255), (board2X, board2Y, 10, 70)).collidepoint(ballX + 8, ballY):
        xMove = -xMove - speedUp
        m = -1.5 * (ballY - board2Y - 35) / 70
        b = getB(ballX, ballY, m)

    win.fill((0, 0, 0))
    text1 = font.render(str(p1Score), 1, (255, 255, 255))
    text2 = font.render(str(p2Score), 1, (255, 255, 255))
    win.blit(text1, (270, 25))
    win.blit(text2, (480, 25))
    pygame.draw.rect(win, (255, 255, 255), (board1X, board1Y, 10, 70))
    pygame.draw.rect(win, (255, 255, 255), (board2X, board2Y, 10, 70))
    pygame.draw.circle(win, (255, 255, 255), (ballX, ballY), 8)

    for i in range(0, 701, 40):
        pygame.draw.line(win, (255, 255, 255), (400, i), (400, i + 20), 5)

    pygame.display.update()

pygame.quit()
