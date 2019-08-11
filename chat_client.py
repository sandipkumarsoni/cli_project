import socket
import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(levelname)s::%(message)s')

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
host = socket.gethostname()

port = 8080

logging.info('Sending Request to server')
s.connect((host, port))
logging.info('Connected to the server')

msg = s.recv(1024).decode()
print("Server response:", msg)

while 1:
	new_msg = input(str("Type your Text>>"))
	new_msg = new_msg.encode()
	logging.info('Sending text to server')
	s.send(new_msg)
	print("Message send to server...")
	msg = s.recv(1024)
	msg = msg.decode()
	print("Server Reply:", msg)
	
### HII CLIents tttttttttttttttttttttttttttttttttttttttttttttt	
	
	
