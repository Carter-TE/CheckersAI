from functions import to_index, to_coordinate
from checkers_board import Board
from checkers_piece import Piece


class Ai:
    def __init__(self, board:Board, maximizing=True):
        self.maximizing = maximizing
        if maximizing: 
            self.team = 'b'
        else:
            self.team = 'w'
        self.board = board
        self.calculated_moves={}
        #self.moves = {} {Piece: [all possible "to" spaces]}


    

    def compute_moves(self, board:Board, team):
        moves = {}
        for piece in board.get_pieces(team):
            p_moves = board.calc_moves(piece)
            #Adds only pieces that have moves
            if p_moves != []:                
                moves[piece] = p_moves
        return moves

    def select_move(self):
        pass

    def evaluate(self, board:Board):
        tot = board.evaluate()
        moves = {**self.compute_moves(board, 'b'),  **self.compute_moves(board, 'w')}

        for piece in moves:
            for move in moves[piece]:
                if abs(int(move[1]) - int(piece.pos[1])) > 1:
                    if piece.team == 'b':
                        tot += .5
                    else:
                        tot -= .5
        return tot
                

        

    def minimax(self, maximizing, depth, temp_board:Board):

        if depth == 0 or len(temp_board.get_pieces('b')) == 0 or len(temp_board.get_pieces('w')) == 0:
            return self.evaluate(temp_board)
        
        if maximizing:
            max_eval = float('-inf')
            moves_per_piece = self.compute_moves(temp_board,'b')
            for piece in moves_per_piece:
                for move in moves_per_piece[piece]:
                    temp = Board(temp_board)
                    temp.move(piece.pos, move)
                    c_eval = self.minimax(False, depth-1, temp)
                    max_eval = max(max_eval, c_eval)
            return max_eval
                

        else:
            min_eval = float('inf')
            moves_per_piece = self.compute_moves(temp_board,'w')
            for piece in moves_per_piece:
                for move in moves_per_piece[piece]:
                    temp = Board(temp_board)
                    temp.move(piece.pos, move)
                    c_eval = self.minimax(True, depth-1, temp)
                    min_eval = min(min_eval, c_eval)
            
            return min_eval
