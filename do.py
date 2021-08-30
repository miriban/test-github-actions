import socket

def connect(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((hostname, port))
    sock.close()
    return result == 0

for i in range(0,255):
    base_ip = '10.1.0.'
    res = connect(base_ip+str(i), 22)
    if res:
        print("Device found at: ",base_ip+str(i) + ":"+str(22))