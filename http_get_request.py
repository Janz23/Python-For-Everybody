import socket

# Create a socket object
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the specified host and port
mysock.connect(('data.pr4e.org', 80))

# Send a GET request to retrieve the specified file
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# Receive and print the response from the server
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

# Close the socket connection
mysock.close()
