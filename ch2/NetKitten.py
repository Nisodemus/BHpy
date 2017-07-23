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
        print("Read buffer from stdin")
        buff = sys.stdin.read()
        #note - this will blockup so CTRL-D is not sending to stdin
        print("Sending [{0} to client".format(buff))
        #send data off
        client_sender(buff)

    #Let's listen and upload, execute and drop shells back (depending on options)
    if listen:
        server_loop()

        
