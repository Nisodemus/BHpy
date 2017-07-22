import socket

bind_IP = '0.0.0.0'
bind_Port = 9000

def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((bind_IP, bind_Port))
    print("waiting on port: " + str(bind_Port))

    while 1:
        data, addr = server. recvfrom(1024)
        print(data)

if __name__ == '__main__':
    udp_server()
     
