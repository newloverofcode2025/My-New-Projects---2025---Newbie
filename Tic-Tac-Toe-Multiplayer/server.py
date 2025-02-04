import socket
import threading
from game_logic import TicTacToe

def handle_client(client_socket):
    game = TicTacToe()
    while True:
        try:
            # Receive the move from the client
            move = client_socket.recv(1024).decode('utf-8')
            if not move:
                break
            row, col = map(int, move.split(','))

            # Make the move
            if game.make_move(row, col):
                # Check for a winner or tie
                result = game.check_winner()
                if result:
                    client_socket.send(result.encode('utf-8'))
                    break

                # Send the updated board to the client
                board_str = '\n'.join(['|'.join(row) for row in game.board])
                client_socket.send(board_str.encode('utf-8'))
            else:
                client_socket.send("Invalid move".encode('utf-8'))

        except ConnectionResetError:
            print("Client disconnected.")
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'  # Localhost (change to your machine's IP for LAN)
    PORT = 5555         # Port number
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Server started on {HOST}:{PORT}. Waiting for a client to connect...")

    client_socket, client_address = server.accept()
    print(f"Client connected from {client_address}")
    threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    main()