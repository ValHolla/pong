import sys
from random import choice

import pygame
from game.ball import Ball
from game.paddles import Paddle
from game.settings import (
    BALL_RADIUS,
    FPS,
    PADDLE_HEIGHT,
    PADDLE_OFFSET,
    PADDLE_START_Y,
    PADDLE_VELOCITY,
    PADDLE_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WINNING_SCORE,
)
from game.user_interface import UserInterface

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")


class Pong:
    def __init__(self):
        self.playing = True
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.left_score = 0
        self.right_score = 0
        self.ball_moving = False
        self.scored = False
        self.winner = ""
        self.direction = choice(["left", "right"])
        self.user_interface = UserInterface()
        self.left_paddle = Paddle(PADDLE_OFFSET, PADDLE_START_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.right_paddle = Paddle(
            SCREEN_WIDTH - PADDLE_WIDTH - PADDLE_OFFSET, PADDLE_START_Y, PADDLE_WIDTH, PADDLE_HEIGHT
        )
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS)

    def new_game(self):
        SCREEN.fill((0, 0, 0))
        self.user_interface.show_score(SCREEN, self.left_score, self.right_score)
        self.user_interface.draw_field(SCREEN)
        self.left_paddle.draw(SCREEN)
        self.right_paddle.draw(SCREEN)
        self.ball.draw(SCREEN)

    def move_paddles(self, keys, left_paddle, right_paddle):
        if keys[pygame.K_w] and left_paddle.y - PADDLE_VELOCITY >= 0:
            left_paddle.move("up")
        if keys[pygame.K_s] and left_paddle.y + PADDLE_VELOCITY + left_paddle.height <= SCREEN_HEIGHT:
            left_paddle.move("down")

        if keys[pygame.K_UP] and right_paddle.y - PADDLE_VELOCITY >= 0:
            right_paddle.move("up")
        if keys[pygame.K_DOWN] and right_paddle.y + PADDLE_VELOCITY + right_paddle.height <= SCREEN_HEIGHT:
            right_paddle.move("down")

    def update_score(self):
        if self.ball.x - BALL_RADIUS <= 0:
            self.scored = True
            self.direction = "right"
            self.right_score += 1
        elif self.ball.x + BALL_RADIUS >= SCREEN_WIDTH:
            self.scored = True
            self.direction = "left"
            self.left_score += 1
        if self.scored:
            self.ball_moving = False
            self.ball.reset()
            self.left_paddle.reset()
            self.right_paddle.reset()
            self.scored = False

    def show_game_over(self):
        if self.left_score >= WINNING_SCORE:
            self.game_over = True
            self.winner = "left"
        elif self.right_score >= WINNING_SCORE:
            self.game_over = True
            self.winner = "right"
        if self.game_over:
            self.user_interface.game_over(SCREEN, self.winner)
            self.ball.reset()
            self.left_paddle.reset()
            self.right_paddle.reset()
            self.left_score = 0
            self.right_score = 0
            self.game_over = False


def main():
    game = Pong()

    while game.playing:
        game.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game.ball_moving = True
        game.new_game()
        game.move_paddles(keys, game.left_paddle, game.right_paddle)
        game.ball.move(game.direction, game.ball_moving)
        game.ball.collide(game.left_paddle, game.right_paddle)
        game.update_score()
        game.show_game_over()
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
