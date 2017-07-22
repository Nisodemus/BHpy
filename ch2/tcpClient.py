#we are making some hardcore assumptions. Assuming it will always succeed
#and that the server is expecting the data, third that server will send back
#in timely fashion.... all for simplicity

import socket

target_host = "www.google.com"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET  param is applying standard IPv4/hostname and SOCK_STREAM indicates it will
#be a TCP client

# connect the client
client.connect((target_host,target_port))

#send some data - create the var and then use str.encode() due to it expecting
#bytes but data is a unicode string
data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(data.encode('utf-8'))

#recieve some data and print response
response = client.recv(4096).decode('utf-8')
print(response)
