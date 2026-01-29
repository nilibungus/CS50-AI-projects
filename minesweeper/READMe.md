This project was completed as part of CS50 AI, Lecture 1. It consists of an implementation of Minesweeper, a classic logic puzzle game played on a rectangular grid. Some squares hide mines, while others are safe. The goal is to reveal all safe squares without clicking on any mines. When a safe square is clicked, a number appears showing how many mines are adjacent to that square, including diagonally. Players use these numbers to deduce which squares contain mines and which are safe. Squares suspected of hiding mines can be flagged to avoid accidentally clicking them. The game is won when all safe squares are revealed, and it is lost if a mine is clicked. Minesweeper challenges the player’s reasoning and deduction skills, turning careful observation into a fun and strategic puzzle.

The project consists of two main files:

runner.py: Provided by CS50 AI, this file contains all the code to run the graphical interface for the game.

minesweeper.py: Mostly implemented by me as required by the assignment. Key functions completed include known_mines (returns all cells known to be mines), known_safes (returns all cells known to be safe), mark_mine (updates sentences if a cell is known to be a mine), mark_safe (updates sentences if a cell is known to be safe), add_knowledge (updates self.mines, self.safes, self.moves_made, and self.knowledge based on new information from a safe cell), make_safe_move (returns a move that is known to be safe), and make_random_move (returns a random move).

  
