import time
import socket

UDP_IP ="192.168.1.151"    #SBC IP Address 
UDP_PORT= 5005		   #matching port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True: 
	#Receive Packet
	print('--------------------------')
	start = time.time()
	data, addr = sock.recvfrom(1024)  #Buffer size is 1024 bytes
	end = time.time()
	#separating the packet
	[Lwheel, Rwheel] = data.split('|')
	LW = int(Lwheel)
	RW = int(Rwheel)
	print'Left Wheel  :%i Left Wheel  x2:%i\n' %(LW,2*LW)
	print'Right Wheel :%i Right Wheel x2:%i\n' %(LW,2*LW)
	print "Recieved Packet:", data,  '\n'
	#computing bit rate and printing it
	duration = (end - start)
	rate = (len(pack)/(duration)*8)
	print 'Bit Rate (bps):%i' %(rate)
