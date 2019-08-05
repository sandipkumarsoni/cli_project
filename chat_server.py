import socket
import sys

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
host = socket.gethostname()

#print(host)
#sys.exit()


port = 8080
s.bind((host, port))
s.listen(1)
print("Waiting For 2 connection")

conn, add = s.accept()
print("First Client connected")
conn.send('Welcome Client, To server'.encode())


conn1, add1 = s.accept()
print("Second Client connected")
conn1.send('Welcome Client1 ,To server'.encode())



while 1:
	msg = input(str('>>'))
	msg = msg.encode()
	conn.send(msg)
	conn1.send(msg)
	print("Message Send...")
	recv_msg = conn.recv(1024)
	recv_msg = recv_msg.decode()
	print("Received from client :", recv_msg)
	conn1.send(recv_msg.encode())
	recv_msg1 = conn1.recv(1024)
	recv_msg1 = recv_msg1.decode()
	print("Received from client1 :", recv_msg1)
	conn.send(recv_msg1.encode())
