import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
#host must be server ip address

port =12345 
s.connect((host,port))

print(s.recv(1024))
s.send("Hello bro")
s.close()
