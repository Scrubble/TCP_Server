#!/bin/python3

import socket

TCP_IP = '192.168.0.213'
TCP_PORT = 50000
BUFFER_SIZE = 20
MESSAGE = "Hello, World!"
counter = 0

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
s.sendto(MESSAGE.encode(),(TCP_IP,TCP_PORT))
while counter < 20:
	data = s.recv(BUFFER_SIZE)
	print("Gesendete Daten: " , data.decode())
	counter = counter + 1

s.close()
