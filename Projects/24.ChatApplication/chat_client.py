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