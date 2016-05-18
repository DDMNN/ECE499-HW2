import socket
import sys
import time
from PIL import Image

host="192.168.2.1"
port = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((host,port))

addr = (host,port)
buf=1024

while True:
	bytes = 0
	f = open("robot_receive.png","wb")
	startstamp = time.time()
	data,addr = sock.recvfrom(buf)
	while(data):
		f.write(data)
		sock.settimeout(20)
		endstamp = time.time()
		bytes += len(data)
		data,addr = sock.recvfrom(buf)
		if data == "end image":
			f.close()
			rate = (bytes/(endstamp - startstamp)*8)/1000
			print "freq (Hz) = 5   "   "|   bit rate (kbps) = ", int(rate)
			Image.open("robot_receive.png").show()
			time.sleep(20)
			break
