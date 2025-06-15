
# This project is of intermediate difficulty because it introduces:

  * **Socket Programming:** Handling network connections.
  * **Multi-threading:** Allowing the server to handle multiple clients concurrently and clients to send/receive messages simultaneously.
  * **Basic Protocol Design:** Defining how messages are sent and received.

-----

## 💬 Python Chat Application

This project consists of two main parts: a **Chat Server** that manages connections and message relaying, and a **Chat Client** that connects to the server to send and receive messages.

### 📁 Project Structure

```
chat-application/
├── chat_server.py
└── chat_client.py
```

### 📋 Prerequisites

  * Python 3.6+ installed

### 🚀 Step-by-Step Implementation

#### 1\. Create `chat_server.py`

This script will act as the central hub. It listens for incoming client connections, accepts them, and then uses threads to handle each client. Messages received from one client are broadcast to all other connected clients.

```python
# chat_server.py
import socket
import threading
import datetime

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []  # List to store connected client sockets and their addresses
        self.usernames = {} # Dictionary to store socket -> username mapping
        self.lock = threading.Lock() # Lock to protect shared resources (clients, usernames)

    def start(self):
        # Create a TCP/IP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allow reuse of address
        
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen()
            print(f"[*] Listening on {self.host}:{self.port}")
        except socket.error as e:
            print(f"[!] Could not bind to port {self.port}: {e}")
            self.server_socket.close()
            return

        # Start accepting client connections in a loop
        while True:
            try:
                client_socket, client_address = self.server_socket.accept()
                print(f"[*] Accepted connection from {client_address}")
                # Start a new thread to handle this client
                client_handler = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_handler.daemon = True # Allow main program to exit even if threads are running
                client_handler.start()
            except KeyboardInterrupt:
                print("\n[!] Server shutting down...")
                self.shutdown()
                break
            except Exception as e:
                print(f"[!] Error accepting connection: {e}")
                
    def handle_client(self, client_socket, client_address):
        # First, get the username from the client
        try:
            username_bytes = client_socket.recv(1024)
            username = username_bytes.decode('utf-8').strip()
            if not username:
                username = f"Guest-{client_address[1]}" # Fallback for empty username
            
            with self.lock:
                self.clients.append(client_socket)
                self.usernames[client_socket] = username
                print(f"[*] {username} ({client_address}) has joined the chat.")
            
            # Announce new user to everyone
            self.broadcast(f"📢 {username} has joined the chat.")

        except Exception as e:
            print(f"[!] Error receiving username from {client_address}: {e}")
            client_socket.close()
            return

        # Now, handle messages from this client
        while True:
            try:
                message = client_socket.recv(4096).decode('utf-8')
                if not message: # Client disconnected
                    break
                
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                formatted_message = f"[{timestamp}] {self.usernames[client_socket]}: {message}"
                print(f"Received from {self.usernames[client_socket]} ({client_address}): {message.strip()}")
                self.broadcast(formatted_message, sender_socket=client_socket)
            except ConnectionResetError: # Client forcefully disconnected
                print(f"[*] {self.usernames.get(client_socket, 'Unknown')} ({client_address}) disconnected forcefully.")
                break
            except socket.error as e: # Other socket errors
                print(f"[!] Socket error with {self.usernames.get(client_socket, 'Unknown')} ({client_address}): {e}")
                break
            except Exception as e:
                print(f"[!] Error handling client {self.usernames.get(client_socket, 'Unknown')} ({client_address}): {e}")
                break

        # Client disconnected or error occurred, clean up
        self.remove_client(client_socket)
        
    def broadcast(self, message, sender_socket=None):
        with self.lock:
            for client_socket in self.clients:
                if client_socket != sender_socket: # Don't send back to the sender
                    try:
                        client_socket.sendall(message.encode('utf-8'))
                    except Exception as e:
                        print(f"[!] Error broadcasting to a client: {e}")
                        # Optionally, remove client if send fails consistently
                        # self.remove_client(client_socket) # This would require careful handling with current iteration
    
    def remove_client(self, client_socket):
        with self.lock:
            if client_socket in self.clients:
                self.clients.remove(client_socket)
                username = self.usernames.pop(client_socket, "Unknown User")
                client_socket.close()
                print(f"[*] {username} has left the chat.")
                self.broadcast(f"💔 {username} has left the chat.")

    def shutdown(self):
        print("[*] Shutting down server...")
        with self.lock:
            for client_socket in self.clients:
                try:
                    client_socket.sendall("Server is shutting down. Goodbye!".encode('utf-8'))
                    client_socket.close()
                except Exception as e:
                    print(f"Error closing client socket during shutdown: {e}")
            self.clients.clear()
            self.usernames.clear()
        self.server_socket.close()
        print("[*] Server shut down successfully.")

if __name__ == '__main__':
    server = ChatServer(HOST, PORT)
    server.start()

```

#### 2\. Create `chat_client.py`

This script will connect to the server, send its username, and then continuously read user input to send to the server, while simultaneously listening for messages from the server.

```python
# chat_client.py
import socket
import threading
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = None

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"[*] Connected to server at {self.host}:{self.port}")
        except socket.error as e:
            print(f"[!] Could not connect to server: {e}")
            sys.exit(1)

    def send_username(self):
        while True:
            username = input("Enter your username: ").strip()
            if username:
                self.username = username
                self.client_socket.sendall(username.encode('utf-8'))
                break
            else:
                print("Username cannot be empty. Please try again.")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(4096).decode('utf-8')
                if not message: # Server disconnected
                    print("\n[!] Server disconnected.")
                    break
                print(f"\r{message}\n{self.username}> ", end="") # Print message and re-prompt user input
            except ConnectionResetError: # Server forcefully disconnected
                print("\n[!] Server forcefully disconnected.")
                break
            except socket.error as e:
                print(f"\n[!] Socket error receiving message: {e}")
                break
            except Exception as e:
                print(f"\n[!] Error receiving message: {e}")
                break
        self.client_socket.close()
        sys.exit(0) # Exit the client gracefully

    def send_messages(self):
        while True:
            try:
                user_input = input(f"{self.username}> ")
                if user_input.lower() == 'exit':
                    break
                self.client_socket.sendall(user_input.encode('utf-8'))
            except ConnectionResetError:
                print("[!] Connection lost to server.")
                break
            except socket.error as e:
                print(f"[!] Socket error sending message: {e}")
                break
            except Exception as e:
                print(f"[!] Error sending message: {e}")
                break
        self.client_socket.close()
        sys.exit(0) # Exit the client gracefully

    def start(self):
        self.connect()
        self.send_username()

        # Start a thread for receiving messages
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True # Allow main program to exit even if threads are running
        receive_thread.start()

        # Main thread handles sending messages
        self.send_messages()

if __name__ == '__main__':
    client = ChatClient(HOST, PORT)
    client.start()

```

### 📝 Code Explanation

#### `chat_server.py`

  * **`ChatServer` Class:** Encapsulates the server's logic.
      * `__init__`: Initializes host, port, a list to keep track of connected `client_sockets`, a dictionary `usernames` to map sockets to usernames, and a `threading.Lock()` to ensure thread-safe access to shared resources (`clients`, `usernames`).
      * **`start()`:**
          * Creates a `socket.socket` for TCP communication (`socket.AF_INET` for IPv4, `socket.SOCK_STREAM` for TCP).
          * `setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`: Allows the socket to be immediately reused after closing, preventing "Address already in use" errors during quick restarts.
          * `bind()`: Associates the socket with a specific network interface and port.
          * `listen()`: Puts the server socket into listening mode, waiting for incoming connections.
          * `accept()`: Blocks until a client connects. When a client connects, it returns a new `client_socket` (for communication with that client) and `client_address`.
          * **`threading.Thread`:** For each new client, a new thread is created to run `handle_client`. This is crucial for the server to handle multiple clients concurrently. `daemon = True` means these threads will automatically exit when the main program exits.
      * **`handle_client(client_socket, client_address)`:**
          * **Username Handshake:** The server expects the first message from the client to be its username. This simple "protocol" ensures the server knows who each client is.
          * Adds the client's socket and username to `self.clients` and `self.usernames` respectively, protected by the `self.lock`.
          * Enters a loop to continuously `recv()` (receive) messages from this specific client.
          * If `recv()` returns an empty byte string (`if not message:`), it indicates the client has gracefully disconnected.
          * **`ConnectionResetError`**: Catches this specific error which occurs when a client forcefully closes the connection.
          * Prints the received message on the server console.
          * Calls `broadcast()` to send the message to all other clients.
          * If a client disconnects or an error occurs, it breaks the loop and calls `remove_client()`.
      * **`broadcast(message, sender_socket=None)`:**
          * Iterates through all connected clients in `self.clients`.
          * Sends the `message` to each client, *except* for the `sender_socket` (to avoid sending a message back to the person who just sent it).
          * Uses `sendall()` to ensure all data is sent.
          * Protected by `self.lock` to prevent issues if `self.clients` is modified while iterating.
      * **`remove_client(client_socket)`:**
          * Removes the disconnected client's socket from `self.clients` and `self.usernames`.
          * Closes the client's socket.
          * Broadcasts a "user left" message to other clients.
      * **`shutdown()`:** Handles graceful server shutdown, notifying clients and closing all sockets.

#### `chat_client.py`

  * **`ChatClient` Class:** Encapsulates the client's logic.
      * `__init__`: Initializes host, port, and creates a `socket.socket`.
      * **`connect()`:** Attempts to `connect()` to the server's host and port.
      * **`send_username()`:** Prompts the user for a username and sends it to the server immediately after connecting.
      * **`receive_messages()`:**
          * Runs in a separate thread.
          * Continuously `recv()` messages from the server.
          * If a message is received, it prints it to the console.
          * `\r` and `end=""` are used in `print()` to ensure that the user's input prompt (` username>  `) is re-displayed correctly after a new message arrives, without interfering with their typing.
          * Handles `ConnectionResetError` if the server disconnects.
          * Exits the client gracefully (`sys.exit(0)`) if the server disconnects.
      * **`send_messages()`:**
          * Runs in the main thread.
          * Continuously takes `input()` from the user.
          * If the user types `exit` (case-insensitive), the client closes.
          * `sendall()` sends the user's input to the server.
          * Handles `ConnectionResetError` if the server disconnects.
      * **`start()`:**
          * Calls `connect()` and `send_username()`.
          * Starts the `receive_messages` function in a new daemon thread.
          * The main thread then runs `send_messages`, allowing the client to send and receive concurrently.

### ▶️ How to Run

1.  **Save the files:** Save the above code as `chat_server.py` and `chat_client.py` in the same directory.

2.  **Open Terminal 1 (for the Server):**

    ```bash
    python chat_server.py
    ```

    You should see: `[*] Listening on 127.0.0.1:65432`

3.  **Open Terminal 2 (for Client 1):**

    ```bash
    python chat_client.py
    ```

    It will prompt: ` Enter your username:  `
    Type a username (e.g., `Alice`) and press Enter.
    You should see: `[*] Connected to server at 127.0.0.1:65432` and then ` Alice>  `

4.  **Open Terminal 3 (for Client 2):**

    ```bash
    python chat_client.py
    ```

    Enter another username (e.g., `Bob`) and press Enter.

5.  **Start Chatting\!**

      * In Alice's terminal, type `Hello Bob!` and press Enter.
      * In Bob's terminal, you should see `[HH:MM:SS] Alice: Hello Bob!`
      * In Bob's terminal, type `Hi Alice!` and press Enter.
      * In Alice's terminal, you should see `[HH:MM:SS] Bob: Hi Alice!`

### 💡 How to Test Disconnections

  * **Client Graceful Exit:** Type `exit` in any client terminal. You'll see "Server disconnected" on the client, and the server will show "[\*] \<Username\> has left the chat."
  * **Forceful Client Disconnect:** Close a client terminal window directly (e.g., click the 'X'). The server will eventually detect a `ConnectionResetError` and report "disconnected forcefully."
  * **Server Shutdown:** Press `Ctrl+C` in the server's terminal. All connected clients will see "[\!] Server disconnected."

### ⚠️ Important Considerations & Future Improvements (Intermediate/Advanced)

  * **Error Handling:** While basic error handling is present, a more robust application would handle network errors more gracefully (e.g., reconnect attempts).
  * **Message Protocol:** The current protocol is very simple (just sending raw strings). For more complex features, you'd use a structured protocol (e.g., sending JSON objects) to include message type, sender ID, timestamps, etc.
  * **Authentication & Authorization:** Currently, anyone can join. You'd need a system for user registration, login, and potentially access control.
  * **Private Messaging:** Extend the protocol to allow clients to send messages only to specific users.
  * **Room/Channel System:** Create different chat rooms for users to join.
  * **GUI:** Build a graphical user interface using libraries like Tkinter, PyQt, or Kivy for a better user experience.
  * **File Transfer:** Allow users to send files to each other.
  * **Database Integration:** Store chat history, user profiles, etc., in a database.
  * **Scalability:** For many users, a single-threaded server (even with client threads) might not scale well. Consider asynchronous I/O (`asyncio`) or frameworks designed for high concurrency.
  * **Network Byte Order:** For cross-platform compatibility, especially when dealing with data length, it's good practice to use `struct` module for packing/unpacking data into network byte order.
  * **Keepalives:** Implement a heartbeat mechanism to detect dead clients/servers faster than relying on OS-level `ConnectionResetError`.

This project provides a strong foundation for understanding client-server communication and multi-threading in Python\!