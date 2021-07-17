import pygame,sys

class Paddle:
    def __init__(self,win,x,y,w,h):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw_player(self):
        global player_rect
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        player_rect = self.rect
        pygame.draw.rect(self.win,"white",player_rect)

    def move_player_up(self):
        self.y -= 4


    def move_player_down(self):
        self.y += 4


class Opponent(Paddle):
    def __init__(self, win, x, y, w, h):
        super().__init__(win, x, y, w, h)

    def draw_opponent(self):
        global opponent_rect
        self.opponent_rect = pygame.Rect(self.x, self.y, self.w, self.h)
        opponent_rect = self.opponent_rect
        pygame.draw.rect(self.win, "white", opponent_rect)

    def opponent_ai(self):
        global ball_rect
        if ball_rect.top <= opponent_rect.top:
            self.y -= 2
        if ball_rect.bottom >= opponent_rect.bottom:
            self.y += 2

class Ball(Paddle):
    def __init__(self, win, x, y, w, h):
        super().__init__(win, x, y, w, h)
        self.dx = 3
        self.dy = 3

    def draw_ball(self):
        global ball_rect
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        ball_rect = self.rect
        pygame.draw.ellipse(self.win, "white", ball_rect)

    def move_ball(self):
        self.x += self.dx
        self.y += self.dy

    def ball_collision(self):
        global opponent_rect,player_rect
        if self.rect.colliderect(opponent_rect):
            self.x += -5
            self.dx *= -1
        if self.rect.colliderect(player_rect):
            self.x += 5
            self.dx *= -1

        if self.x >= 800 or self.x <= 0:
            self.x = 400
            self.y = 300
            self.dx *= -1
        if self.y >= 570 or self.y <= 0:
            self.dy *= -1

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800,600))
        self.player = Paddle(self.surface,10,200,20,100)
        self.opponent =Opponent(self.surface,770,200,20,100)
        self.ball = Ball(self.surface,400,300,30,30)
        self.score_a = 0
        self.score_b = 0
        self.font = pygame.font.Font("freesansbold.ttf", 29)
        self.opponent_score = self.font.render(f"Opponent Score: {self.score_a}", True, (200, 200, 200))
        self.player_score = self.font.render(f"Player Score: {self.score_b}", True, (200, 200, 200))
        self.FPS = pygame.time.Clock()

    def game_score(self):
        if self.ball.x <= 2:
            self.score_a += 1
            self.opponent_score = self.font.render(f"Opponent Score: {self.score_a}", True, (200, 200, 200))
        if self.ball.x >= 798:
            self.score_b += 1
            self.player_score = self.font.render(f"Player Score: {self.score_b}", True, (200, 200, 200))

    def game_play(self):
        self.surface.fill("black")
        self.player.draw_player()
        self.opponent.draw_opponent()
        self.ball.draw_ball()
        self.ball.move_ball()
        self.ball.ball_collision()
        self.opponent.opponent_ai()
        self.game_score()
        self.surface.blit(self.opponent_score,(50,50))
        self.surface.blit(self.player_score,(540,50))
        pygame.draw.line(self.surface,"white",(400,0),(400,800),9)
        pygame.draw.circle(self.surface,"white",(400,300),90,90)
        pygame.draw.circle(self.surface,"black",(400,300),80,80)
        pygame.draw.line(self.surface, "white", (400, 0), (400, 800), 9)
        pygame.display.update()
        self.FPS.tick(60)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.player.y > 1:
                self.player.move_player_up()
            if keys[pygame.K_DOWN] and self.player.y < 498:
                self.player.move_player_down()

            self.game_play()

game = Game()
game.run()
