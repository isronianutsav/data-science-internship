
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="10.78.139.137"  #ip address of sender(my , if i am sending)
port=5555

complete_address= (ip,port)
s.bind(complete_address)
while True:
    msg=s.recvfrom(1024) #1024 is character limit
    msg[0].decode('ascii')
    print(msg)