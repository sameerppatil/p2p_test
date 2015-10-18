__author__ = 'Sameer'
import socket


def main():
    serverport = 12000
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('', serverport))
    print "The server is ready to receive"
    while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        print("Got the message %s from %s" %(message, clientAddress))
        host, port = socket.getnameinfo(clientAddress, socket.AF_INET)
        print ("Host, port pair: %s, %s" % (host, port))
    serverSocket.close()
    pass


if __name__ == "__main__":
    main()
    pass