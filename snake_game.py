# james molamphy jmolamph
import pygame
import time
import random

import food
import snake


class SnakeGame:
    def __init__(self):
        # screen attributes
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        # color attributes
        self.BKGD_COLOR = (40, 40, 40)
        self.SNAKE_COLOR = (200, 200, 200)
        self.LOSE_COLOR = (185, 0, 0)
        self.WIN_COLOR = (80, 185, 80)
        self.MSG_COLOR = (120, 120, 120)
        self.FOOD_COLOR = (80, 185, 80)

        # snake attributes
        self.SNAKE_BLOCK_SIZE = 20
        self.snake = None
        self.snake_x1_change = 0
        self.snake_y1_change = 0

        # food attributes
        self.food = None

        # game attributes
        self.PROMPT_FONT = None
        self.SCORE_FONT = None
        self.FONT_SIZE = 24
        self.SCREEN = None
        self.running = None
        self.game_lost = None
        self.last_direction = None

    def start_game(self):
        """
        Creates and displays the Snake Game window, then starts the gameplay loop.
        """
        # set up the game, and save the screen
        self.SCREEN = self.setup_screen()
        self.PROMPT_FONT = pygame.font.SysFont('Calibri', self.FONT_SIZE)
        self.SCORE_FONT = pygame.font.SysFont('Calibri', self.FONT_SIZE)
        self.gameplay_loop()

    def setup_screen(self):
        """
        initializes pygame and sets up screen object
        :return: screen object
        """
        # initialize pygame
        pygame.init()

        # define the dimensions of pygame screen object
        screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # set the screen's caption
        pygame.display.set_caption("James' Snake Game")

        # set the background color of the screen
        screen.fill(self.BKGD_COLOR)

        # update the display on screen
        pygame.display.flip()

        return screen

    def gameplay_loop(self):
        """
        main gameplay event loop
        :return:
        """

        # initialize variables
        self.running = True
        self.game_lost = False
        self.last_direction = None

        # initialize the snake variables
        self.create_snake()
        self.snake_x1_change = 0
        self.snake_y1_change = 0

        # initialize the food variables
        self.create_food()

        # create pygame clock
        clock = pygame.time.Clock()

        # gameplay loop until QUIT
        while self.running:

            # if the snake dies
            while self.game_lost:
                self.display_lose_screen()

            # check through game events to get snake direction
            self.check_events()

            # check if snake head is out of bounds
            self.game_lost = True if self.snake.get_x() >= self.SCREEN_WIDTH or self.snake.get_x() < 0 else self.game_lost
            self.game_lost = True if self.snake.get_y() >= self.SCREEN_HEIGHT or self.snake.get_y() < 0 else self.game_lost

            # add new snake head position to the snake's position list
            snake_head = [self.snake.get_x(), self.snake.get_y()]
            self.snake.append_list(snake_head)

            # if the snake did not eat food, delete tail block to maintain size
            if len(self.snake.get_list()) > self.snake.get_length():
                self.snake.delete_tail()

            # if the snake ran into the food, respawn a new food and update the length of the snake
            if self.food.get_x() == self.snake.get_x() and self.food.get_y() == self.snake.get_y():
                self.food.spawn()
                self.snake.set_length()

            # if the snake ran into itself, end game
            for block in self.snake.get_list()[:-1]:
                if block == snake_head:
                    self.game_lost = True

            # update snake coordinates
            self.snake.set_position(self.snake_x1_change, self.snake_y1_change)

            # update screen with snake, food, and score
            self.SCREEN.fill(self.BKGD_COLOR)
            pygame.draw.rect(self.SCREEN, self.FOOD_COLOR,
                             [self.food.get_x(), self.food.get_y(), self.SNAKE_BLOCK_SIZE, self.SNAKE_BLOCK_SIZE])
            self.display_snake()
            self.show_score()
            pygame.display.update()

            clock.tick(self.snake.get_speed())

        # if end of gameplay loop, display thank you message to user and quit the program
        self.display_message("Thanks for playing!", self.MSG_COLOR, 1)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()

    def display_lose_screen(self):

        # display lose message on screen
        self.SCREEN.fill(self.BKGD_COLOR)
        self.display_message("  You Lost!", self.LOSE_COLOR, 1)
        self.display_message("Press C to play again.", self.LOSE_COLOR, 2)
        self.display_message("  Press Q to quit.", self.LOSE_COLOR, 3)
        pygame.display.update()

        # check if user wants to continue or quit the game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # if they press C, continue the game
                if event.key == pygame.K_c:
                    self.gameplay_loop()

                # if they press Q, quit the game
                if event.key == pygame.K_q:
                    self.running = False
                    self.game_lost = False
                    break

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # if legal keypress, shift the snake head position in the corresponding direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.last_direction != "R":
                    self.snake_x1_change = -self.SNAKE_BLOCK_SIZE
                    self.snake_y1_change = 0
                    self.last_direction = "L"

                elif event.key == pygame.K_RIGHT and self.last_direction != "L":
                    self.snake_x1_change = self.SNAKE_BLOCK_SIZE
                    self.snake_y1_change = 0
                    self.last_direction = "R"

                elif event.key == pygame.K_UP and self.last_direction != "D":
                    self.snake_x1_change = 0
                    self.snake_y1_change = -self.SNAKE_BLOCK_SIZE
                    self.last_direction = "U"

                elif event.key == pygame.K_DOWN and self.last_direction != "U":
                    self.snake_x1_change = 0
                    self.snake_y1_change = self.SNAKE_BLOCK_SIZE
                    self.last_direction = "D"

    def display_message(self, message, text_color, position):
        """
        Displays text message on screen for user
        :param message: string
        :param text_color: (int, int, int)
        :param position: int
        :return:
        """
        msg = self.PROMPT_FONT.render(message, True, text_color)
        text_rectangle = msg.get_rect(center=(self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/4 + (position * self.FONT_SIZE)))
        self.SCREEN.blit(msg, text_rectangle)

    def show_score(self):
        """
        displays score in top left for user
        """
        value = self.SCORE_FONT.render("Your Score: {}".format(self.snake.get_length()-1), True, self.WIN_COLOR)
        self.SCREEN.blit(value, [0, 0])

    def create_food(self):
        """
        creates a new food object on the game board
        """
        self.food = food.Food(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SNAKE_BLOCK_SIZE)

    def create_snake(self):
        """
        creates a new snake object on the game board
        """
        self.snake = snake.Snake(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SNAKE_BLOCK_SIZE)

    def display_snake(self):
        """
        displays the snake's position on the screen
        """
        for block_xy in self.snake.get_list():
            pygame.draw.rect(self.SCREEN, self.SNAKE_COLOR, [block_xy[0], block_xy[1], self.SNAKE_BLOCK_SIZE, self.SNAKE_BLOCK_SIZE])
