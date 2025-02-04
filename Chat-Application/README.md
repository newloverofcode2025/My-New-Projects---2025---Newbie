# Simple Chat Application

A Python-based chat application that allows multiple users to communicate in real-time over a local network. The system saves chat history to a text file.

## Features
- Real-time messaging between a server and multiple clients.
- Chat history saved to `chat_history.txt`.
- Simple text-based interface for sending and receiving messages.
- Uses a thread pool for efficient handling of multiple clients.

## How to Run
1. Clone this repository.
2. Navigate to the project folder.
3. Run the server:
   ```bash
   python server.py

   Requirements
Python 3.x
Notes
Ensure that the server and client are running on the same network.
Update the HOST and PORT variables in both server.py and client.py if needed.

