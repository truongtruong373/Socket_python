import socket
import select

HEADER_LENGTH = 10
HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf-8"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, SERVER_PORT))
server_socket.listen()

socket_list = [server_socket]
clients = {}


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False

        message_length = int(message_header.decode(FORMAT).strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)

    for notified_socket in read_sockets:
        # nếu server nhận một access mới
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

            socket_list.append(client_socket)
            clients[client_socket] = user

            print(f"Accepted new connection from {client_address[0]}:{client_address[1]}"
                  f"username: {user['data'].decode(FORMAT)}")

        else:
            message = receive_message(notified_socket)
            if message is False:
                print(f"Closed connection from {clients[notified_socket]}")
                socket_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]

            print(f"Received message from {user['data'].decode(FORMAT)}: {message['data'].decode(FORMAT)}")

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        socket_list.remove(notified_socket)
        del clients[notified_socket]
