import pygame


class Tateti:
    winner = 0
    run = True
    inMenu = False
    window = pygame.display.set_mode((800, 600))
    draw = 1
    board = []
    red = (255, 0, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)
    light_green = (117, 240, 117)
    light_red = (233, 102, 81)
    title_pos = [300, 50]
    font_winner = pygame.font.Font('retro_computer_personal_use.ttf', 50)
    font_name_game = pygame.font.Font('retro_computer_personal_use.ttf', 30)
    name_game_rendered = font_name_game.render('TA-TE-TI', False, white)
    font_menu = pygame.font.Font('retro_computer_personal_use.ttf', 25)
    font_menu.set_bold(True)
    exit_rendered = font_menu.render('EXIT', False, red)
    play_rendered = font_menu.render('PLAY AGAIN', False, white)

    imageOne = pygame.image.load('tateti_files/circulo.png')
    circle = pygame.transform.scale(imageOne, [80, 80])
    imageTwo = pygame.image.load('tateti_files/cruz.png')
    cross = pygame.transform.scale(imageTwo, [80, 80])
    listRect = []
    listFirstOpen = []
    exit_pos = [300, 200]
    play_again_pos = [300, 300]

    def __int__(self):
        print('init')

    # no winner 0 | winner returns 10 | board complete and no winner -1
    def check_winner(self, num):
        cont = 0
        # raya en horizontal
        for row in self.board:
            for player in row:
                if num == player:
                    cont += 1
            if cont == 3:
                return 10
            cont = 0

        # raya en vertical
        for column in range(3):
            for row in range(3):
                if num == self.board[row][column]:
                    cont += 1
            if cont == 3:
                return 10
            cont = 0

        # primer diagonal
        cont = 0
        for i in range(3):
            if self.board[i][i] == num:
                cont += 1
            if cont == 3:
                return 10

        # segunda diagonal
        cont = 0
        for i in range(3):
            if self.board[i][2 - i] == num:
                cont += 1
            if cont == 3:
                return 10

        # empate
        cont = 0
        for column in range(3):
            for row in range(3):
                if self.board[row][column] != 0:
                    cont += 1
            if cont == 9:
                return -1

    def menu(self):
        self.window.fill(self.black)
        self.window.blit(self.exit_rendered, self.exit_pos)
        self.window.blit(self.play_rendered, self.play_again_pos)
        self.inMenu = True

    def game_start(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.name_game_rendered, self.title_pos)
        self.listRect = [pygame.draw.rect(self.window, (8, 47, 99), (230, 130, 340, 340)),
                         pygame.draw.rect(self.window, (188, 196, 208), (240, 140, 100, 100)),
                         pygame.draw.rect(self.window, (188, 196, 208), (350, 140, 100, 100)),
                         pygame.draw.rect(self.window, (188, 196, 208), (460, 140, 100, 100)),
                         pygame.draw.rect(self.window, (188, 196, 208), (240, 250, 100, 100)),
                         pygame.draw.rect(self.window, (188, 196, 208), (350, 250, 100, 100)),
                         pygame.draw.rect(self.window, (188, 196, 208), (460, 250, 100, 100)),
                         pygame.draw.rect(self.window, (188, 196, 208), (240, 360, 100, 100)),
                         pygame.draw.rect(self.window, (188, 196, 208), (350, 360, 100, 100)),
                         pygame.draw.rect(self.window, (188, 196, 208), (460, 360, 100, 100))]
        self.listFirstOpen = [True, True, True, True, True, True, True, True, True]
        self.draw = 1
        self.winner = 0
        self.inMenu = False
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        rect_circle = pygame.draw.rect(self.window, self.light_green, (50, 230, 150, 200))
        rect_cross = pygame.draw.rect(self.window, self.light_red, (600, 230, 150, 200))
        self.window.blit(self.circle, self.circle.get_rect(center=rect_circle.center))
        self.window.blit(self.cross, self.cross.get_rect(center=rect_cross.center))

    def main_tateti(self):
        self.game_start()
        pygame.time.delay(500)
        while self.run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_start()
                        self.draw = 1
                        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        self.winner = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    rect_cross = pygame.draw.rect(self.window, self.black, (600, 230, 150, 200))
                    position = pygame.mouse.get_pos()
                    if self.winner == 0:
                        if self.listRect[1].collidepoint(position) and self.listFirstOpen[0]:
                            if self.draw == 1:
                                self.window.blit(self.circle, [250, 150])
                                self.draw = 2
                                self.board[0][0] = 1
                            else:
                                self.window.blit(self.cross, [250, 150])
                                self.draw = 1
                                self.board[0][0] = 2
                            self.listFirstOpen[0] = False
                        if self.listRect[2].collidepoint(position) and self.listFirstOpen[1]:
                            if self.draw == 1:
                                self.window.blit(self.circle, [360, 150])
                                self.draw = 2
                                self.board[0][1] = 1
                            else:
                                self.window.blit(self.cross, [360, 150])
                                self.draw = 1
                                self.board[0][1] = 2
                            self.listFirstOpen[1] = False
                        if self.listRect[3].collidepoint(position) and self.listFirstOpen[2]:
                            if self.draw == 1:
                                self.window.blit(self.circle, [470, 150])
                                self.draw = 2
                                self.board[0][2] = 1
                            else:
                                self.window.blit(self.cross, [470, 150])
                                self.draw = 1
                                self.board[0][2] = 2
                            self.listFirstOpen[2] = False
                        if self.listRect[4].collidepoint(position) and self.listFirstOpen[3]:
                            if self.draw == 1:
                                self.window.blit(self.circle, [250, 260])
                                self.draw = 2
                                self.board[1][0] = 1
                            else:
                                self.window.blit(self.cross, [250, 260])
                                self.draw = 1
                                self.board[1][0] = 2
                            self.listFirstOpen[3] = False
                        if self.listRect[5].collidepoint(position) and self.listFirstOpen[4]:
                            if self.draw == 1:
                                self.window.blit(self.circle, [360, 260])
                                self.draw = 2
                                self.board[1][1] = 1
                            else:
                                self.window.blit(self.cross, [360, 260])
                                self.draw = 1
                                self.board[1][1] = 2
                            self.listFirstOpen[4] = False
                        if self.listRect[6].collidepoint(position) and self.listFirstOpen[5]:
                            if self.draw == 1:
                                self.window.blit(self.circle, [470, 260])
                                self.draw = 2
                                self.board[1][2] = 1
                            else:
                                self.window.blit(self.cross, [470, 260])
                                self.draw = 1
                                self.board[1][2] = 2
                            self.listFirstOpen[5] = False
                        if self.listRect[7].collidepoint(position) and self.listFirstOpen[6]:
                            if self.draw == 1:
                                self.window.blit(self.circle, [250, 370])
                                self.draw = 2
                                self.board[2][0] = 1
                            else:
                                self.window.blit(self.cross, [250, 370])
                                self.draw = 1
                                self.board[2][0] = 2
                            self.listFirstOpen[6] = False
                        if self.listRect[8].collidepoint(position) and self.listFirstOpen[7]:
                            if self.draw == 1:
                                self.window.blit(self.circle, [360, 370])
                                self.draw = 2
                                self.board[2][1] = 1
                            else:
                                self.window.blit(self.cross, [360, 370])
                                self.draw = 1
                                self.board[2][1] = 2
                            self.listFirstOpen[7] = False
                        if self.listRect[9].collidepoint(position) and self.listFirstOpen[8]:
                            if self.draw == 1:
                                self.window.blit(self.circle, [470, 370])
                                self.draw = 2
                                self.board[2][2] = 1
                            else:
                                self.window.blit(self.cross, [470, 370])
                                self.draw = 1
                                self.board[2][2] = 2
                            self.listFirstOpen[8] = False
                    if self.exit_rendered.get_rect(topleft=self.exit_pos).collidepoint(position) and self.winner != 0:
                        self.run = False
                    if self.play_rendered.get_rect(
                            topleft=self.play_again_pos).collidepoint(position) and self.winner != 0:
                        self.game_start()
                    if self.draw == 1 and not self.inMenu:
                        rect = pygame.draw.rect(self.window, self.light_green, (50, 230, 150, 200))
                        self.window.blit(self.circle, self.circle.get_rect(center=rect.center))
                    if self.draw == 2 and not self.inMenu:
                        rect = pygame.draw.rect(self.window, self.light_green, (50, 230, 150, 200))
                        self.window.blit(self.cross, self.cross.get_rect(center=rect.center))
            pygame.display.update()
            if self.check_winner(1) == -1:
                pygame.time.delay(2000)
                self.window.fill(self.black)
                winner_rendered = self.font_winner.render('TIE', False, self.red)
                self.window.blit(winner_rendered, [350, 230])
                pygame.display.update()
                pygame.time.delay(2000)
                self.window.fill(self.black)
                self.game_start()
            if self.check_winner(1) == 10:
                self.winner = 1
            if self.check_winner(2) == 10:
                self.winner = 2
            if self.winner == 1 or self.winner == 2:
                if not self.inMenu:
                    pygame.time.delay(1800)
                    self.window.fill(self.black)
                    winner_rendered = self.font_winner.render('PLAYER  ' + str(self.winner) + '  WON', False, self.red)
                    self.window.blit(winner_rendered, [170, 230])
                    pygame.display.update()
                    pygame.time.delay(1500)
                    self.menu()
                    pygame.display.update()


# main
def main_game():
    pygame.display.set_caption("TA-TE-TI")
    pygame.display.set_icon(pygame.image.load('tateti_files/icon_tateti.ico'))
    game = Tateti()
    game.main_tateti()
