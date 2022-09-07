import socket
import threading
#asking for a nickname for the clients who will be connected to the server
nickname = input("What's your alias!")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
                pass
            else :
                print(message)
        except:
            print("an error occured")
            client.close()
            break
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))
#Threading...
receive_thread = threading.Thread(target=receive)  
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()

