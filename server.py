import socket
import threading

def main():
    IPHOST = "127.0.0.1"
    PORT = 1025
    MAXCONNECTIONS = 5 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind( (IPHOST,PORT) )
    s.listen(MAXCONNECTIONS)

    while True:
        pass





if __name__ == "__main__":
    main()
