
import time

import random

# * CHECK WINNER * #

def end_game(board,current_player):
    
    for row in range(6):
        
        for col in range(7):
            
            try:
                
                if all(board[row][col+i] == current_player for i in range(4)):
                    
                    return True
                
                elif all(board[row+i][col] == current_player for i in range(4)):
                    
                    return True
                
            except:
                
                pass
            
    return False


def equal(board):

    return all(all(cell != 0 for cell in row) for row in board)


class Node:
    
    def __init__(self,board,current_player,parent=None,data=0,children=[],Max=True,depth=0):
        
        self.board = board
        
        self.current_player = current_player
        
        self.data = data
        
        self.parent = parent
        
        self.children = children
        
        self.Max = Max
        
        self.depth = depth
        

def tree(root):
    
    root.data = root.current_player if end_game(board=root.board, current_player= root.current_player) else 0
    
    if root.data != 0:
        
        return root
    
    if root.depth == 6: # * 5 AND 6 ARE OK * #
        
        return root
    
    possible_boards = []
    
    col_range = [6,5,4,3,2,1,0]
    
    random.shuffle(col_range)
    
    for col in col_range:
        
        for row in range(5,-1,-1):
            
            if root.board[row][col] == 0:
                
                board = [ite[:] for ite in root.board]
                
                board[row][col] = -1*root.current_player
                
                possible_boards.append(board)
                
                break
            
    for board in possible_boards:
        
        child = Node(board=board,parent=root,Max= not root.Max , depth= root.depth + 1 , current_player= -1 * root.current_player,children=[])
        
        child = tree(root=child)
        
        root.children.append(child)
            
    return root


def Mini_Max(root,depth):

    if len(root.children) == 0:
        
        return root

    if root.Max:
        
        max_eval = float('-inf')
        
        for child in root.children:
            
            if max_eval < Mini_Max(child,depth=depth+1).data:
                
                max_eval = Mini_Max(child,depth=depth+1).data
                
                root.data = max_eval
                
                if depth == 0:
                    
                    root.board = Mini_Max(child,depth=depth+1).board
                
        return root
        
    else:
        
        min_eval = float('inf')
        
        for child in root.children:
            
            if min_eval > Mini_Max(child,depth=depth+1).data:
                
                min_eval = Mini_Max(child,depth=depth+1).data
                
                root.data = min_eval
                
                if depth == 0:
                
                    root.board = Mini_Max(child,depth=depth+1).board
                
        return root
    

def alpha_beta(root,depth,alpha,beta):
    
    if len(root.children) == 0:
        
        return root
    
    if root.Max:
        
        value = float('-inf')
        
        for child in root.children:
            
            if value < alpha_beta(child,depth=depth+1,alpha=alpha,beta=beta).data:
                
                value = alpha_beta(child,depth=depth+1,alpha=alpha,beta=beta).data
                
                root.data = value
                
                if depth == 0:

                    root.board = alpha_beta(child,depth=depth+1,alpha=alpha,beta=beta).board
                
                alpha = max(alpha,value)
                
                if alpha >= beta:
                    
                    print('Max Pruning')
                
                    break
                
        return root
    
    else:
        
        value = float('inf')
        
        for child in root.children:
            
            if value > alpha_beta(child,depth=depth+1,alpha=alpha,beta=beta).data:
                
                value = alpha_beta(child,depth=depth+1,alpha=alpha,beta=beta).data
                
                root.data = value
                
                if depth == 0:
                    
                    root.board = alpha_beta(child,depth=depth+1,alpha=alpha,beta=beta).board
                    
                beta = min(beta,value)
                    
                if beta <= alpha:
                    
                    print('Min Pruning')
                    
                    break
                
        return root