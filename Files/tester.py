from functions import to_index, to_coordinate
from checkers_board import Board
from minimax_ai import Ai
if __name__=='__main__':
    b_arr =  [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', 'b', ' ', 'b', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', 'w', ' '],
                    [' ', 'w', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    b = Board(arr=b_arr)
    
    ai = Ai(b)
    print(b)
    
    """ print(b.calc_moves(b.get_piece("b6")))
    print(to_index("b6")+" "+to_index('d4')+" "+to_index()) """
    print(ai.evaluate(b))
    e = ai.minimax(True, 3, b)
    print(e)