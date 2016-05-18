import socket

UDP_IP = "xxx.xxx.x.x"    #SBC IP address
UDP_PORT = 5005		  #matching port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

loop = True
while (loop):
	#User Inputs
	print('---------------------------------------------------------------\n')
	print('choice of Inputs: forward - right wheel position = left wheel position > 0 \nreverse - right wheel position = left wheel position < 0\nleft - right wheel position > left wheel position\nright - right wheel position < left wheel position')
	print('---------------------------------------------------------------\n')
	#Input Commands
	Rwheel = input('Enter Right Wheel Position(numeric value):')
	Lwheel = input('Enter Left Wheel Position (numeric value):')
	#Command Packet
	User_input = 'Left:'+str(Lwheel)+'|'+'Right:'+str(Rwheel)
	sock.sendto(User_input, (UDP_IP, UDP_PORT))
	print '\nLeft Wheel Input:%i \tRight Wheel Input:%i' %(Lwheel, Rwheel) 

sock.close()  

