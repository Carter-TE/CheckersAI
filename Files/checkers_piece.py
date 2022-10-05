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



