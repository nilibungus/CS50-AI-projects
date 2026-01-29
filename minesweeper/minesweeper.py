import itertools
import random

def subseting(set1, set2):

    for el in set1:
        set2.add(el)
    return set2

class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        known_mines1 = set()
        if len(self.cells) == self.count:

            subseting(self.cells, known_mines1)
            return known_mines1
        else:
            return known_mines1


    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        known_safes1 = set()
        if self.count == 0:
            subseting(self.cells, known_safes1)
            return known_safes1
        return known_safes1

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1




    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)




class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        self.moves_made.add(cell)
        self.mark_safe(cell)
        self.safes.add(cell)
        setcells = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if (i, j) == cell:
                    continue


                if 0 <= i < self.height and 0 <= j < self.width:
                    setcells.add((i, j))
        sentence = Sentence(setcells, count)
        self.knowledge.append(sentence)
        for cell in sentence.cells.copy():
            if cell in sentence.known_mines():
                self.mark_mine(cell)
                self.mines.add(cell)
            if cell in sentence.known_safes():
                self.mark_safe(cell)



        new_sentences = []
        changed = True
        while changed:
            changed = False

            for i in range(len(self.knowledge)):
                for j in range(len(self.knowledge)):
                    if i == j:
                        continue

                    if self.knowledge[i].cells.issubset(self.knowledge[j].cells):
                        cellsi_updated = set()
                        cellsj_updated = set()
                        count1 = 0

                        for cell in self.knowledge[j].cells - self.knowledge[i].cells:

                            if cell not in self.safes and cell not in self.mines:
                                cellsj_updated.add(cell)

                        for cell in self.knowledge[i].cells:
                            if cell not in self.safes and cell not in self.mines:
                                cellsi_updated.add(cell)

                        complement = cellsj_updated - cellsi_updated
                        count3 = self.knowledge[j].count - self.knowledge[i].count

                        sentence3 = Sentence(complement, count3)

                        for cell in sentence3.cells.copy():
                            if cell in sentence3.known_mines():
                                self.mark_mine(cell)
                                changed = True
                            if cell in sentence3.known_safes():
                                self.mark_safe(cell)
                                changed = True

                        if (sentence3 not in self.knowledge and sentence3 not in new_sentences):
                            new_sentences.append(sentence3)
                            changed = True

                    elif self.knowledge[j].cells.issubset(self.knowledge[i].cells):
                        cellsi_updated = set()
                        cellsj_updated = set()
                        count1 = 0

                        for cell in self.knowledge[i].cells - self.knowledge[j].cells:

                            if cell not in self.safes and cell not in self.mines:
                                cellsj_updated.add(cell)

                        for cell in self.knowledge[i].cells:
                            if cell not in self.safes and cell not in self.mines:
                                cellsi_updated.add(cell)

                        complement = cellsi_updated - cellsj_updated
                        count3 = self.knowledge[i].count - self.knowledge[j].count

                        sentence3 = Sentence(complement, count3)

                        for cell in sentence3.cells.copy():
                            if cell in sentence3.known_mines():
                                self.mark_mine(cell)
                                changed = True
                            if cell in sentence3.known_safes():
                                self.mark_safe(cell)
                                changed = True

                        if (sentence3 not in self.knowledge and sentence3 not in new_sentences):
                            new_sentences.append(sentence3)
                            changed = True

        self.knowledge.extend(new_sentences)












    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        self_mines_copy = self.mines.copy()
        self_safes_copy = self.safes.copy()
        self_movesmade_copy = self.moves_made.copy()
        for move in self_safes_copy:
            if move not in self_movesmade_copy:
                return move



    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        self_mines_copy = self.mines.copy()
        self_safes_copy = self.safes.copy()
        self_movesmade_copy = self.moves_made.copy()
        height = self.height
        width = self.width
        h = random.randint(0, height - 1)
        w = random.randint(0, width - 1)
        if (h, w) not in self_movesmade_copy:
            if (h, w) not in self_mines_copy:
                return (h, w)

