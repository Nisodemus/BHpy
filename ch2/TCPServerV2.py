import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

# Create an instance of a socket to act as server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Pass IP and Port for server to listen to
server.bind((bind_ip, bind_port))

# Set maximum connection backlog to 5
server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))


def handle_client(client_socket):
    while True:
        # Capture data recieved from client
        request = client_socket.recv(1024)

        print("[*] Received: %s" % request)

        try:
            # Send a packet back to client
            client_socket.send(b"Received")
        except:
            # Close connection if client couldn't receive
            client_socket.close()
            break



while True:

    client, addr = server.accept()
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    # Spin client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
