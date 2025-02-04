import socket
import tkinter as tk

def send_move(row, col):
    move = f"{row},{col}"
    client_socket.send(move.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    if response in ['X', 'O', 'Tie']:
        result_label.config(text=f"Result: {response}")
    else:
        update_board(response)

def update_board(board_str):
    board = [row.split('|') for row in board_str.split('\n')]
    for i in range(3):
        for j in range(3):
            board_labels[i][j].config(text=board[i][j])

def main():
    global client_socket, board_labels, result_label

    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'  # Change to the server's IP address for LAN
    PORT = 5555         # Must match the server's port
    client_socket.connect((HOST, PORT))

    # Create the GUI
    root = tk.Tk()
    root.title("Tic-Tac-Toe Client")
    board_labels = [[None for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            label = tk.Label(root, text=' ', font=('Arial', 24), width=5, height=2, relief='solid')
            label.grid(row=i, column=j)
            label.bind('<Button-1>', lambda e, r=i, c=j: send_move(r, c))
            board_labels[i][j] = label

    result_label = tk.Label(root, text="Result: ", font=('Arial', 16))
    result_label.grid(row=3, column=0, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    main()