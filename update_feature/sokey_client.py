import socket,json,threading,time
# from excel import *


def initstater(ip=str,port=int):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))
    return sock
    

def receiver(sock):
    while True:
        작업종류설정=sock.recv(1024).decode("utf-8")
        if 작업종류설정=="가구매작업":
            print("가구매작업 결과물 데이터를 받았습니다.")

        elif 작업종류설정=="서버정보업데이트":
            print("서버정보 업데이트 데이터를 받았습니다.")
             
        else:
            print("작업종류설정이 잘못되었습니다.")


def socket_sender(sock,작업방식,가구매작업데이터):
    #작업방식 데이터 보내기.
    sock.sendall(작업방식.encode("utf-8"))
    #1.가구매 작업 데이터 보내기.
    if 작업방식 == "가구매작업":
        print("가구매 작업 데이터를 보냅니다.")
        sock.sendall(json.dumps(가구매작업데이터).encode("utf-8"))
    #2.서버정보업데이트 정보 요청하기.
    if 작업방식 == "서버정보업데이트":
        print("서버정보업데이트 정보 요청을 보냅니다.")

def soket_start(ip,port):
    sock=initstater(ip,port)
    threading.Thread(target=receiver,args=(sock,)).start()
    return sock
    

#사용방법이다.
if __name__ == '__main__':
    sock=soket_start("127.0.0.1",12000)

    while True:
        작업방식=input("작업방식을 설정해주세요:")
        가구매작업데이터={ 
            "url": "Https://copang",
            "최대가격" : 100000,
            "최소가격" : 10000,
        }
        socket_sender(sock,작업방식,가구매작업데이터)

