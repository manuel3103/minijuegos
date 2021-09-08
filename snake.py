import pygame
import random
import os

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

#pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')
block_size = 10
eat_sound = pygame.mixer.Sound('snake_files/eat.wav')
end_game_sound = pygame.mixer.Sound('snake_files/end_game.wav')

clock = pygame.time.Clock()
FPS = 22

font = pygame.font.SysFont(None, 35)
font_score = pygame.font.Font('snake_files/retro_computer_personal_use.ttf', 15)
font_large = pygame.font.SysFont(None, 75)


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    paused = False
        gameDisplay.fill(black)

        message_to_screen("Juego pausado", red, 10, 'L')
        message_to_screen("Presiona r para volver al juego", red, 90, 's')
        pygame.display.update()


def update_high_score(high_score):
    text_high = font_score.render(f"RECORD:{high_score}", True, red)
    gameDisplay.blit(text_high, [600, 0])

def update_score(score):
    text = font_score.render(f"PUNTAJE:{score}", True, red)
    gameDisplay.blit(text, [0, 0])


def shortcuts():
    welcome_screen = True
    while welcome_screen:
        welcome_screen = handle_key_on_welcome_screen()
        gameDisplay.fill(black)
        message_to_screen("Instrucciones", green, -200, 'L')
        message_to_screen("Jugar -> p", white, -100, 's')
        message_to_screen("Salir -> q", white, -55, 's')
        message_to_screen("Pausa -> b", white, 80, 's')
        message_to_screen("Volver al juego -> r", white, 125, 's')
        message_to_screen("Volver atras -> e", white, -10, 's')
        message_to_screen("Intrucciones -> s", white, 170, 's')
        message_to_screen("Menu -> h", white, 35, 's')
        pygame.display.update()


def handle_key_on_welcome_screen() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                intro()
                return False
            if event.key == pygame.K_q:
                return False
            if event.key == pygame.K_h:
                intro()
                return False
    return True


def intro():
    intro = True
    pygame.display.set_caption("SNAKE")
    icon_surface = pygame.image.load('snake_files/snake.ico')
    pygame.display.set_icon(icon_surface)
    while intro:
        intro = handle_key_during_game()
        
        gameDisplay.fill(black)
        message_to_screen("Bienvenido al Snake!", green, -200, 'L')
        message_to_screen("Presiona la tecla q para salir", white, -100, 's')
        message_to_screen("Presiona la tecla p para jugar", white, -50, 's')
        message_to_screen("Presiona la tecla s para ver las intrucciones", white, 0, 's')
        pygame.display.update()


def handle_key_during_game() -> bool:
    gameDisplay.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_loop()
                return False
            elif event.key == pygame.K_q:
                return False
            elif event.key == pygame.K_s:
                shortcuts()
                return False
    return True


def text_objects(text, color, size):
    if size == "L":
        text_surface = font_large.render(text, True, color)
    else:
        text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_to_screen(msg, color, y_displace, size):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(text_surf, text_rect)


def snake_create(block_size, snake_list):
    for el in snake_list:
        pygame.draw.rect(gameDisplay, green, [el[0], el[1], block_size, block_size])


def game_loop():
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    snake_list = []
    snake_length = 1
    lead_x_change = 0
    lead_y_change = 0
    randappleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    randappleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
    while not gameExit:
        if gameOver:
            message_to_screen("Fin del juego", red, -200, 'L')
            message_to_screen("Presiona la tecla p para jugar de nuevo!", white, -100, 's')
            message_to_screen("Presiona la tecla q para salir!", white, -50, 's')
            message_to_screen("Presiona la tecla h para ir al menu!", white, 0, 's')
            end_game_sound.play()
            pygame.display.update()
        while gameOver:
           
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    if event.key == pygame.K_h:
                        intro()
                    if event.key == pygame.K_p:
                        gameExit = False
                        gameOver = False
                        lead_x = display_width / 2
                        lead_y = display_height / 2
                        snake_list = []
                        snake_length = 1
                        lead_x_change = 0
                        lead_y_change = 0
                        randappleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
                        randappleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size                  
                    lead_y_change = 0
                
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0

                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_b:
                    pause()
        if lead_x <= 0 or lead_y <= 0 or lead_x >= display_width or lead_y >= display_height:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change


        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, red, [randappleX, randappleY, block_size, block_size])

        snake_create(block_size, snake_list)
        update_score(snake_length - 1)
        pygame.display.update()

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snake_list.append(snakehead)
        if snake_length < len(snake_list):
            del (snake_list[0])

        if lead_x == randappleX and lead_y == randappleY:
            randappleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            randappleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            eat_sound.play()
            snake_length += 1

        clock.tick(FPS)

 


