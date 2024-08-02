import socket

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(("localhost", 9999))

# Receive a message from the server
message = client.recv(1024).decode()

# Send a response to the server
client.send(input(message).encode())

# Receive another message from the server
message = client.recv(1024).decode()

# Send another response to the server
client.send(input(message).encode())

# Print the final message from the server
print(client.recv(1024).decode())
