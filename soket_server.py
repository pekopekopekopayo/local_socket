from socket import *
import threading
import time

PORT = 8888

# 접속중인 모든 유저 
global clients
clients = {} 

# 메세지를 전체에게 보냄
def send(sender_addr, message):
    print(f"{sender_addr}: {message}")
    for addr in clients:
        if sender_addr != addr:
            clients[addr].send(f"{sender_addr}: {message}".encode('utf-8'))
    
# 유저 당 하나의 스레드 생성 후 메세지를 보내기 전까지 기다림
def receive(addr, sock):
    while True:
        recvData = sock.recv(1024)
        send(addr, recvData.decode('utf-8'))

sever_soket = socket(AF_INET, SOCK_STREAM)
sever_soket.bind(('localhost', PORT))
sever_soket.listen()
print("%d: server 기동" %PORT)

# 메인 스레드가 종료되면 안되므로 루프 너무 부담을 주고 싶진 않으므로 슬립을 취함
while True:
    time.sleep(1)
    client_sokect, client_address = sever_soket.accept()
    print(f"{str(client_address)}에서 접속이 되었습니다.")

    clients[client_address] = client_sokect
    receiver = threading.Thread(target=receive, args=(client_address, client_sokect))
    
    receiver.start()
