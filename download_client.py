import socket
import os
def sendfile(sock):
	str1 = sock.recv(1024)
	filename = str1.decode('utf-8')
	print('The server requests my file:' , filename)
	if os.path.exists(filename):
		print('I have %s ,begin to download!' % filename)
		sock.send(b'yes')
		sock.recv(1024)
		size = 1024
		with open(filename, 'rb') as f:
			while True:
				data = f.read(size)
				sock.send(data)
				if len(data) < size:
					break
		print('%s is downloaded successfully!' % filename)
	else:
		print('Sorry, I have no %s' % filename)
		sock.send(b'no')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8000))
while True:
	sendfile(sock)
sock.close()