import socket

target_host = "0.0.0.0"
target_port = 9000

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
data = "AAAAaBBBBBCCCC"
client.sendto(data.encode('utf-8'), (target_host,target_port))
#recieve some data
data, addr = client.recvfrom(4096)

print(data)
