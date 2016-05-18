import socket
import sys
import Image
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host ="192.168.2.1"
port = 5005
buf =1024
addr = (host,port)

while True:
    startstamp = time.time()
    f=open ("robot_receive.jpg", "rb") 
    data = f.read(buf)
    while (data):
        if(sock.sendto(data,addr)):
            data = f.read(buf)
    f.close()
    sock.sendto("end image",addr)
    stopstamp = time.time()
    time.sleep(0.2)
