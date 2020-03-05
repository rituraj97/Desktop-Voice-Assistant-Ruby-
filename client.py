import socket, threading

def send(uname):
    while True:
        msg = input('\nMe: ')
        data=uname+':'+msg
        cli_sock.send(data.encode())

def receive():
        while True:
            data = cli_sock.recv(20801)
            print(" ")
            x=data.decode()
            print('\n' + x)

if __name__ == "__main__":   
    # socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = localhost
    PORT = 3000

    uname = input('Enter your name to enter the chat:')

    cli_sock.connect((HOST, PORT))     
    print('Connected to remote host...')


    thread_send = threading.Thread(target = send,args=[uname])
    thread_send.start()


    thread_receive = threading.Thread(target = receive)
    thread_receive.start()
