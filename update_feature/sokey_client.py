import socket,json,threading,time
from excel import *


def initstater(ip=str,port=int):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(ip,port)
    return sock
    

def receiver(sock):
    while True:
        작업종류설정=sock.recv(1024).decode("utf-8")
        if 작업종류설정=="가구매작업":
            print("가구매작업 결과물 데이터를 받았습니다.")

            보낼데이터={ 
                "url": "Https://copang",
                "최대가격" : 100000,
                "최소가격" : 10000,
            }
            sock.sendall(json.dumps(보낼데이터).encode("utf-8"))

        elif 작업종류설정=="서버정보업데이트":
            pass 
        else:
            print("작업종류설정이 잘못되었습니다.")
        
