import socket


class Room:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('localhost', 8002))

    def send_msg(self, msg, room):
        if msg != '':
            self.sock.send(f'{msg},{room}'.encode())

            total_msg = self.sock.recv(100000000).decode().split(',')

            room_msg = total_msg[int(total_msg.index(room) - (len(total_msg) / 2))].split('/')

            return room_msg

        else:
            self.sock.send(f'{room}'.encode())

            total_msg = self.sock.recv(100000000).decode().split(',')

            room_msg = total_msg[int(total_msg.index(room) - (len(total_msg) / 2))].split('/')

            return room_msg
