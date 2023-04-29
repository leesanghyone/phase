import socket,json,threading,time,sys
import socket,json,threading,time,sys
# from Coupang_work_fungtion import *


def initstater(ip=str,port=int):
    global waitlist,workerlist
    #1. 준비재료
    waitlist=[{"url": "https://copang.com","작업시간" : 100000,"플랫폼" : "쿠팡"},{"url": "https://naver.com","작업시간" : 20000,"플랫폼" : 30000}]
    workerlist=[]
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((ip,port))
    sock.listen()
    print("서버를 창설했습니다.")
    c_sock,addr=sock.accept()
    print("클라이언트가 들어왔다.")
    return c_sock

def receiver(c_sock):
    while True:
        #1.작업방식을 설정하는 데이터.
        작업방식=c_sock.recv(1024).decode("utf-8")
        if 작업방식=="가구매작업":
            print("가구매작업을 데이터를 받았습니다.")
            작업데이터=json.loads(c_sock.recv(1024).decode("utf-8"))
            waitlist.append(작업데이터)
            print(작업데이터["url"],작업데이터["최대가격"])
            
        elif 작업방식=="서버정보업데이트":
            print("서버정보 업데이트를 클라이언트가 요청했습니다")
            
            #1. 클라이언트에게 작업방식을 보내준다.
            c_sock.sendall("서버정보업데이트".encode("utf-8"))
            
            #서버일감 정보를 보내준다.
            for work in waitlist:
                serverwork=[work["url"],work["작업시간"],work["플랫폼"]]
                c_sock.sendall(json.dumps(serverwork).encode("utf-8"))
            c_sock.sendall("작업끝".encode("utf-8"))
            



        else:
            print("작업방식이 잘못되었습니다.")

def worker(c_sock):
    pass

def timeamanager():
    pass

def socket_start(ip=str,port=int):
    c_sock=initstater(ip,port)
    threading.Thread(target=receiver,args=(c_sock,)).start()
    threading.Thread(target=worker,args=(c_sock,)).start()


if __name__ == '__main__':
    socket_start("127.0.0.1",12000)

