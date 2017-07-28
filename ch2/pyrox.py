import sys
import socket
import threading
import argparse

def reqhandler(buff):
    #do needed packet modification
    return buff

def reshandler(buff):
    #more modz
    return buff

def recFrom(connection):
    buff = "".encode()

    #setting timeout
    connection.settimeout(3)

    try:
        #keep reading into buffer untill no moar data
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buff += data
        except:
            pass
        return buff

def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, str) else 2

    for i in range(0, len(src), length):
        s = src[i:i+length]
        hexa = b' '.join(["%0*X".encode() % (digits, ord(x)) for x in s])
        text = b''.join([x.encode() if 0x20 <= ord(x) < 0x7F else b'.' for x in s'])
        result.append(b"%04x    %-*s    %s") % (i, length*(digits + 1), hexa, text)

    print(b'\n'.join(result))

    
