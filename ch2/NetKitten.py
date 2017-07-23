import sys
import socket
import getopt
import threading
import subprocess
import argparse

#globals - used for various options
target = None
port = None
uploadDestination = None
execute = None
upload = None
command = False
listen = False

def main ():

    global target
    global port
    global uploadDestination
    global execute
    global upload
    global command
    global listen

    #build argument parsing and descriptions of various actions
    parser = argparse.ArgumentParser(description="Baby netcat clone built in py3")
    parser.add_argument("port", type=int, help="The target port")
    parser.add_argument("-t", "--target_host", type.str, help="The target host", default="0.0.0.0")
    parser.add_argument("-l", "--listen", help="listen on [host]:[port] for connections", action="store_true", default=False)
    parser.add_argument("-e", "--execute", help="--execute=file_to_run fire the given file when receiving a connection")
    parser.add_argument("-c", "--command", help="Spawn a command shell", action="store_true", default=False)
    parser.add_argument("-u", "--upload", help="--upload=destination when upload file and write to [destination] when connection recieved")

    #parse arguments
    target = args.target_host
    port = args.port
    uploadDestination = args.upload
    execute = args.execute
    command = args.command
    listen = args.listen

    #Decide if we are listening or just sending data from stdin
    if not listen and target is not None and port > 0:
        print("Kitten: Read buffer from stdin")
        buff = sys.stdin.read()
        #note - this will blockup so CTRL-D is not sending to stdin
        print("Sending [{0} to client".format(buff))
        #send data off
        client_sender(buff)

    #Let's listen and upload, execute and drop shells back (depending on options)
    if listen:
        server_loop()

def client_sender(buff):

    print("Kitten: Sending data to client on port " + str(port))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # connection to target
        client.connect((target, port))

        if len(buff):
            client.send(buff.encode())
        while True:
            #Wait for a data response
            recv_len = 1
            response = ""

            while recv_len:
                print("Kitten: waiting for response form client")
                data = client.recv(4096)
                recv_len = len(data)
                response += data.decode(errors="ignore")

                if recv_len < 4096:
                    break

            print(response, end="")

            #wait for more inputs
            buff = input("")
            buff += "\n"

            #ship it away
            client.send(buff.encode())

        except:
            print("[] Exception n shit. Run Away!")
        finally:
            client.close()

def server_loop():

    global target
    print("kitten: Entering server loopage")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    #set max listen to 5
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        #spin up thread to handle new client
        client_thread = threading_Thread(target=client_handler, args=(client_socket,))

def run_command(command):
    #newline prunning
    command = command.rstrip()
    print("Kitten: Firing command: " + command)

    try:
        #launch new process
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to fire command. \r\n"

    #shoot data back to client
    return output

#client handler + shell loop + shit tons of fixs needed. 
