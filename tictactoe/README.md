This project was completed as part of CS50’s Introduction to Artificial Intelligence with Python. It consists of an implementation of Tic-Tac-Toe with an AI that plays optimally using the Minimax algorithm. The game is played on a standard 3×3 board, where two players alternate placing Xs and Os. The goal is to get three in a row horizontally, vertically, or diagonally.

The program allows a human player to compete against the AI. It includes functions to determine the current player, available moves, resulting board states, game termination, winners, and utility values for terminal states. The Minimax algorithm evaluates all possible future board states to choose the optimal move, ensuring that the AI never loses if played correctly. Optional alpha-beta pruning can be implemented to improve efficiency.

Key functions implemented include:

player(board) – Returns whose turn it is (X or O) on the current board.

actions(board) – Returns all possible legal moves.

result(board, action) – Returns the board state that results from a move.

winner(board) – Determines the winner if there is one.

terminal(board) – Checks if the game has ended.

utility(board) – Returns the utility of a terminal board: 1 for X win, -1 for O win, 0 for tie.

minimax(board) – Returns the optimal move for the current player using Minimax.

This project demonstrates proficiency in Python programming, game theory, and AI algorithms, while providing a hands-on example of decision-making in strategic games.
