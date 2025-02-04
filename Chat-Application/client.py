import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\nServer: {message}")
        except ConnectionResetError:
            print("\nServer disconnected.")
            break
        except Exception as e:
            print(f"\nError: {e}")
            break
    client_socket.close()

def main():
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        HOST = '127.0.0.1'  # Change to the server's IP address for LAN
        PORT = 5555         # Must match the server's port
        client.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        # Start a thread to receive messages
        threading.Thread(target=receive_messages, args=(client,)).start()

        # Send messages to the server
        while True:
            message = input("You: ")
            if message.lower() == 'exit':
                break
            client.send(message.encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()