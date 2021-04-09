import pygame

pygame.init()

screen = pygame.display.set_mode((1080,720))
p1col = (255,122,122)
p2col = (0,0,255)
def num_to_coords(x,y):
    if x == 1 and y == 1:
        return 7
    if x == 1 and y == 2:
        return 4
    if x == 1 and y == 3:
        return 1
    if x == 2 and y == 1:
        return 8
    if x == 2 and y == 2:
        return 5
    if x == 2 and y == 3:
        return 2
    if x == 3 and y == 1:
        return 9
    if x == 3 and y == 2:
        return 6
    if x == 1 and y == 1:
        return 3
def num_to_x(num):
    if num == 1 or num == 4 or num == 7:
        return 1
    if num == 2 or num == 5 or num == 8:
        return 2
    if num == 3 or num == 6 or num == 9:
        return 3
def num_to_y(num):
    if num == 1 or num == 2 or num == 3:
        return 3
    if num == 4 or num == 5 or num == 6:
        return 2
    if num == 7 or num == 8 or num == 9:
        return 1

def make_map():
    font = pygame.font.Font('freesansbold.ttf',64)
    p1txt = font.render('PLAYER',True,(10,10,10))
    p2txt = font.render('COMPUTER',True,(10,10,10))
    pygame.draw.rect(screen,p1col,(0,0,540,120))
    pygame.draw.rect(screen,p2col,(540,0,540,120))
    screen.blit(p1txt,(10,10))
    screen.blit(p2txt,(680,10))
    pygame.draw.rect(screen,(122,122,122),(235,110,610,610))
    pygame.draw.rect(screen,(0,0,0),(245,120,590,590))
    n = 1
    while n <= 2:
        pygame.draw.rect(screen,(122,122,122),(245,110+n*200,600,10))
        pygame.draw.rect(screen,(122,122,122),(235+n*200,110,10,600))

        n+=1

def cross(num):
    n = 0
    while n <= 156:
        pygame.draw.circle(screen, p1col, ((num_to_x(num) - 1) * 200 + 262+n, ((num_to_y(num) - 1)) * 200 + 137+n), 12)
        pygame.draw.circle(screen, p1col, ((num_to_x(num) - 1) * 200 + 262+n, ((num_to_y(num) - 1)) * 200 + 293-n), 12)

        n += 1
    pygame.draw.circle(screen, p1col, ((num_to_x(num) - 1) * 200 + 262, ((num_to_y(num) - 1)) * 200 + 137), 12)
    pygame.draw.circle(screen, p1col, ((num_to_x(num) - 1) * 200 + 262, ((num_to_y(num) - 1)) * 200 + 293), 12)
    pygame.draw.circle(screen, p1col, ((num_to_x(num) - 1) * 200 + 418, ((num_to_y(num) - 1)) * 200 + 137), 12)
    pygame.draw.circle(screen, p1col, ((num_to_x(num) - 1) * 200 + 418, ((num_to_y(num) - 1)) * 200 + 293), 12)
def circle(num):
    pygame.draw.circle(screen, p2col, (340 + (num_to_x(num)-1)*200, 215 + (num_to_y(num)-1)*200), 85)
    pygame.draw.circle(screen, (0,0,0), (340 + (num_to_x(num)-1)*200, 215 + (num_to_y(num)-1)*200), 61)





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1080, 720))
    make_map()
    circle(6)
    cross(1)

    pygame.display.flip()

pygame.quit()
