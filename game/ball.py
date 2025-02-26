"""ball.py"""

from random import randrange

import pygame
from game.settings import BALL_VELOCITY, DEFAULT_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH


class Ball:
    """ball class"""

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_velocity = BALL_VELOCITY
        self.y_velocity = randrange(-BALL_VELOCITY, BALL_VELOCITY) / 2

    def draw(self, screen):
        """draw the ball"""
        pygame.draw.circle(screen, DEFAULT_COLOR, (self.x, self.y), self.radius)

    def move(self, direction, moving):
        """move the ball"""
        multiplier = 1
        if moving:
            if direction == "left":
                multiplier = -1
            elif direction == "right":
                multiplier = 1
            self.x += self.x_velocity * multiplier
            self.y += self.y_velocity

    def reset(self):
        """reset position"""
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.x_velocity = BALL_VELOCITY
        self.y_velocity = randrange(-BALL_VELOCITY, BALL_VELOCITY) / 2

    def calculate_offset(self, paddle):
        """calculate the y velocity off the paddle"""
        middle_y = paddle.y + paddle.height / 2
        difference_in_y = middle_y - self.y
        reduction_factor = (paddle.height / 2) / BALL_VELOCITY

        return difference_in_y / reduction_factor

    def collide(self, left_paddle, right_paddle):
        """collisions"""
        left_ball_x = self.x - self.radius
        right_ball_x = self.x + self.radius

        # roof and floor
        if self.y + self.radius >= SCREEN_HEIGHT:
            self.y_velocity *= -1
        elif self.y - self.radius <= 0:
            self.y_velocity *= -1

        if self.y >= left_paddle.y and self.y <= left_paddle.y + left_paddle.height:
            if left_ball_x <= left_paddle.x + left_paddle.width:
                self.x_velocity *= -1
                self.y_velocity = -1 * self.calculate_offset(left_paddle)

        if self.y >= right_paddle.y and self.y <= right_paddle.y + right_paddle.height:
            if right_ball_x >= right_paddle.x:
                self.x_velocity *= -1
                self.y_velocity = -1 * self.calculate_offset(right_paddle)
