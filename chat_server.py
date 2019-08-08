import socket
import sys
import subprocess
import multiprocessing
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(levelname)s::%(message)s')

#LOG_FILENAME = '/home/sandip/cli_project/socket.log'

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s = socket.socket()
host = socket.gethostname()
logging.info('Socket Created')

#print(host)
#sys.exit()


port = 8080
s.bind((host, port))
s.listen(20)
print("Waiting For connection")

list_of_clients = []

def client_process(conn):
	conn.send("Welcome for chat".encode())
	while True:
		try:
			msg = conn.recv(1024)
			msg = msg.decode()
			if msg:
				print('>>>', msg)
				broadcast(msg, conn)
			else:
				remove(conn)
		except Exception as err:
			continue


def broadcast(msg_1, conn_1):
	cmd = ['/bin/sh', '-c', msg_1]
	msg_11 = msg_1.split()
	try:
		logging.info('Checking for Linux command')
		subprocess.call(msg_11)
		#p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		#stdout,stderr = p1.communicate()
		opt = 'ACK'
	except Exception as err:
		opt = 'NOCK'	
	opt = opt.encode()
	conn_1.send(opt)


def remove(connection): 
	if connection in list_of_clients:
		logging.info('DisconNNECTING One connection')
		list_of_clients.remove(connection) 			



while True:
	logging.info('Accepting request from server')
	conn, add = s.accept()
	list_of_clients.append(conn)
	p1 = multiprocessing.Process(target = client_process, args=(conn,))
	p1.start()
	#p1.join()
	#start_new_thread(client_thread, (conn,))
