import socket
import os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8000))
sock.listen(1)
print('Waiting for connecting...')
conn,addr = sock.accept()
while True:
	filename = 'C:/Users/hp/Desktop/2020144135.txt'
	print('I want to get the file %s!' % filename)
	conn.send(filename.encode('utf-8'))
	str1 = conn.recv(1024)
	str2 = str1.decode('utf-8')
	if str2 == 'no':
		print('To get the file %s is failed!' % filename)
	else:
		conn.send(b'I am ready!')
		temp = filename.split('/')
		myname = 'my_' + temp[len(temp)-1]
		size = 1024
		with open(myname,'wb') as f:
			while True:
				data = conn.recv(size)
				f.write(data)
				if len(data) < size:
					break
	conn.close()
	print('The download file is %s !' % myname)
sock.close()
