"""paddles.py"""

import pygame
from game.settings import (
    DEFAULT_COLOR,
    PADDLE_HEIGHT,
    PADDLE_OFFSET,
    PADDLE_VELOCITY,
    PADDLE_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class Paddle:
    """Paddle class"""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        """draw the paddles"""
        pygame.draw.rect(screen, DEFAULT_COLOR, (self.x, self.y, self.width, self.height))

    def move(self, direction):
        """move the paddles"""
        if direction == "up":
            self.y -= PADDLE_VELOCITY
        elif direction == "down":
            self.y += PADDLE_VELOCITY

    def reset(self):
        """location of the paddles at start"""
        if self.x < SCREEN_WIDTH / 2:
            # Left side
            paddle_x = PADDLE_OFFSET
        else:
            paddle_x = SCREEN_WIDTH - PADDLE_WIDTH - PADDLE_OFFSET
        paddle_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
        self.x = paddle_x
        self.y = paddle_y
