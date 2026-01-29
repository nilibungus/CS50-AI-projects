"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

played_turns = []
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_X = 0
    number_of_O = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                number_of_X +=1
            elif board[i][j] == O:
                number_of_O += 1
            else:
                pass
    if number_of_X == number_of_O:
        return X
    else:
        return O





def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    if terminal(board):
        return None
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    actions.add((i, j))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if not isinstance(action, tuple) or len(action) != 2 or action[0] not in range(3) or action[1] not in range(3):
        raise ValueError
    elif board[action[0]][action[1]] != EMPTY:
        raise ValueError("cell not available")
    else:
        x = action[0]
        y = action[1]
        new_board = copy.deepcopy(board)
        new_board[x][y] = player(board)
        return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board) == 1:
        return X
    elif utility(board) == -1:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.

    """
    if utility(board) == 1 or utility(board) == -1:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False

        return True


diagonal1 = [(0, 0), (1, 1), (2, 2)]
diagonal2 = [(0, 2), (1, 1), (2, 0)]
vertical1 = [(0, 0), (1, 0), (2, 0)]
vertical2 = [(0, 1), (1, 1), (2, 1)]
vertical3 = [(0, 2), (1, 2), (2, 2)]
def utility(board):
    for i in range(3):
        if board[i] == [X, X, X]:
            return 1
        if board[i] == [O, O, O]:
            return -1
        else:
            pass



    for i in range(3):
        countX = 0
        countO = 0


        for j in range(3):
            if board[j][i] == X:
                countX += 1
            if board[j][i] == O:
                countO += 1
        if countX == 3:
            return 1
        if countO ==3:
            return -1
        else:
            pass


    countX = 0
    countO = 0

    for cell in diagonal1:
        if board[cell[0]][cell[1]] == X:
                countX += 1
        if board[cell[0]][cell[1]] == O:
                countO += 1

    if countX == 3:
        return 1
    if countO == 3:
        return -1
    else:
        pass

    countX = 0
    countO = 0
    for cell in diagonal2:
        if board[cell[0]][cell[1]] == X:
            countX += 1
        if board[cell[0]][cell[1]] == O:
            countO += 1

    if countX == 3:
        return 1
    if countO == 3:
        return -1
    else:
        pass

    return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """


    gametree = game_tree(board)

    if not terminal(board):
        minimax_algorithm(gametree)
    else:
        return None


    points_of_children = []
    board_node = None

    for node in gametree:
       if node.state == board:
            board_node = node
            break     # << important: stop searching once found

    if board_node is None:
        print(order_game_tree(gametree)[-1].state)
        print(f"{board} is not in the game tree")
    else:
        for child in board_node.children:
            if hasattr(child, "points"):
                points_of_children.append(child.points)
            else:
                raise ValueError(f"{child.state} has no points!")
        max_children_points = max(points_of_children)
        min_children_points = min(points_of_children)
        bestmoves = []
        if player(board) == X:
            for child in board_node.children:
                if child.points == max_children_points:
                    bestmoves.append(child.action)
            return bestmoves[0]
        if player(board) == O:
            for child in board_node.children:
                if child.points == min_children_points:
                    bestmoves.append(child.action)
            return bestmoves[0]








class Node():
    def __init__(self, state, parent, action, children, number, level):
        self.state = state
        self.parent = parent
        self.action = action
        self.children = children
        self.number = number
        self.level = level

def add_attribute(obj, name, value):
    setattr(obj, name, value)


def game_tree(board):
    gametree = []
    root = Node(state=copy.deepcopy(board), parent=None, action=None, children=[], number=0, level=8)
    gametree.append(root)

    allnodes = [root]

    while allnodes:
        node = allnodes.pop(0)   # BFS; pop() would be DFS
        if not terminal(node.state):
            for action in actions(node.state):
                # Make a fresh copy of node.state so result() can't clobber others.
                parent_state_copy = copy.deepcopy(node.state)

                # Option A: if your result() returns a fresh state (non-mutating),
                # you can do: child_state = result(node.state, action)
                # Option B (defensive): call result on a copy so any in-place edits
                # won't affect node.state or other nodes:
                child_state = result(parent_state_copy, action)

                new_child = Node(
                    state=child_state,
                    parent=node,
                    action=action,
                    children=[],
                    number=node.number + 1,
                    level=node.level - 1
                )

                node.children.append(new_child)
                gametree.append(new_child)
                allnodes.append(new_child)

    return gametree










def order_game_tree(gametree):
    return sorted(gametree, key=lambda n: n.level)





def minimax_algorithm(gametree):
    newgametree = order_game_tree(gametree)
    for node in newgametree:
        if terminal(node.state):
            add_attribute(node, "points", utility(node.state))
        else:
            children_points = []
            for child in node.children:
                children_points.append(child.points)
            maximum = max(children_points)
            minimum = min(children_points)
            if node.number % 2 == 0:
                add_attribute(node, "points", maximum)
            else:
                add_attribute(node, "points", minimum)






















