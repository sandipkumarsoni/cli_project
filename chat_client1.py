import socket
import sys

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
host = socket.gethostname()

port = 8080

s.connect((host, port))
print("Conneted to the Server")

msg = s.recv(1024).decode()
print("Server MSG:", msg)

while 1:
	msg = s.recv(1024)
	msg = msg.decode()
	print("received from Server:", msg)
	new_msg = input(str(">>"))
	new_msg = new_msg.encode()
	s.send(new_msg)
	print("Message send to server...")

