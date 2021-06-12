import socket
import threading
import pickle,struct
import cv2
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def receivemsg(s):
    data = b""
    payload_size = struct.calcsize("Q")
    while True:
        while len(data) < payload_size:
            packet = s.recv(4096) 
         
            if not packet: break
            data+=packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q",packed_msg_size)[0]
    
        while len(data) < msg_size:
            data += s.recv(4096)
            

        frame_data = data[:msg_size]
        data  = data[msg_size:]
        frame = pickle.loads(frame_data)
        cv2.imshow("Receiving Video",frame)
        key = cv2.waitKey(1) & 0xFF
        if key  == ord('q'):
            break
    s.close()

def sendmsg(s):
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        data=pickle.dumps(frame)
        message = struct.pack("Q",len(data))+data
        s.sendall(message)
        print("successfully sended")

if __name__=='__main__':
    s.connect(("127.0.0.1",9000))
    t1=threading.Thread(target=sendmsg, args=(s,))
    t1.start()
    t2=threading.Thread(target=receivemsg, args=(s,))
    t2.start()
        
    
