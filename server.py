import socket
import sys

def create_socket():
    """Create a Socket(connect two computers)"""
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print('Socket creation error: '+ str(msg))

def bind_socket():
    """Binding the socket and listening for connections"""
    try:
        global host
        global port
        global s

        print('Binding the Port: ' + str(port))
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print('Socket binding error: '+ str(msg) + '\n' + 'Retrying...')
        bind_socket()

def socket_accept():
    """Establish connection with client (socket must be listening)"""
    conn, address = s.accept()
    print('Connection has been established!' + 'IP ' + address[0] + ' | Port' + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    """Send commands to client"""
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end='')

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()