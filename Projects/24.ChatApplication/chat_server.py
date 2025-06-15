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