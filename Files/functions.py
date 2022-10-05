coordinate_key = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
index_key = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}


def to_coordinate(space):
    """
    Returns the algebraic notation of a space on the board (e.g. a8)

    :param space: Index coordinate of space on board (e.g. 00 for a8)
    :return: String of space coordinate in algebraic notation
    """
    space = str(space)
    if not space.isnumeric():
        raise IndexError('Coordinate not on board')
    row = str(8 - int(space[0]))
    col = index_key.get((int(space[1])))
    if col is None or int(row) > 8 or int(row) <= 0:
        raise IndexError('Coordinate not on board')
    return col + row


def to_index(space):
    """
    Returns the index of space in 2D array as a string

    :param space: String of space coordinate on chess board in algebraic notation(e.g. a1)
    :return: String of row column indices in virtual board representation (e.g. a8 = 00)
    """
    col = coordinate_key.get(space[0].lower())
    row = str(8 - int(space[1]))
    if col is None or int(row) > 8:
        raise IndexError('Coordinate not on board')

    return row + str(col)
