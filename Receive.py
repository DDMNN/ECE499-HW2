import socket

UDP_IP = "192.168.1.81"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,#Internet,
		     socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024)
	print"Received Message", data