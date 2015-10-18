__author__ = 'Sameer'

import socket, sys

def main():
    servername = '127.0.0.1'
    serverport = 12000
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ("The client has trying to connect to server (%s)" % servername)
    clientSocket.sendto('handshake signal', (servername, serverport))
    text_input = raw_input("Want to exit?: ")
    clientSocket.close()
    if text_input.lower() == "y":
        sys.exit(0)
    pass



if __name__ == "__main__":
    main()
    pass