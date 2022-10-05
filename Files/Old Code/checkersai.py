import math
from board import Board
from checkers_piece import Piece
from functions import *


class CheckersAI:
    def __init__(self, board, team='b'):
        self.board = board
        self.team = team

        self.pieces = self.board.get_pieces(self.team)

        for piece in self.pieces:
            if (self.board.get_display_piece(piece.pos).isupper()):
                piece.make_queen()

        self.moves = {}
        self.weight_moves = {}

    def compute_move(self):
        self.pieces = self.board.get_pieces(self.team)
        self.get_moves()
        self.weight_moves = {}
        for piece in self.moves.keys():
            for move in self.moves[piece]:
                weight = 0

                if self.is_jump(piece.pos, move):
                    weight += 1
                weight += self.safe_move(piece.pos, move)
                #print(piece.pos, move, weight)
                key = piece.pos+move
                self.weight_moves[key] = weight
        move = max(self.weight_moves, key=self.weight_moves.get)
        print('AI move: ',move)
        self.board.move(move[:2], move[2:])


    def get_moves(self, piece=None):
        """
        Returns list of all possible moves of a specific piece

        :param piece: Space location as string of 'row col' indices
        :return: list: all possible moves of specified piece
        """
        self.moves = {}
        for piece in self.pieces:
            piece.calc_moves()
            if not piece.get_moves():
                continue
            self.moves[piece] = piece.get_moves()

        return self.moves

    def is_jump(self, piece, move):
        """
        Returns true if the move for the specified piece is a jump

        :param piece: piece location
        :param move: location to move to
        :return: Boolean
        """
        try:
            piece = to_index(piece)
            move = to_index(move)
        except IndexError as err:
            print(err)
            return False

        if abs(int(piece) - int(move)) != 11 and abs(int(piece) - int(move)) != 9:
            return True
        return False


    def safe_move(self, piece, move):
        # Need to check if spots are friendly and for queens and if piece has been jumped

        temp_board = Board(self.board)
        #print(temp_board)
        temp_board.move(piece, move)
        #print(temp_board)
        try:
            move_index = int(to_index(move))
        except IndexError as err:
            print(err)

        tl = str(move_index - 11)
        if len(tl) < 2:
            tl = '0' + tl
        tr = str(move_index - 9)
        if len(tr) < 2:
            tr = '0' + tr
        bl = str(move_index + 9)
        if len(bl) < 2:
            bl = '0' + bl
        br = str(move_index + 11)
        if len(br) < 2:
            br = '0' + br

        try:
            tl = to_coordinate(tl)
            tr = to_coordinate(tr)
            bl = to_coordinate(bl)
            br = to_coordinate(br)
        except IndexError as err:
            #print(err)
            return 1

        # all surrounding spaces
        surrounding = [tl, br, tr, bl]

        # occupied surrounding spaces only
        temp = [temp_board.get_piece(x) for x in surrounding if temp_board.get_piece(x) is not None]
        if len(temp) < 1:
            return 1

        # surrounding spaces occupied by other player only
        temp = [x for x in temp if x.team != self.team]
        if len(surrounding) < 1:
            return 1

        # check if it can be jumped
        for x in temp:
            x.calc_moves()
            moves = x.get_moves()
            if any(i in moves for i in surrounding):
                return -1
        return 1

        #surr_pcs =






if __name__ == '__main__':
    b = Board()
    #print(b)
    player1 = CheckersAI(b)
    player2 = CheckersAI(b, team='w')
    count = 1
    while True:
        legal = False
        completed_move = False
        print('Round ',count)
        print(b)

        while not completed_move:
            player_move = input('Player move (startEnd): ')
            while not legal:
                try:
                    b.pcs[player_move[:2]]
                except KeyError as err:
                    print('No piece on space')
                    player_move = input('Move (startEnd): ')
                    continue

                legal = True
            try:
                b.move(player_move[:2], player_move[2:])
            except ValueError as err:
                print(err)
                continue
            completed_move = True

        print(b)
        player1.compute_move()
        count += 1

