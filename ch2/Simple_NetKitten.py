import socket

port = 9999
hostname = "0.0.0.0"
text_to_send = "AAABBBCC TEST101"

def netkitten(text_to_send):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(( hostname, port ))
    s.sendall(text_to_send.encode('utf-8'))
    s.shutdown(socket.SHUT_WR)

    rec_data = []

    while 1:

        data = s.recv(1024)
        if not data:
            break
        rec_data.append(data)

    s.close()
    return rec_data

if __name__ == "__main__":

    text_to_send = "boo hoo"
    text_recved = netkitten(text_to_send)
    print(text_recved[1])
