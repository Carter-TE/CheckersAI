from checkers_piece import Piece
from functions import to_index, to_coordinate
import copy

class Board():

    def __init__(self, board=None, game=None):
        if game == 'chess':
            pass
        else:
            if board is None:
                self.board_arr=[[' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
                                ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
                                [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],
                                [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
                                ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' ']]
                
                self.pcs = {}   

                # Creates dictionary mapping each piece to a space on the board (Key: space, Value: piece obj)
                for row in range(len(self.board_arr)):
                    for col in range(len(self.board_arr)):
                        space = self.board_arr[row][col]
                        coords = to_coordinate(str(row) + str(col))
                        if space == 'b' or space == 'B':
                            self.pcs[coords] = Piece(coords, self, 'b')
                        elif space == 'w' or space == 'W':
                            self.pcs[coords] = Piece(coords, self, 'w')
                        if space == 'B'or space == 'W':
                            self.pcs[coords].queen = True

            else:
                self.board_arr = list(map(list,board.board_arr))
                self.pcs = copy.deepcopy(board.pcs)
                for x in self.pcs:
                    self.pcs[x].board = self

    def evaluate(self):
        tot = 0
        for piece in self.pcs.values():
            # Amount to add/subtract based on type of piece
            temp = 0
            if piece.queen:
                temp+=2
            else:
                temp+=1
            #Add or Subtract depending on team 
            if piece.team == 'w':
                tot+=temp
            else:
                tot-=temp

        return tot

    def move(self, start, to):
        """
        Moves piece from 'start' space to 'to' space

        :param start: Location  where the piece is starting from
        :param to: Location where the piece will move to
        :return: boolean: whether the piece was moved to the desired space or not
        """
        self.pcs[start].calc_moves()
        if to not in self.pcs[start].moves():
            raise ValueError('Invalid move')
        temp = self.pcs[start]
        del (self.pcs[start])
        self.pcs[to] = temp
        self.pcs[to].move(to)
        end_space = to

        try:
            start = to_index(start)
            to = to_index(to)
        except IndexError as err:
            print(err)
            return False

        r1 = int(start[0])
        c1 = int(start[1])
        r2 = int(to[0])
        c2 = int(to[1])
        temp = self.board_arr[r1][c1]
        self.board_arr[r1][c1] = ' '
        self.board_arr[r2][c2] = temp

        if abs(r1-r2) !=1:
            num = int(start)+((int(to) - int(start))//2)
            j_space = str(num)
            self.board_arr[int(j_space[0])][int(j_space[1])] = ' '
            key = to_coordinate(j_space)
            del(self.pcs[key])

        if r2 == 0 or r2 == 7:
            self.pcs[end_space].make_queen()
            self.board_arr[r2][c2] = self.board_arr[r2][c2].upper()


        return True

    def calc_moves(self, piece):
        """
        Updates move field with all possible moves the piece can make

        :return:
        """

        piece.moves = []
        pos_index = int(to_index(piece.pos))
        temp_moves = [pos_index + (9 * piece.direction), pos_index + (11 * piece.direction)]
        if piece.queen:
            temp_moves.append(pos_index - (11 * piece.direction))
            temp_moves.append(pos_index - (9 * piece.direction))

        # Formatting for moves to 0th row (top of the board)
        for i in range(len(temp_moves)):
            if len(str(temp_moves[i])) < 2:
                temp_moves[i] = '0'+str(temp_moves[i])

        # Filters moves not on board
        moves = []
        for move in temp_moves:
            try:
                m = to_coordinate(move)
            except IndexError as err:
                continue
            moves.append(m)
            del (m)

        # Filters valid moves
        for move in moves:
            if self.can_move_to(move):
                piece.moves.append(move)
                continue
            jump = piece.can_jump(move)
            if jump is not None:
                piece.moves.append(jump)
        return piece.moves

    # <editor-fold desc="possible method">
    def jumps(self, space):
        """
        Calculates whether any jumps are possible from piece located at space
        
        :param space: Space location of starting piece
        :return: list: All space locations of possible jumps or []
        """
        nums = list(space)
        row = int(nums[0])
        col = int(nums[1])
        adjacent = list()
        adjacent.append(str(row + 1) + str(col - 1))
        adjacent.append(str(row + 1) + str(col + 1))
        if self.get_display_piece(space).isupper():
            adjacent.append(str(row - 1) + str(col - 1))
            adjacent.append(str(row - 1) + str(col + 1))
        '''for i in adjacent
            if'''
    # </editor-fold>


    def can_move_to(self, space):
        """
        Returns whether the space can be moved to or not

        :param space: The space location to be checked if piece can be moved to
        :return: boolean: whether the piece can be moved to space or not
        """

        try:
            move = to_index(space)
        except IndexError as err:
            print(err)
            return False

        row = int(move[0])
        col = int(move[1])

        if self.board_arr[row][col] == ' ':
            return True
        return False

    def get_pieces(self, team):
        """
        Returns space location of all pieces on a team

        :param team: String 'b' or 'w' to determine which teams pieces to return
        :return: list: Strings of (row,col) space coordinates of each piece
        """
        return [piece for piece in self.pcs.values() if piece.team == team ]

    def get_piece(self, space):
        """
        Returns piece object located at 'space

        :param space: Board location of the piece in algebraic notation
        :return: Piece ibject
        """
        piece = self.pcs.get(space)
        return piece

    def get_display_piece(self, space):
        """
        Returns piece at specified space

        :param space: Space location in algebraic notation
        :return: String: that is displayed
        """
        try:
            ispace = to_index(space)
        except IndexError as err:
            print(err)
            return
        row = int(ispace[0])
        col = int(ispace[1])
        return self.board_arr[row][col]


    def __str__(self):
        str_rep = '    A B C D E F G H\n    ----------------\n'
        row_num = 8
        for row in self.board_arr:
            temp = str(row_num) + ' | '
            for col in row:
                space = col
                if space == ' ':
                    space = '.'
                temp += space + ' '
            str_rep += str(temp)
            str_rep += '\n'
            row_num -= 1
        return str_rep


if __name__ == '__main__':
    b = Board()
    print(b)
    p = b.get_piece("b8")
    b.calc_moves(p)
    print(p.moves)
    #index = (to_index('d9'))
    #print(index)
    #print(b.evaluate())
    # print(b.to_coordinate(71))
    # print(b.to_coordinate('00'))

    """
    print(b.move('11', '21'))
    print(b)

    for i in range(8):
        temp=[]
        for j in range(8):
            space = str(i)
            space+=(' ')
            space+=(str(j))
            temp.append(space)
        print(temp)"""
