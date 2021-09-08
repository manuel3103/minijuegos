import pygame
import os
from random import randint


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def right(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def left(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 680:
            self.rect.x = 680


class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [0, 0]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = randint(-5, 5)
        self.velocity[1] = -self.velocity[1]

    def up(self):
        self.velocity[0] = randint(-5, 5)
        self.velocity[1] = -5


class Breakout:

    def __init__(self):
        if __name__ == '__main__':
            pygame.init()

        self.WHITE = (255, 255, 255)
        self.DARK = (0, 0, 0)
        self.LIGHTBLUE = (0, 136, 200)
        self.RED = (255, 0, 0)
        self.ORANGE = (255, 100, 0)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        self.font_menu = pygame.font.Font("retro_computer_personal_use.ttf", 25)
        self.font_menu.set_bold(True)

        self.size = (800, 600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Breakout Game")

        self.sound = pygame.mixer.Sound(os.path.join("breakout_files", "ping_pong_8bit_plop.ogg"))
        self.soundB = pygame.mixer.Sound(os.path.join("breakout_files", "ping_pong_8bit_beeep.ogg"))
        self.soundG = pygame.mixer.Sound(os.path.join("breakout_files", "game_over.wav"))

        self.score = 0
        self.lives = 3

        self.all_sprite_list = pygame.sprite.Group()
        self.paddle = Paddle(self.LIGHTBLUE, 120, 10)
        self.paddle.rect.x = 350
        self.paddle.rect.y = 560
        self.ball = Ball(self.WHITE, 10, 10)
        self.ball.rect.x = 400
        self.ball.rect.y = 554

        self.brick_list = pygame.sprite.Group()
        for i in range(22):
            self.brick = Brick(self.RED, 30, 20)
            self.brick.rect.x = 20 + i * 35
            self.brick.rect.y = 110
            self.all_sprite_list.add(self.brick)
            self.brick_list.add(self.brick)

        for i in range(22):
            self.brick = Brick(self.ORANGE, 30, 20)
            self.brick.rect.x = 20 + i * 35
            self.brick.rect.y = 140
            self.all_sprite_list.add(self.brick)
            self.brick_list.add(self.brick)

        for i in range(22):
            self.brick = Brick(self.YELLOW, 30, 20)
            self.brick.rect.x = 20 + i * 35
            self.brick.rect.y = 170
            self.all_sprite_list.add(self.brick)
            self.brick_list.add(self.brick)

        for i in range(22):
            self.brick = Brick(self.GREEN, 30, 20)
            self.brick.rect.x = 20 + i * 35
            self.brick.rect.y = 200
            self.all_sprite_list.add(self.brick)
            self.brick_list.add(self.brick)

        for i in range(22):
            self.brick = Brick(self.BLUE, 30, 20)
            self.brick.rect.x = 20 + i * 35
            self.brick.rect.y = 230
            self.all_sprite_list.add(self.brick)
            self.brick_list.add(self.brick)

        self.all_sprite_list.add(self.ball)
        self.all_sprite_list.add(self.paddle)

        self.resume_pause = self.font_menu.render('RESUME', False, self.WHITE)
        self.exit_pause = self.font_menu.render('EXIT', False, self.RED)

        self.resume_pos = [int(self.size[0] * 0.5 - self.resume_pause.get_width() / 2), int(self.size[1] * 0.3 - 25)]
        self.exit_pos = [int(self.size[0] * 0.5 - self.exit_pause.get_width() / 2), int(self.size[1] * 0.7 - 25)]

        self.clock = pygame.time.Clock()

        self.exit_e = self.font_menu.render('EXIT', False, self.RED)
        self.resume = self.font_menu.render('RESUME', False, self.WHITE)

        self.pos_exit = [int(self.size[0] * 0.5 - self.exit_e.get_width() / 2), int(self.size[1] * 0.3 - 25)]
        self.pos_resume = [int(self.size[0] * 0.5 - self.resume.get_width() / 2), int(self.size[1] * 0.7 - 25)]

    # if the player wants keep playing return true, else false.
    def view_menu_stop(self):
        wants_keep_playing = False
        exit_menu = False
        while not exit_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()
                    if self.resume.get_rect(topleft=self.pos_resume).collidepoint(pos_mouse):
                        wants_keep_playing = True
                        exit_menu = True
                    elif self.exit_e.get_rect(topleft=self.pos_exit).collidepoint(pos_mouse):
                        wants_keep_playing = False
                        exit_menu = True

            if not exit_menu:
                self.screen.fill(self.DARK)

                self.screen.blit(self.exit_e, self.pos_exit)
                self.screen.blit(self.resume, self.pos_resume)

            pygame.display.flip()
            self.clock.tick(60)
        return wants_keep_playing

    def start_game(self):
        carry_on = True
        while carry_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    carry_on = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        carry_on = self.view_menu_stop()
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.paddle.right(6)
            if key[pygame.K_RIGHT]:
                self.paddle.left(6)

            self.all_sprite_list.update()
            if self.ball.rect.x >= 790:
                self.ball.velocity[0] = -self.ball.velocity[0]
            if self.ball.rect.x <= 0:
                self.ball.velocity[0] = -self.ball.velocity[0]
            if self.ball.rect.y > 590:
                self.ball.rect.x = 400
                self.ball.rect.y = 554
                self.paddle.rect.x = 350
                self.paddle.rect.y = 560
                self.ball.velocity[1] = -self.ball.velocity[1]
                self.lives -= 1
                if self.lives == 0:
                    self.screen.fill(self.DARK)
                    font = pygame.font.Font('retro_computer_personal_use.ttf', 74)
                    s_font = pygame.font.Font('retro_computer_personal_use.ttf', 25)
                    s_text = s_font.render("score: " + str(self.score), 1, self.WHITE)
                    text = font.render("GAME OVER", 1, self.RED)
                    self.screen.blit(text, (150, 250))
                    self.screen.blit(s_text, (300, 500))
                    pygame.display.flip()
                    self.soundG.play()
                    pygame.time.wait(3000)
                    carry_on = False

            if self.ball.rect.y < 40:
                self.ball.velocity[1] = -self.ball.velocity[1]

            if pygame.sprite.collide_mask(self.ball, self.paddle):
                self.sound.play()
                self.ball.up()

            brick_collide_list = pygame.sprite.spritecollide(self.ball, self.brick_list, False)
            for brick in brick_collide_list:
                self.ball.bounce()
                self.score += 1
                brick.kill()
                self.soundB.play()
                if len(self.brick_list) == 0:
                    self.screen.fill(self.DARK)
                    font = pygame.font.Font('retro_computer_personal_use.ttf', 74)
                    text = font.render("YOU WON!", 1, self.WHITE)
                    s_font = pygame.font.Font('retro_computer_personal_use.ttf', 25)
                    s_text = s_font.render("score: " + str(self.score), 1, self.WHITE)
                    self.screen.blit(text, (200, 250))
                    self.screen.blit(s_text, (300, 500))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    carry_on = False

            self.screen.fill(self.DARK)
            pygame.draw.line(self.screen, self.WHITE, [0, 38], [800, 38], 2)

            # Display
            font = pygame.font.Font('retro_computer_personal_use.ttf', 18)
            text = font.render("Score: " + str(self.score), 1, self.WHITE)
            self.screen.blit(text, (20, 10))
            text = font.render("Lives: " + str(self.lives), 1, self.WHITE)
            self.screen.blit(text, (675, 10))
            if self.lives < 2:
                text = font.render("Lives: " + str(self.lives), 1, self.RED)
                self.screen.blit(text, (675, 10))

            self.all_sprite_list.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(60)

        if __name__ == '__main__':
            pygame.quit()


def main_game():
    pygame.display.set_caption("Breakout")
    game = Breakout()
    game.start_game()
