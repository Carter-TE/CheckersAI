import functions



class Piece:
    def __init__(self, p, board, team='b', queen=False):
        self.pos = p  # Algebraic notation
        #self.board = board
        self.team = team
        self.moves = []
        self.queen = queen
        self.direction = 1
        if team == 'w':
            self.direction = -1  

    def move(self, space):
        self.pos = space

"""     @property
    def team(self):
        return self.team
    
    @team.setter
    def team(self, t):
        self.team = t """