import socket

def connect(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((hostname, port))
    sock.close()
    return result == 0

if __name__ == '__main__':
    for i in {1..254} ;do (ping 10.1.0.$i -c 1 -w 5  >/dev/null && echo "10.1.0.$i" &) ;done