from socket import *
import threading
import time

PORT = 8888

def send(sock):
    while True:
        message = input(">>>")
        print(f"(me): {message}")
        sock.send(message.encode('utf-8'))


def receive(sock):
    while True:
        message = sock.recv(1024)
        print("\n" + message.decode('utf-8'))

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', PORT))

print('접속 완료')

sender = threading.Thread(target=send, args=(client_socket,))
receiver = threading.Thread(target=receive, args=(client_socket,))

sender.start()
receiver.start()

while True:
    time.sleep(1)