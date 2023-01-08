from functions import to_index, to_coordinate
from checkers_board import Board
from minimax_ai import Ai
if __name__=='__main__':
    """ b_arr =[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', ' ', ' ', 'w', ' ', 'w', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']] """
    b = Board()
    
    ai_b = Ai(b)
    print(b)
    """ p = ai_b.select_move(b, 'b', 3)
    print(p.best_move)
    ai_w = Ai(b,False) """

    
    b_turn = True
    print(b)
    while len(b.get_pieces('b')) != 0 and len(b.get_pieces('w')) != 0:

        if b_turn:
            p = ai_b.select_move(b, 'b', 3)
            print('Black\'s Move: '+p.pos+' '+list(p.best_move.keys())[0])
            move = str(p.pos+' '+list(p.best_move.keys())[0]).split(" ")
            while(True):
                try:
                    b.move(move[0],move[1])
                    b_turn = False
                    break
                except ValueError as err:
                    move = input("Enter Valid move (Start End)").split(" ")
                    print(b.calc_moves(b.get_piece(move[0])))
                except KeyError as err:
                    print(err)
                    move = input("Enter Valid move (Start End)").split(" ")

        else:
            print("White's Move.")
            move = input("Enter move separated by space (Start End)").split(" ")
            while(True):
                try:
                    b.move(move[0],move[1])
                    b_turn = True
                    break
                except(ValueError):
                    print(b.calc_moves(b.get_piece(move[0])))
                    move = input("Enter Valid move (Start End)").split(" ")
                    
                except KeyError as err:
                    print("Invalid start space"+err)
                    move = input("Enter Valid move (Start End)").split(" ")

        print(b) 
    
    
 