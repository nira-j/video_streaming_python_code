import socket
import threading
import cv2,pickle,struct,time

# server ip
ip= "127.0.0.1" 

# port  
port=9000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# binding
server.bind((ip,port))

server.listen()

#receive
def receive():
    client,address=server.accept()
    while True:
        message = client.recv(4096)
        print("successfully recived")
        client.sendall(message)
    
if __name__=='__main__':
    print("server is running")
    receive()
