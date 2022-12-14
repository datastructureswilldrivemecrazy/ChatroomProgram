import threading
import socket
host = '127.0.0.1'
port = 55555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host , port))
server.listen()
#initializing two lists which will store the clients and the nicknames assigned to them 
clients = []
nicknames = []
def broadcast (message):#sends the message to all the clients in the server
    for client in clients:
        client.send(message) 
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat'.encode('ascii'))
            nicknames.remove(nickname)    
            break
def receive():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f'{nickname} has joined the chat'.encode('ascii'))
        client.send(f'connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print("WELCOME   TO    BISHAL's   PRIVATE   CHATROOM")
print("CONNECT YOURSELF AS A CLIENT AND AHAVE FUN!!!")
print("__________________________________________________")
print("server online......checking for clients")
receive()