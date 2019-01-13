import socket
host = "" 
#host must be server ip address
port = 12345 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port)) 
s.listen(2)
conn, addr = s.accept()
print(addr, "You are now Connected")
conn.send("Thank you for connecting")
conn.close()
