import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
running = True
x = 30
y = 30
ball = pygame.image.load("ball.png")
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-=3
    if pressed[pygame.K_DOWN]: y+=3
    if pressed[pygame.K_RIGHT]: x+=3
    if pressed[pygame.K_LEFT]: x-=3

    screen.fill((255, 255, 255))
    screen.blit(ball, (x,y))
    pygame.display.flip()
    clock.tick(60)                                                                                                                                                                                                                                                                                                                                                                                              