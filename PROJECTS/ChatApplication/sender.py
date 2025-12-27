
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="10.78.139.117"  #ip address of receiver
port=8888 #port of reciever
complete_address= (ip,port)
message=input("SEND YOUR MESSAGE : ")
encoded_message=message.encode('ascii')
s.sendto(encoded_message,complete_address)