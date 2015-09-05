#!/usr/bin/python
import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
def get_ip():
    return "127.0.0.1"
def get_port():
    return PORT
api={"getip":get_ip,"getport":get_port}
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Socket bind complete'
s.listen(10)
print 'Socket now listening'
while True:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    #now keep talking with the client
    receive_data=''
    while True:
        data=conn.recv(10)
        receive_data=receive_data+data
        if not data:
            break
        elif receive_data[-2:]=='\r\n':
            break
        else:
            continue 
    print "we hava received data: " + receive_data
    mth=receive_data.strip()
    if api.has_key(mth):
        print "ye"
        reply=api[mth]()
        conn.sendall(str(reply))
    conn.close()
s.close()
