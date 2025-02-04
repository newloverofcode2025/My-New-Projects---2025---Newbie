import socket
import threading
from concurrent.futures import ThreadPoolExecutor

# Function to handle client communication
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\nClient: {message}")
            save_to_chat_history(f"Client: {message}")
        except ConnectionResetError:
            print("\nClient disconnected.")
            break
        except Exception as e:
            print(f"\nError: {e}")
            break
    client_socket.close()

# Function to save messages to chat history
def save_to_chat_history(message):
    with open("chat_history.txt", "a") as file:
        file.write(message + "\n")

def accept_connections(server, thread_pool):
    while True:
        client_socket, addr = server.accept()
        print(f"\nAccepted connection from {addr}")
        thread_pool.submit(handle_client, client_socket)

def main():
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to an IP address and port
        HOST = '127.0.0.1'  # Localhost (change to your machine's IP for LAN)
        PORT = 5555         # Port number
        server.bind((HOST, PORT))

        # Start listening for connections
        server.listen(5)
        print(f"Server listening on {HOST}:{PORT}")

        # Create a thread pool
        with ThreadPoolExecutor(max_workers=10) as thread_pool:
            accept_connections(server, thread_pool)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    main()