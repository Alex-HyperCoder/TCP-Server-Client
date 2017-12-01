import os
import socket
import threading

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
Y = '\e[1;33m' # yellow

bind_ip = '127.0.0.1'
bind_port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

if os.name == 'posix':
    cmd = 'clear'
elif os.name == 'nt':
    cmd = 'cls'

os.system(cmd)

print 'Server Address: ' + C + str(bind_ip) + W
print 'Listening Port: ' + C + str(bind_port) + W
print '------------------------------------------'

def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    client_socket.send('ACK!')
    print 'Received {}'.format(request)
    client_socket.close()

while True:

    client_sock, address = server.accept()
    print 'Peer: ' + C + address[0] + W + ' Connecting Port[' + C + str(address[1]) + W + ']'

    #Save Connection to File
    conlog = open("connection_log.log", "a")
    conlog.write(address[0] + ":" + str(address[1]) + "\r\n")
    conlog.close()
    
    #Begin Thread
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)
    )
client_handler.start()
