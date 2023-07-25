import pygame
import numpy as np
from Player import *
from Board import BoardUtility

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

RED = (255, 0, 0)
BG_COLOR = (20, 200, 160)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)


class XO:

    def __init__(self, player1, player2):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('TIC TAC TOE')
        self.screen.fill(BG_COLOR)
        self.player1 = player1
        self.player2 = player2
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS))

    def draw_lines(self):
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)

        pygame.draw.line(self.screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

        pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)

        pygame.draw.line(self.screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 1:
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, (
                        int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                       CIRCLE_RADIUS,
                                       CIRCLE_WIDTH)
                elif self.board[row][col] == 2:
                    pygame.draw.line(self.screen, CROSS_COLOR,
                                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                    pygame.draw.line(self.screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                     CROSS_WIDTH)

    def available_square(self, row, col):
        return self.board[row][col] == 0

    def is_board_full(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 0:
                    return False

        return True

    def restart(self):
        self.screen.fill(BG_COLOR)
        self.draw_lines()
        print(self.board)
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS))

    def check_win(self, player):
        for col in range(BOARD_COLS):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                self.draw_vertical_winning_line(col, player)
                return True

        for row in range(BOARD_ROWS):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                self.draw_horizontal_winning_line(row, player)
                return True

        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            self.draw_asc_diagonal(player)
            return True

        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            self.draw_desc_diagonal(player)
            return True

        return False

    def draw_vertical_winning_line(self, col, player):
        posX = col * SQUARE_SIZE + SQUARE_SIZE // 2

        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(self.screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)

    def draw_horizontal_winning_line(self, row, player):
        posY = row * SQUARE_SIZE + SQUARE_SIZE // 2

        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(self.screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH)

    def draw_asc_diagonal(self, player):
        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(self.screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)

    def draw_desc_diagonal(self, player):
        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(self.screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)

    def play_game_with_gui(self):
        self.draw_lines()
        self.draw_figures()
        turn = np.random.randint(0, 2)
        print('player1 is O. player2 is X.')
        print(f'player{turn + 1} goes first.')
        while True:
            if turn == 0:
                row, col = self.player1.play(self.board)
                if self.available_square(row, col):
                    BoardUtility.make_move(self.board, row, col, self.player1.piece)
            elif turn == 1:
                row, col = self.player2.play(self.board)
                if self.available_square(row, col):
                    BoardUtility.make_move(self.board, row, col, self.player2.piece)
            turn = 1 - turn
            self.draw_figures()
            pygame.display.update()
            if BoardUtility.has_player_won(self.board, 1):
                print("PLAYER 1 WINS!")
                win = 1
                pygame.time.wait(30000)
                self.restart()
                break
            if BoardUtility.has_player_won(self.board, 2):
                print("PLAYER 2 WINS!")
                win = 2
                pygame.time.wait(30000)
                self.restart()
                break
            if BoardUtility.is_draw(self.board):
                win = -1
                print("NO ONE WON DRAW!")
                pygame.time.wait(30000)
                self.restart()
                break

        return win

    def play_game_without_gui(self):
        turn = np.random.randint(0, 2)
        print('player1 is O. player2 is X.')
        print(f'player{turn + 1} goes first.')
        while True:
            if turn == 0:
                row, col = self.player1.play(self.board)
                BoardUtility.make_move(self.board, row, col, self.player1.piece)
            elif turn == 1:
                row, col = self.player2.play(self.board)
                BoardUtility.make_move(self.board, row, col, self.player2.piece)
            turn = 1 - turn
            if BoardUtility.has_player_won(self.board, 1):
                print("PLAYER 1 WINS!")
                win = 1
                self.restart()
                break
            if BoardUtility.has_player_won(self.board, 2):
                print("PLAYER 2 WINS!")
                win = 2
                self.restart()
                break
            if BoardUtility.is_draw(self.board):
                win = -1
                print("NO ONE WON DRAW!")
                self.restart()
                break

        return win
