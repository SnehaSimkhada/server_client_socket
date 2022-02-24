from socket import *
from turtle import fd
serverPort = 8008
serverName = ('localhost')
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(1)
print('The server ' + serverName + ' is ready to receive')
connectionSocket, addr = serverSocket.accept()

while True:
	
	sentence = connectionSocket.recv(1024).decode()
	print('Got From Client: ', sentence)
	first_chars = sentence[0:4]
	remaining = sentence[5:len(sentence)]
	if  first_chars == 'HELO':
		reply = "Hello " + remaining + ", pleased to meet you."
		connectionSocket.send(reply.encode('utf-8'))
	
	elif sentence == 'REQTIME':	
		from datetime import datetime
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		connectionSocket.send(current_time.encode('utf-8'))

	elif sentence == 'REQDATE':	
		from datetime import datetime
		shortDate = datetime.today().strftime('%Y-%m-%d')
		connectionSocket.send(shortDate.encode('utf-8'))

	elif first_chars == 'ECHO':	
		connectionSocket.send(remaining.encode('utf-8'))

	elif sentence == 'REQIP':
		import socket
		hostname = socket.gethostname()    
		IPAddr = socket.gethostbyname(hostname) 		
		connectionSocket.send(IPAddr.encode('utf-8'))
	
	elif sentence == 'BYE':	
		connectionSocket.send("See yah Later".encode('utf-8'))
		connectionSocket.close()
		
	else:
		print('No Such Command')
		connectionSocket.close()

		
		
		
