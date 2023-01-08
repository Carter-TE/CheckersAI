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

    def select_move(self, board, team, depth):
        """
        Selects the piece with the move that evaluates to the highest board evaluation
        Calls minimax for moves on each piece"""

        
        
        moves_per_piece = self.compute_moves(board, team)

        if team == 'b':
            maximizing = True
            evaluation = float('-inf')
        else:
            maximizing = False
            evaluation = float('inf')

        for piece in moves_per_piece.keys():
           evaluation = self.minimax(maximizing, depth, board, piece)
        
        piece_to_move = Piece(None,None,team)
        piece_to_move.best_move = {' ':evaluation}
        for piece in moves_per_piece.keys():
            if maximizing:
                if list(piece.best_move.values())[0] > list(piece_to_move.best_move.values())[0]:
                    piece_to_move = piece

            else: 
                if list(piece.best_move.values())[0] < list(piece_to_move.best_move.values())[0]:
                    piece_to_move = piece
        
        return piece_to_move

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
                

    def minimax(self, maximizing, depth, temp_board:Board, piece:Piece):
        """
        Returns the best move for a specific piece"""

        if depth == 0 or len(temp_board.get_pieces('b')) == 0 or len(temp_board.get_pieces('w')) == 0:
            return self.evaluate(temp_board)

        if maximizing:
            for move in piece.moves:
                temp = Board(temp_board)
                temp.move(piece.pos, move)
                current_eval = self.select_move(temp, 'w', depth-1)
                max_eval = max(list(piece.best_move.values())[0], list(current_eval.best_move.values())[0])

                if max_eval == list(current_eval.best_move.values())[0]:
                    piece.best_move = {move:max_eval}
            return float('-inf')

        
        else: 
            for move in piece.moves:
                temp = Board(temp_board)
                temp.move(piece.pos, move)
                current_eval = self.select_move(temp, 'b', depth-1)
                min_eval = min(list(piece.best_move.values())[0], list(current_eval.best_move.values())[0])

                if min_eval == list(current_eval.best_move.values())[0]:
                    piece.best_move = {move:min_eval}
            
            return float('inf')
                
                
        
        

    """ def minimax(self, maximizing, depth, temp_board:Board):

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
            
            return min_eval """
