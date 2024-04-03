import os

# folders
GAME_DIR = os.path.dirname(__file__)
FONT_DIR = os.path.join(GAME_DIR, "fonts")

# game config
FPS: int = 60
SCREEN_WIDTH: int = 700
SCREEN_HEIGHT: int = 500
WINNING_SCORE: int = 10
GAME_FONT: str = os.path.join(FONT_DIR, "font.ttf")
SCORE_SIZE: int = 50
SCORE_OFFSET: int = 20
DEFAULT_COLOR: tuple = (255, 255, 255)
DASH_SPACE: int = SCREEN_HEIGHT // 20
CENTER_LINE_WIDTH: int = 5

# paddle config
PADDLE_WIDTH: int = 20
PADDLE_HEIGHT: int = 100
PADDLE_OFFSET: int = 10
PADDLE_VELOCITY: int = 4
PADDLE_START_Y: int = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2

# ball config
BALL_RADIUS: int = 7
BALL_VELOCITY: int = 5
