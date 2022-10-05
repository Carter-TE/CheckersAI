import functions



class Piece:
    def __init__(self, p, board, team='b', queen=False):
        self.pos = p  # Algebraic notation
        self.board = board
        self.team = team
        self.moves = []
        self.queen = queen
        self.direction = 1
        if team == 'w':
            self.direction = -1

    

   

    def move(self, space):
        self.pos = space

    def calc_moves(self):
        """
        Updates move field with all possible moves the piece can make

        :return:
        """

        self.moves = []
        pos_index = int(functions.to_index(self.pos))
        temp_moves = [pos_index + (9 * self.direction), pos_index + (11 * self.direction)]
        if self.queen:
            temp_moves.append(pos_index - (11 * self.direction))
            temp_moves.append(pos_index - (9 * self.direction))

        # Formatting for moves to 0th row (top of the board)
        for i in range(len(temp_moves)):
            if len(str(temp_moves[i])) < 2:
                temp_moves[i] = '0'+str(temp_moves[i])

        # Filters moves not on board
        moves = []
        for move in temp_moves:
            try:
                m = functions.to_coordinate(move)
            except IndexError as err:
                continue
            moves.append(m)
            del (m)

        # Filters valid moves
        for move in moves:
            if self.board.can_move_to(move):
                self.moves.append(move)
                continue
            jump = self.can_jump(move)
            if jump is not None:
                self.moves.append(jump)

    def can_jump(self, move):
        """
        Determines whether a space can be jumped over or not

        :param move: Space to be jumped
        :return: None or space that will be jumped too
        """
        jump_space = None
        if self.board.get_display_piece(move) not in [self.team, self.team.upper(), ' ']:

            try:
                move = int(functions.to_index(move))
                space = int(functions.to_index(self.pos))
            except IndexError as err:
                print(err)
                return None
        else:
            return None

        if (move - space) == 11:
            jump_space = str(move + 11)
        elif (move - space) == 9:
            jump_space = str(move + 9)
        elif (move - space) == -11:
            jump_space = str(move - 11)
        elif (move - space) == -9:
            jump_space = str(move - 9)
        try:
            jump_space = functions.to_coordinate(jump_space)
        except IndexError:
            return None
        if self.board.can_move_to(jump_space):
            return jump_space
        return None



