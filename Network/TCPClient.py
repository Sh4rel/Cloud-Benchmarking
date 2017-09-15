import sys
import socket
import time

def main():
    """ main """
    target_host = '127.0.0.1'
    target_port = 9999

    if len(sys.argv) != 2:              # error handling
        print 'Error: invalid arguments'
    else:
        num_of_thread = int(sys.argv[1])

    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((target_host, target_port))

    f = open('TestFile64KB','rb')
    start = time.time()
    # send 64 bytes
    client.send(bytes(111111111111111111111111111))

    # receive data
    response = client.recv(4096)
    duration = start - time.time()
    print response

if __name__ == '__main__':
    main()