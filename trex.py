import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("T-rex")

# font
font = pygame.font.Font('retro_computer_personal_use.ttf', 20)

# variables
clock = pygame.time.Clock()
FPS = 85
# imgaes
tree = pygame.image.load("t-rex_files/tree.png")
tree = pygame.transform.scale(tree, (70, 50))
tree1 = pygame.image.load("t-rex_files/tree1.png")
tree1 = pygame.transform.scale(tree1, (100, 60))
tree2 = pygame.image.load("t-rex_files/tree2.png")
tree2 = pygame.transform.scale(tree2, (90, 60))
tree3 = pygame.image.load("t-rex_files/tree3.png")
tree3 = pygame.transform.scale(tree3, (45, 60))
tree4 = pygame.image.load("t-rex_files/tree4.png")
tree4 = pygame.transform.scale(tree4, (70, 60))
dino = pygame.image.load("t-rex_files/dra1.png")
dino = pygame.transform.scale(dino, (50, 50))
dino2 = pygame.image.load("t-rex_files/dra2.png")
dino2 = pygame.transform.scale(dino2, (50, 50))
dino3 = pygame.image.load("t-rex_files/dra3.png")
dino3 = pygame.transform.scale(dino3, (50, 50))
dino4 = pygame.image.load("t-rex_files/dra4.png")
dino4 = pygame.transform.scale(dino4, (50, 50))
dino5 = pygame.image.load("t-rex_files/dra6.png")
dino5 = pygame.transform.scale(dino5, (50, 50))

run = [dino, dino, dino, dino, dino2, dino2, dino2, dino2, dino3, dino3, dino3, dino3, dino4, dino4, dino4, dino4]

background = pygame.image.load("t-rex_files/background.png")


def main_trex():
    pygame.display.set_caption("T-REX")
    icon_surface = pygame.image.load('t-rex_files/favicon.png')
    pygame.display.set_icon(icon_surface)

    #sounds
    jump_music = pygame.mixer.Sound('t-rex_files/jump.wav')
 
    

    back_x = 0
    back_y = 0
    dino_x = 50
    dino_y = 275
    tree_x = 650
    tree_y = 282
    back_velocity = 0
    run_point = 0
    gravity = 6
    game = False
    game_over = False
    jump = False
    score = 0
    game_run = True

    while game_run:

        if back_velocity == 0:
            text_begin = font.render("Presione flecha arriba para iniciar.", True, (0, 0, 0))
            screen.blit(text_begin, [150, 150])
            run_point = 0
            pygame.display.update()
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jump_music.play()
                    if dino_y == 275:
                        jump = True
                        back_velocity = 4
                        game = True
                if event.key == K_SPACE:
                    back_x = 0
                    back_y = 0
                    dino_x = 50
                    dino_y = 275
                    tree_x = 650
                    tree_y = 282
                    back_velocity = 0
                    run_point = 0
                    gravity = 7
                    game = False
                    game_over = False
                    jump = False
                    score = 0

        if back_x == -600:
            back_x = 0

        if tree_x < -2000:
            tree_x = 650

        # making dino jumps
        if 276 > dino_y > 125:
            if jump:
                dino_y -= 7
        else:
            jump = False

        if dino_y < 275:
            if not jump:
                dino_y += gravity

        # collision
        if tree_x < dino_x + 50 < tree_x + 70 and tree_y < dino_y + 50 < tree_y + 50:
            back_velocity = 0.0001
            run_point = 0
            game = False
            game_over = True

        if tree_x + 430 < dino_x + 50 < tree_x + 510 and tree_y < dino_y + 50 < tree_y + 50:
            back_velocity = 0.0001
            run_point = 0          
            game = False
            game_over = True

        if tree_x + 835 < dino_x + 50 < tree_x + 915 and tree_y < dino_y + 50 < tree_y + 50:
            back_velocity = 0.0001
            run_point = 0           
            game = False
            game_over = True

        if tree_x + 1200 < dino_x + 50 < tree_x + 1270 and tree_y < dino_y + 50 < tree_y + 50:
            back_velocity = 0.0001
            run_point = 0           
            game = False
            game_over = True
        
        if tree_x + 1620 < dino_x + 50 < tree_x + 1690 and tree_y < dino_y + 50 < tree_y + 50:
            back_velocity = 0.0001
            run_point = 0         
            game = False
            game_over = True

        

        if game:
            score += 1

        screen.fill((255, 255, 255))

        text = font.render("Puntaje: " + str(score), True, (0, 0, 0))
        text_to_finish = font.render("Fin del juego. Presione espacio.", True, (0, 0, 0))

        back_x -= back_velocity
        tree_x -= back_velocity

        screen.blit(background, [back_x + 600, back_y])
        screen.blit(background, [back_x, back_y])
        screen.blit(text, [600, 50])
        if game_over:
            screen.blit(text_to_finish, [150, 150])
        screen.blit(tree, [tree_x, tree_y])

        screen.blit(run[run_point], [dino_x, dino_y])

        # changing images to make dino run
        if not game_over:
            run_point += 1  # making an advance in my list of dinos
            if run_point > 15:
                run_point = 0


        screen.blit(tree, [tree_x,tree_y])
        screen.blit(tree1, [tree_x + 400, tree_y])
        screen.blit(tree2, [tree_x + 800, tree_y - 8])
        screen.blit(tree3, [tree_x + 1200, tree_y - 8])
        screen.blit(tree4, [tree_x + 1600, tree_y - 2])
        clock.tick(FPS)
        pygame.display.update()
