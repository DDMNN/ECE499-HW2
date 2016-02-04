import socket

UDP_IP = "192.168.1.82"
UDP_PORT = 5006
MESSAGE = "Hello World!"

print "UDP Target IP", UDP_IP
print "UDP Target Port", UDP_PORT
print "Message:", MESSAGE

sock = socket.socket(socket.AF_INET,#Internet,
		     socket.SOCK_DGRAM)
sock.sendto(MESSAGE,(UDP_IP,UDP_PORT))
