import socket,json,threading,time,sys
import socket,json,threading,time,sys
from Coupang_work_fungtion import *


def initstater():
    global waitlist,workerlist
    #1. 준비재료
    waitlist=[]
    workerlist=[]
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("127.0.0.1",12000))
    sock.listen()
    c_sock,addr=sock.accept()
    print("클라이언트가 들어왔다.")
    return c_sock

def receiver(c_sock):

    #1.작업방식을 설정하는 데이터.
    작업방식=c_sock.recv(1024).decode("utf-8")
    if 작업방식=="서버정보업데이트":
        print("서버정보 업데이트를 클라이언트가 요청했습니다")
    elif 작업방식=="가구매작업":
        print("가구매작업을 데이터를 받았습니다.")

def worker(c_sock):
    pass

def timeamanager():
    pass
