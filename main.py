import pygame  # 1:18:00
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
score_surf = test_font.render('My game', False, 'black')
score_rect = score_surf.get_rect(center=(400, 100))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
snail_rect = snail_surf.get_rect(bottomright=(snail_x_pos, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
            #if player_rect.collidepoint((event.pos)):
                #print('collision')
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(score_surf, score_rect)
    screen.blit(snail_surf, snail_rect)
    snail_rect.x -= 4
    if snail_rect.left <= -100:
        snail_rect.left = 800
    player_rect.left += 1
    screen.blit(player_surf, player_rect)
    #if player_rect.colliderect(mouse_pos):
        #pygame.quit()
        #exit()
    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint((mouse_pos)):
        #print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)