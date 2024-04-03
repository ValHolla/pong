"""user_interface.py"""

import pygame
from game.settings import (
    CENTER_LINE_WIDTH,
    DASH_SPACE,
    DEFAULT_COLOR,
    GAME_FONT,
    SCORE_OFFSET,
    SCORE_SIZE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class UserInterface:
    """UI"""

    def __init__(self):
        self.game_font = pygame.font.Font(GAME_FONT, SCORE_SIZE)

    def show_score(self, screen, left_score, right_score):
        """show score"""
        left_score_text = self.game_font.render(str(left_score), 1, DEFAULT_COLOR)
        right_score_text = self.game_font.render(str(right_score), 1, DEFAULT_COLOR)

        screen.blit(left_score_text, (SCREEN_WIDTH // 4 - left_score_text.get_width() // 2, SCORE_OFFSET))
        screen.blit(
            right_score_text,
            (SCREEN_WIDTH * 3 / 4 - right_score_text.get_width() // 2, SCORE_OFFSET),
        )

    def draw_field(self, screen):
        """draw the field"""
        for dash in range(10, SCREEN_HEIGHT, DASH_SPACE):
            if dash % 2 == 0:
                pygame.draw.rect(
                    screen,
                    DEFAULT_COLOR,
                    (
                        SCREEN_WIDTH // 2 - CENTER_LINE_WIDTH // 2,
                        dash,
                        CENTER_LINE_WIDTH,
                        DASH_SPACE,
                    ),
                )

    def game_over(self, screen, winner):
        """game over screen"""
        go_message = "Game Over."
        congrats_msg = f"Congrats, {winner} player!"
        go_text = self.game_font.render(go_message, 1, DEFAULT_COLOR)
        congrats_text = self.game_font.render(congrats_msg, 1, DEFAULT_COLOR)
        screen.fill((0, 0, 0))
        screen.blit(go_text, (SCREEN_WIDTH // 2 - go_text.get_width() // 2, SCREEN_HEIGHT // 2 - go_text.get_height()))
        screen.blit(
            congrats_text,
            (SCREEN_WIDTH // 2 - congrats_text.get_width() // 2, SCREEN_HEIGHT // 2 + congrats_text.get_height()),
        )
        pygame.display.update()
        pygame.time.delay(5000)
