__author__ = 'Sameer'

import socket, sys, time

def main():
    servername = '127.0.0.1'
    serverport = 12000
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ("The client has trying to connect to server (%s)" % servername)
    while 1:
        clientSocket.sendto('handshake signal', (servername, serverport))
        time.sleep(2)
    pass



if __name__ == "__main__":
    main()
    pass