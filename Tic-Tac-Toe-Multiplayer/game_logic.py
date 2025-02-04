class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'
        self.move_history = []

    def make_move(self, row, col):
        """Place a mark on the board if the cell is empty and within bounds."""
        if 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.move_history.append((row, col))
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        """Check if there's a winner or a tie."""
        # Check rows, columns, and diagonals
        for i in range(self.size):
            if all(self.board[i][j] == self.board[i][0] != ' ' for j in range(self.size)):
                return self.board[i][0]
            if all(self.board[j][i] == self.board[0][i] != ' ' for j in range(self.size)):
                return self.board[0][i]

        if all(self.board[i][i] == self.board[0][0] != ' ' for i in range(self.size)):
            return self.board[0][0]
        if all(self.board[i][self.size - 1 - i] == self.board[0][self.size - 1] != ' ' for i in range(self.size)):
            return self.board[0][self.size - 1]

        # Check for a tie
        if all(cell != ' ' for row in self.board for cell in row):
            return 'Tie'

        return None

    def reset_game(self):
        """Reset the game board and current player."""
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = 'X'
        self.move_history = []

    def display_board(self):
        """Display the current state of the board."""
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.size * 2 - 1))

    def undo_move(self):
        """Undo the last move."""
        if self.move_history:
            row, col = self.move_history.pop()
            self.board[row][col] = ' '
            self.current_player = 'O' if self.current_player == 'X' else 'X'