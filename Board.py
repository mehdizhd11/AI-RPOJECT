
import pygame

from Logic import *

import time

# Initialize Pygame
pygame.init()

# Set up the game constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
SQUARE_SIZE = 80
RADIUS = SQUARE_SIZE // 2 - 5
WINDOW_WIDTH = BOARD_WIDTH * SQUARE_SIZE
WINDOW_HEIGHT = (BOARD_HEIGHT + 1) * SQUARE_SIZE
PLAYER1_COLOR = (255, 255, 0)
PLAYER2_COLOR = (0, 255, 255)

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Connect 4")

# Function to draw the game board
def draw_board(board):
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            pygame.draw.rect(window, (0, 0, 0), (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(window, (255, 255, 255), (col * SQUARE_SIZE + RADIUS, (row + 1) * SQUARE_SIZE + RADIUS), RADIUS)

    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if board[row][col] == 1:
                pygame.draw.circle(window, PLAYER1_COLOR, (col * SQUARE_SIZE + RADIUS, (row + 1) * SQUARE_SIZE + RADIUS), RADIUS)
            elif board[row][col] == -1:
                pygame.draw.circle(window, PLAYER2_COLOR, (col * SQUARE_SIZE + RADIUS, (row + 1) * SQUARE_SIZE + RADIUS), RADIUS)

    pygame.display.update()

# Create the game board
board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

# Variable to keep track of the current player
current_player = -1

# Game loop
running = True

while running:
    
    if current_player < 0:

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
            
                mouse_x = event.pos[0]
            
                col = mouse_x // SQUARE_SIZE
            
                if board[0][col] == 0:
            
                    for row in range(BOARD_HEIGHT - 1, -1, -1):
            
                        if board[row][col] == 0:
            
                            board[row][col] = -1
                            
                            # WINNER CHECK
                            
                            if end_game(board,current_player=-1):
                                
                                running = False
                                
                                print('PLAYER WIN!')
                            
                            current_player = 1
                            
                            break
                        
    else:
        
        time.sleep(1)
            
        root = Node(board=board , current_player=-1 , children=[])
        
        root = tree(root=root)
        
        # root = Mini_Max(root=root,depth=0)
        
        root = alpha_beta(root=root,depth=0,alpha=float('-inf'),beta=float('inf'))
        
        board = [ite[:] for ite in root.board]
        
        if end_game(board=board,current_player=1):
            
            running = False
            
            print('AGENT WIN!')
            
        current_player = -1
    
    window.fill((0, 0, 0))
        
    draw_board(board)
    
    if equal(board=board):
        
        print('EQUAL!')
        
        running = False
    

time.sleep(3)
# Quit the game
pygame.quit()