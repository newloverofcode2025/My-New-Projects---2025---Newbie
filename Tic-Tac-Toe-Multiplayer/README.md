# Multiplayer Tic-Tac-Toe Game

A Python-based multiplayer Tic-Tac-Toe game with a graphical user interface (GUI). Players can compete in real-time over a local network.

## Features
- Real-time multiplayer gameplay over a local network.
- Graphical user interface (GUI) for the game board.
- Detects wins, ties, and invalid moves.
- Simple and intuitive interface.
- Undo move functionality.
- Customizable board size.
- Score tracking for multiple games.

## How to Run
1. Clone this repository.
2. Navigate to the project folder.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

   Dependencies
Python 3.x
Tkinter (for GUI)
Socket (for network communication)
Usage
Start the server on one machine.
Start the client on another machine (or the same machine for testing).
Use the GUI to play the game. Click on the cells to make a move.
The game will display the result (win/tie) and allow you to undo moves.

Customization
You can change the board size by modifying the size parameter in the TicTacToe class in game_logic.py.
Customize player symbols and names by modifying the TicTacToe class initialization.
Enjoy playing Tic-Tac-Toe!