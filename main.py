import pygame

pygame.init()

import flappy_bird
import tateti
import spaceinvaders
import pong
import breakout
import snake
import trex

run = True
W, H = 800, 600
window = pygame.display.set_mode((W, H))
game_rect_pressed = False
game_font = pygame.font.Font('retro_computer_personal_use.ttf', 40)
game_font.set_bold(True)
white = (255, 255, 255)
red = (215, 16, 16)

pygame.mixer.music.load('menu_music.mp3')
pygame.mixer.music.play(-1)

# main menu


while run:
    
    pygame.mixer.music.set_volume(0.7)
    window.fill((0, 0, 0))
    message_surface = game_font.render("CLASSIC GAMES", True, red)
    message_rect = message_surface.get_rect(center=(W // 2, H // 2))
    window.blit(message_surface, message_rect)

    listGamesRects = [pygame.draw.rect(window, white, (200, 140, 100, 100)),
                      pygame.draw.rect(window, white, (310, 140, 100, 100)),
                      pygame.draw.rect(window, white, (420, 140, 100, 100)),
                      pygame.draw.rect(window, white, (530, 140, 100, 100)),
                      pygame.draw.rect(window, white, (240, 350, 100, 100)),
                      pygame.draw.rect(window, white, (350, 350, 100, 100)),
                      pygame.draw.rect(window, white, (460, 350, 100, 100))]

    listGamesIcons = [
        pygame.transform.scale(pygame.image.load('game_icons/tateti_icon.png'), [80, 80]),
        pygame.transform.scale(pygame.image.load('game_icons/flappy_bird_icon.png'), [80, 60]),
        pygame.transform.scale(pygame.image.load('game_icons/pong_icon.png'), [80, 80]),
        pygame.transform.scale(pygame.image.load('game_icons/snake_icon.png'), [80, 80]),
        pygame.transform.scale(pygame.image.load('game_icons/t_rex_icon.png'), [80, 80]),
        pygame.transform.scale(pygame.image.load('game_icons/space_invaders_icon.png'), [80, 80]),
        pygame.transform.scale(pygame.image.load('game_icons/breakout_icon.png'), [80, 80])
    ]

    # Carga las imagenes centradas con el rect que le corresponde
    window.blit(listGamesIcons[0], listGamesIcons[0].get_rect(center=listGamesRects[0].center))
    window.blit(listGamesIcons[1], listGamesIcons[1].get_rect(center=listGamesRects[1].center))
    window.blit(listGamesIcons[2], listGamesIcons[2].get_rect(center=listGamesRects[2].center))
    window.blit(listGamesIcons[3], listGamesIcons[3].get_rect(center=listGamesRects[3].center))
    window.blit(listGamesIcons[4], listGamesIcons[4].get_rect(center=listGamesRects[4].center))
    window.blit(listGamesIcons[5], listGamesIcons[5].get_rect(center=listGamesRects[5].center))
    window.blit(listGamesIcons[6], listGamesIcons[6].get_rect(center=listGamesRects[6].center))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if listGamesRects[0].collidepoint(pos):
                pygame.mixer.music.set_volume(0.2)
                tateti.main_game()
            if listGamesRects[1].collidepoint(pos):
                pygame.mixer.music.set_volume(0.2)
                flappy_bird.main_game()
            if listGamesRects[2].collidepoint(pos):
                pygame.mixer.music.set_volume(0.2)
                pong.view_menu_screen()
            if listGamesRects[3].collidepoint(pos):
                pygame.mixer.music.set_volume(0.2)
                snake.intro()
            if listGamesRects[4].collidepoint(pos):
                pygame.mixer.music.set_volume(0.2)
                trex.main_trex()
            if listGamesRects[5].collidepoint(pos):
                pygame.mixer.music.set_volume(0.2)
                spaceinvaders.main_game()
            if listGamesRects[6].collidepoint(pos):
                pygame.mixer.music.set_volume(0.2)
                breakout.main_game()

    pygame.display.set_caption("MENU")
    pygame.display.set_icon(pygame.image.load('icon_menu.ico'))
    pygame.display.update()

pygame.quit()
