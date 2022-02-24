from socket import *
serverName = 'localhost'
serverPort = 8008
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    sentence = input('Input a sentence: ')
    print('From Client: ', sentence)
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
    if sentence =='BYE':
       break

   
