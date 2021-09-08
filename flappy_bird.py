import pygame
import random


class FlappyBird:
    run = True
    W, H = 800, 600
    window = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    #TODO: cambiar esto
    pygame.font.init()
    game_font = pygame.font.Font('retro_computer_personal_use.ttf', 30)
    game_font.set_bold(True)

    # Game variables
    gravity = 0.25
    bird_movement = 0
    game_active = True
    score = 0
    high_score = 0
    white = (255, 255, 255)

    bg_surface = pygame.image.load('flappy_bird_files/sprites/background-day.png').convert()
    bg_surface = pygame.transform.scale(bg_surface, (W, H))

    floor_surface = pygame.image.load('flappy_bird_files/sprites/base.png').convert()
    floor_surface = pygame.transform.scale(floor_surface, (W, 100))
    floor_x_pos = 0

    bird_surface = pygame.image.load('flappy_bird_files/sprites/bird.png').convert_alpha()
    bird_surface = pygame.transform.scale(bird_surface, (50, 40))
    bird_rect = bird_surface.get_rect(center=(50, H // 2))

    pipe_surface = pygame.image.load('flappy_bird_files/sprites/pipe-green.png').convert()
    pipe_surface = pygame.transform.scale2x(pipe_surface)
    pipe_list = []
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1200)
    pipe_height = [275, 300, 320, 350, 350]

    def press_to_start(self):
        waiting = True
        text = "PRESS SPACE BAR"
        self.window.blit(self.bg_surface, (0, 0))
        game_font = pygame.font.Font('retro_computer_personal_use.ttf', 25)
        game_font.set_bold(True)
        message_surface = game_font.render(text, True, self.white)
        message_rect = message_surface.get_rect(center=(self.W // 2, self.H // 2))
        self.window.blit(message_surface, message_rect)
        pygame.display.update()
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def rotate_bird(self, bird):
        new_bird = pygame.transform.rotozoom(bird, -self.bird_movement * 2, 1)
        return new_bird

    def draw_floor(self):
        self.window.blit(self.floor_surface, (self.floor_x_pos, self.H - 60))
        self.window.blit(self.floor_surface, (self.floor_x_pos + self.W, self.H - 60))
        if self.floor_x_pos <= -self.W:
            self.floor_x_pos = 0

    def create_pipe(self):
        random_pipe_pos = random.choice(self.pipe_height)
        bottom_pipe = self.pipe_surface.get_rect(midtop=(self.W + 200, random_pipe_pos))
        top_pipe = self.pipe_surface.get_rect(midbottom=(self.W + 200, random_pipe_pos - 250))
        return bottom_pipe, top_pipe

    def move_pipes(self, pipes):
        for pipe in pipes:
            pipe.centerx -= 5
        return pipes

    def draw_pipes(self, pipes):
        for pipe in pipes:
            if pipe.bottom >= self.H:
                self.window.blit(self.pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe_surface, False, True)
                self.window.blit(flip_pipe, pipe)

    def check_collision(self, pipes):
        for pipe in pipes:
            if self.bird_rect.colliderect(pipe):
                return False

        if self.bird_rect.top <= -50 or self.bird_rect.bottom >= self.H - 60:
            return False

        return True

    def score_display(self, game_state):
        if game_state == 'main_game':
            score_surface = self.game_font.render(str(int(self.score)), True, self.white)
            score_rect = score_surface.get_rect(center=(self.W//2, 100))
            self.window.blit(score_surface, score_rect)
        if game_state == 'game_over':
            score_surface = self.game_font.render('Score ' + str(int(self.score)), True, self.white)
            score_rect = score_surface.get_rect(center=(self.W // 2, 100))
            self.window.blit(score_surface, score_rect)

            high_score_surface = self.game_font.render('High score: ' + str(int(self.high_score)), True, self.white)
            high_score_rect = high_score_surface.get_rect(center=(self.W // 2, 500))
            self.window.blit(high_score_surface, high_score_rect)

    def update_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def main_flappy_bird(self):
        self.press_to_start()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game_active:
                        self.bird_movement = 0
                        self.bird_movement -= 10
                    if event.key == pygame.K_SPACE and not self.game_active:
                        self.game_active = True
                        self.pipe_list.clear()
                        self.bird_rect.center = (50, self.H // 2)
                        self.bird_movement = 0
                        self.score = 0
                if event.type == self.SPAWNPIPE:
                    self.pipe_list.extend(self.create_pipe())

            self.window.blit(self.bg_surface, (0, 0))
            if self.game_active:
                # Bird
                self.bird_movement += self.gravity
                rotated_bird = self.rotate_bird(self.bird_surface)
                self.bird_rect.centery += self.bird_movement
                self.window.blit(rotated_bird, self.bird_rect)
                self.game_active = self.check_collision(self.pipe_list)

                # Pipes
                self.pipe_list = self.move_pipes(self.pipe_list)
                self.draw_pipes(self.pipe_list)
                self.score += 0.01
                self.score_display('main_game')
            else:
                self.update_score()
                self.score_display('game_over')
            # Floor
            self.floor_x_pos -= 1
            self.draw_floor()
            pygame.display.update()
            self.clock.tick(80)


# main
def main_game():
    pygame.display.set_caption("FLAPPY BIRD")
    icon_surface = pygame.image.load('flappy_bird_files/favicon.ico')
    pygame.display.set_icon(icon_surface)
    juego2 = FlappyBird()
    juego2.main_flappy_bird()

