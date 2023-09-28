import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('localhost', 8002))

sock.listen(5)

room, chat = list(), list()

while True:
    try:
        novoSock, _ = sock.accept()
        msg_room = novoSock.recv(1024).decode()

        try:
            new_room = msg_room.split(',')[1]
            new_msg = msg_room.split(',')[0]

        except IndexError:
            new_room = msg_room
            new_msg = ''

        if (new_room in room) and (new_room != '') and (new_msg != ''):
            chat[room.index(new_room)].append(new_msg)

        elif new_msg != '':
            room.append(new_room)
            chat.append([])
            chat[room.index(new_room)].append(new_msg)

        else:
            room.append(new_room)
            chat.append([])

        room_string = ','.join(room)
        chat_string = ','.join('/'.join(i) for i in chat)

        msg_room = f'{chat_string},{room_string}'

        novoSock.send(msg_room.encode())

    except KeyboardInterrupt:
        sock.close()
