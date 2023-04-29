import socket,json,threading,time,sys
import socket,json,threading,time,sys
# from Coupang_work_fungtion import *


def initstater(ip=str,port=int):
    global waitlist,workerlist
    #1. 준비재료
    waitlist=[{"작업시간": "15:43","플랫폼" : "쿠팡"},{"작업시간": "13:30","플랫폼" : "네이버"}] #1.작업시간, 2.플랫폼
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
        ###########################################
        if 작업방식=="가구매작업":
            print("가구매작업을 데이터를 받았습니다.")
            작업데이터=json.loads(c_sock.recv(1024).decode("utf-8"))
            waitlist.append(작업데이터)
            print(작업데이터["url"],작업데이터["최대가격"])
        ###########################################    
        elif 작업방식=="서버정보업데이트":
            print("서버정보 업데이트를 클라이언트가 요청했습니다")
            
            #2. 클라이언트에게 작업방식을 보내준다.
            c_sock.sendall("서버정보업데이트".encode("utf-8"))
            
            #3.서버일감 정보를 보내준다.
            for work in waitlist:
                sendwork=[waitlist.index(work),work["작업시간"],work["플랫폼"],waitlist.index(work)] #1.인덱스, 2.작업시간, 3.플랫폼 ,4.고유인덱스
                c_sock.sendall(json.dumps(sendwork).encode("utf-8"))
            c_sock.sendall("작업끝".encode("utf-8"))

            #클라이언측의서 응답을 받는다.
            응답=c_sock.recv(1024).decode("utf-8")

            if 응답=="수정있음":
                while True:
                    수정데이터=json.loads(c_sock.recv(1024).decode("utf-8"))
                    if 수정데이터=="수정끝":
                        break
                    waitlist[수정데이터[4]]["url"]=수정데이터[1]
                    waitlist[수정데이터[4]]["작업시간"]=수정데이터[2]
                    waitlist[수정데이터[4]]["플랫폼"]=수정데이터[3]
                    print("수정완료")

                    #인덱스를 수정사항이 있다면, 수정한다.
                    if 수정데이터[0]!=수정데이터[4]:
                        고유인덱스=수정데이터[4]
                        고유데이터=waitlist[고유인덱스]
                        변경인덱스=수정데이터[0]
                        변경데이터=waitlist[변경인덱스]
                        waitlist[고유인덱스]=변경데이터
                        waitlist[변경인덱스]=고유데이터
                        print("인덱스를 수정했습니다.")
            elif 응답=="수정없음":
                pass


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

