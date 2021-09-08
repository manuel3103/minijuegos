import pygame, os, sys, enum

black = (50, 50, 50)
white = (255, 255, 255)
green = (0, 255, 0)
red   = (255, 0 , 0)

screen_size = (800, 600)

screen = pygame.display.set_mode(screen_size)
clock  = pygame.time.Clock()

if __name__ == '__main__':
    pygame.init()

sound_player_shoot  = pygame.mixer.Sound(os.path.join("space_invaders_files","player_shoot.wav"))
sound_enemie_shoot  = pygame.mixer.Sound(os.path.join("space_invaders_files","enemie_shoot.wav"))
sound_enemie_beaten = pygame.mixer.Sound(os.path.join("space_invaders_files","enemie_beaten.wav"))
sound_player_beaten = pygame.mixer.Sound(os.path.join("space_invaders_files","player_beaten.wav"))

sound_player_shoot.set_volume(0.5)
sound_enemie_shoot.set_volume(0.5)
sound_enemie_beaten.set_volume(0.5)
sound_player_beaten.set_volume(0.5)

sprites = pygame.image.load(os.path.join("space_invaders_files","space-invaders.png")).convert()
live_sheet = pygame.image.load(os.path.join("space_invaders_files","life.png")).convert()

sprites.set_colorkey(0)
live_sheet.set_colorkey(white)
size_enemie_one     = (8, 8)
size_enemie_two     = (11, 8)
size_enemie_three   = (12, 8)
size_enemie_boss    = (16, 8)
size_player         = (13, 8)
size_enemie_shoot   = (3, 7)
size_shoot          = (1, 7)
size_life_bar       = (83, 11)
size_life_heart     = (16, 14)

live_heart         = pygame.transform.scale(live_sheet.subsurface((0 , 0)  , size_life_heart)   , (24, 21))
life_bar_zero      = pygame.transform.scale(live_sheet.subsurface((0 , 39) , size_life_bar)     , (161, 20))
life_bar_one       = pygame.transform.scale(live_sheet.subsurface((0 , 27) , size_life_bar)     , (161, 20))
life_bar_two       = pygame.transform.scale(live_sheet.subsurface((0 , 15) , size_life_bar)     , (161, 20))
life_bar_three     = pygame.transform.scale(live_sheet.subsurface((18, 3)  , size_life_bar)     , (161, 20))
enemie_one_FIRST   = pygame.transform.scale(sprites.subsurface(   (5, 1)   , size_enemie_one)   , (24, 24))
enemie_one_TWO     = pygame.transform.scale(sprites.subsurface(   (5, 11)  , size_enemie_one)   , (24, 24))
enemie_two_FIRST   = pygame.transform.scale(sprites.subsurface(   (22, 1)  , size_enemie_two)   , (33, 24))
enemie_two_TWO     = pygame.transform.scale(sprites.subsurface(   (22, 11) , size_enemie_two)   , (33, 24))
enemie_three_FIRST = pygame.transform.scale(sprites.subsurface(   (39, 1)  , size_enemie_three) , (34, 24))
enemie_three_TWO   = pygame.transform.scale(sprites.subsurface(   (39, 11) , size_enemie_three) , (34, 24))
enemie_death       = pygame.transform.scale(sprites.subsurface(   (55, 1)  , (13, 8))           , (64, 32))
player_image       = pygame.transform.scale(sprites.subsurface(   (3, 49)  , size_player)       , (39, 24))
player_shoot       = pygame.transform.scale(sprites.subsurface(   (52, 21) , size_shoot)        , (3, 21))
enemie_shoot_one   = pygame.transform.scale(sprites.subsurface(   (1, 21)  , size_enemie_shoot) , (9, 21))
enemie_shoot_two   = pygame.transform.scale(sprites.subsurface(   (6, 21)  , size_enemie_shoot) , (9, 21))
enemie_shoot_three = pygame.transform.scale(sprites.subsurface(   (11, 21) , size_enemie_shoot) , (9, 21))
enemie_shoot_four  = pygame.transform.scale(sprites.subsurface(   (16, 21) , size_enemie_shoot) , (9, 21))

font_menu  = pygame.font.Font('retro_computer_personal_use.ttf', 25)
font_menu.set_bold(True)
exit_rendered   = font_menu.render('EXIT', False, red)
resume_rendered = font_menu.render('RESUME', False, white)
dead_rendered   = font_menu.render('Stupid aliens', False, red)
win_rendered    = font_menu.render('YOU ARE THE BEST', False, green)
exit_pos        = [int(screen_size[0] * 0.5 - exit_rendered.get_width() / 2)     , int(screen_size[1] * 0.7 - 25)]
resume_pos      = [int(screen_size[0] * 0.5 - resume_rendered.get_width() / 2)   , int(screen_size[1] * 0.3 - 25)]
dead_pos        = [int(screen_size[0] * 0.5 - dead_rendered.get_width() / 2)     , int(screen_size[1] * 0.3 - 25)]
win_pos         = [int(screen_size[0] * 0.5 - win_rendered.get_width() / 2)      , int(screen_size[1] * 0.3 - 25)]

class MOVE_ENEMY(enum.Enum):

    RIGHT = 0
    LEFT  = 1

class ShootC(pygame.sprite.Sprite):

    def __init__(self, owner, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.owner        = owner
        self.image        = enemie_shoot_one if type(self.owner) is Enemy else player_shoot
        self.actual_image = 0
        self.rect         = self.image.get_rect()
        self.rect.x       = initial_position[0]
        self.rect.y       = initial_position[1]

    def move(self):
        if type(self.owner) is Enemy:
            self.actual_image += 1
            if self.actual_image == 1:
                self.image = enemie_shoot_two
            elif self.actual_image == 2:
                self.image = enemie_shoot_three
            elif self.actual_image == 3:
                self.image = enemie_shoot_four
            elif self.actual_image == 4:
                self.image = enemie_shoot_one
                self.actual_image = 0
            self.rect.y += 10
            if(self.rect.y > 630):
                self.kill()
        elif type(self.owner) is Player:
            self.rect.y -= 14
            if(self.rect.y < -30):
                self.kill()

    def hit(self):
        self.kill()

class Enemy(pygame.sprite.Sprite):

    def __init__(self, image_one, image_two, initial_position):
        pygame.sprite.Sprite.__init__(self)
        
        self.image_one = image_one
        self.image_two = image_two
        self.available_to_shoot = True
        self.last_shoot = 0

        self.image  = image_one
        self.rect   = self.image_one.get_rect()
        self.rect.x = initial_position[0]
        self.rect.y = initial_position[1]

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.image = self.image_two if self.image == self.image_one else self.image_one

    def shoot(self):
        sound_enemie_shoot.play()
        return ShootC(self, self.rect.midbottom)

    def hit(self):
        self.image = enemie_death
        sound_enemie_beaten.play()
        self.kill()

class Player(pygame.sprite.Sprite):

    def __init__(self, image, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = initial_position[0]
        self.rect.y = initial_position[1]
        self.velocity_x = 0
        self.life = 3

    def move(self):
        if self.rect.right + self.velocity_x >= 800:
            self.rect.right = 800
        elif self.rect.left + self.velocity_x <= 0:
            self.rect.left = 0
        else:
            self.rect.x += self.velocity_x

    def beaten(self, shoots):
        print(self.life)
        self.life -= shoots
        sound_player_beaten.play()

    def shoot(self):
        sound_player_shoot.play()
        return ShootC(self, self.rect.midtop)

class SpaceInvaders():

    def __init__(self):
        self.total_enemies                 = pygame.sprite.RenderUpdates()
        self.first_line_enemies            = pygame.sprite.RenderUpdates()
        self.second_line_enemies           = pygame.sprite.RenderUpdates()
        self.thrid_line_enemies            = pygame.sprite.RenderUpdates()
        self.enemies_availables_to_shoot   = pygame.sprite.RenderUpdates()
        self.enemies_unavailables_to_shoot = pygame.sprite.RenderUpdates()
        self.enemies_shoots                = pygame.sprite.RenderUpdates()
        self.player_shoots                 = pygame.sprite.RenderUpdates()

        self.image_life  = life_bar_three
        self.image_heart = live_heart
        self.player = Player(player_image, (400, 550))


        self.first_line_with_direction_dictionary  = {MOVE_ENEMY.RIGHT : self.first_line_enemies }
        self.second_line_with_direction_dictionary = {MOVE_ENEMY.LEFT  : self.second_line_enemies}
        self.thrid_line_with_direction_dictionary  = {MOVE_ENEMY.RIGHT : self.thrid_line_enemies }

    def _move_line(self, dictionary):
        for key in dictionary:
            for enemy in dictionary[key]:
                if key == MOVE_ENEMY.LEFT:
                    enemy.move(enemy.rect.x - 5, enemy.rect.y)
                else:
                    enemy.move(enemy.rect.x + 5, enemy.rect.y)

    def _determine_move_x(self, dictionary):
        move_x = None
        for key in dictionary:
            for enemy in dictionary[key]:
                if key == MOVE_ENEMY.RIGHT:
                    if enemy.image.get_rect().right + enemy.rect.x + 5 >= 800:
                        move_x = MOVE_ENEMY.LEFT
                        break
                elif key == MOVE_ENEMY.LEFT:
                    if enemy.image.get_rect().left + enemy.rect.x - 5 <= 0:
                        move_x = MOVE_ENEMY.RIGHT
                        break
        if move_x != None:
            enemies = dictionary.pop(key)
            dictionary[move_x] = enemies
            for enemy in dictionary[move_x]:
                enemy.move(enemy.rect.x, enemy.rect.y + 5)

    def _move_enemies(self):

        self._determine_move_x(self.first_line_with_direction_dictionary)
        self._determine_move_x(self.second_line_with_direction_dictionary)
        self._determine_move_x(self.thrid_line_with_direction_dictionary)

        self._move_line(self.first_line_with_direction_dictionary)
        self._move_line(self.second_line_with_direction_dictionary)
        self._move_line(self.thrid_line_with_direction_dictionary)

    def _initialize_enemies_positions(self):
        for i in range(0, 60, 10):
            enemyFirstLine = Enemy(enemie_one_FIRST, enemie_one_TWO, (i * 14 + 5, 30 ))
            enemySecondLine = Enemy(enemie_two_FIRST, enemie_two_TWO, (i * 14 + 60, 70))
            enemyThridLine = Enemy(enemie_three_FIRST, enemie_three_TWO, (i * 14 + 5, 110))
            self.first_line_enemies.add(enemyFirstLine)
            self.second_line_enemies.add(enemySecondLine)
            self.thrid_line_enemies.add(enemyThridLine)
            self.enemies_availables_to_shoot.add(enemyFirstLine, enemySecondLine, enemyThridLine)
            self.total_enemies.add(enemyFirstLine, enemySecondLine, enemyThridLine)

    def enemies_shooting(self, enemies):
        current_time = pygame.time.get_ticks()
        for enemy in enemies:
            enemy.last_shoot = current_time
            self.enemies_shoots.add(enemy.shoot())
            self.enemies_availables_to_shoot.remove(enemy)
            self.enemies_unavailables_to_shoot.add(enemy)

    def _capture_enemies_to_shoot(self):
        self.enemies_shooting([enemy for enemy in self.enemies_availables_to_shoot  if enemy.rect.centerx >= self.player.rect.left and enemy.rect.centerx <= self.player.rect.right])

    def _move_shoots(self):
        for shoot in self.enemies_shoots:
            shoot.move()
        for shoot in self.player_shoots:
            shoot.move()

    def _determine_life_image(self):
        if self.player.life == 2:
            self.image_life = life_bar_two
        elif self.player.life == 1:
            self.image_life = life_bar_one
        elif self.player.life == 0:
            self.image_life = life_bar_zero

    def _move_unavailable_enemies_to_shoot_to_available(self):
        current_time = pygame.time.get_ticks()
        self.enemies_availables_to_shoot.add([enemy for enemy in self.enemies_unavailables_to_shoot if current_time - enemy.last_shoot > 1700])
        self.enemies_unavailables_to_shoot.remove([enemy for enemy in self.enemies_availables_to_shoot])
    
    def view_menu_stop(self):
        keep_playing = False
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    if __name__ == '__main__':
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()
                    if resume_rendered.get_rect(topleft=resume_pos).collidepoint(pos_mouse):
                        keep_playing = True
                        waiting = False
                    elif exit_rendered.get_rect(topleft=exit_pos).collidepoint(pos_mouse):
                        waiting = False
                        keep_playing = False
                        
            screen.fill(black)

            screen.blit(exit_rendered, exit_pos)
            screen.blit(resume_rendered, resume_pos)

            pygame.display.flip()
            clock.tick(60)
        return keep_playing

    def view_menu_dead(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    if __name__ == '__main__':
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()
                    if exit_rendered.get_rect(topleft=exit_pos).collidepoint(pos_mouse):
                        waiting = False
                        
            screen.fill(black)

            screen.blit(exit_rendered, exit_pos)
            screen.blit(dead_rendered, dead_pos)

            pygame.display.flip()
            clock.tick(60)

    def view_menu_win(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    if __name__ == '__main__':
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()
                    if exit_rendered.get_rect(topleft=exit_pos).collidepoint(pos_mouse):
                        waiting = False
                        
            screen.fill(black)

            screen.blit(exit_rendered, exit_pos)
            screen.blit(win_rendered , win_pos)

            pygame.display.flip()
            clock.tick(60)

    def start_game(self):
        self._initialize_enemies_positions()
        game_finished = False
        pygame.time.set_timer(pygame.USEREVENT+1, 600)
        available_to_shoot = False
        while not game_finished:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT+1:
                    available_to_shoot = True
                if event.type == pygame.QUIT:
                    game_finished = True
                    if __name__ == '__main__':
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and available_to_shoot:
                        self.player_shoots.add(self.player.shoot())
                        available_to_shoot = False
                    if event.key == pygame.K_ESCAPE:
                        game_finished = not self.view_menu_stop()
                    elif event.key == pygame.K_RIGHT:
                        self.player.velocity_x = 10
                    elif event.key == pygame.K_LEFT:
                        self.player.velocity_x = - 10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.player.velocity_x = 0
                
            self._move_unavailable_enemies_to_shoot_to_available()
            self._capture_enemies_to_shoot()

            if len(pygame.sprite.groupcollide(self.player_shoots, self.total_enemies, True, True)) >= 1:
                sound_enemie_beaten.play()

            player_beaten = len(pygame.sprite.spritecollide(self.player, self.enemies_shoots, True))

            if player_beaten > 0:
                self.player.beaten(player_beaten)

            if self.player.life <= 0 or len(self.total_enemies) <= 0:
                    game_finished = True

            screen.fill(black)

            self.player.move()

            self.total_enemies.clear(screen, screen)
            self.enemies_shoots.clear(screen, screen)
            self.player_shoots.clear(screen, screen)

            self._move_enemies()
            self._move_shoots()
            self._determine_life_image()

            self.total_enemies.draw(screen)
            self.enemies_shoots.draw(screen)
            self.player_shoots.draw(screen)

            screen.blit(self.player.image, self.player.rect)
            screen.blit(self.image_heart,(600, 3))
            screen.blit(self.image_life,(625, 3))

            pygame.display.flip()
            clock.tick(14)

        pygame.time.set_timer(pygame.USEREVENT+1, 0)
        if self.player.life <= 0:
            self.view_menu_dead()
        elif len(self.total_enemies) <= 0:
            self.view_menu_win()



def main_game():
    pygame.display.set_caption("Space invaders")
    game = SpaceInvaders()
    game.start_game()