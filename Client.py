import socket

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect(('127.0.0.1', 5000))

client.send('TCP SEND')
# receive the response data (4096 is recommended buffer size)
response = client.recv(4096)

client.close()
