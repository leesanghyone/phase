import socket,json,threading,time,datetime
from PyQt5.QtWidgets import QTableWidgetItem
from excel import *
import queue


def initstater(ip=str,port=int):
    global 쓰레드락,선입선출
    쓰레드락=threading.Lock()
    선입선출=queue.Queue()
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))
    return sock

#--------------리시버 파트----------------------.
def receiver(sock):
    while True:
        받은데이터=sock.recv(8000).decode("utf-8")
        print("서버측에서 데이터를 받았습니다.")
        선입선출.put(받은데이터)
#--------------리시버 워크작업소----------------------.
#존재이유는: 리시버측에서 작업을 하는 도중에 새로운 작업데이터가 오면, 리시버측에서 작업을 하지 못하고, 새로운 작업데이터를 받아야한다.
def receiver_worker(sock,guiparent):
    global waitlist
    waitlist=None
    while True:
        if 선입선출.empty() == True: #데이터가 없으면 1초 쉰다.
            print("일할 데이터가 없다.")
            time.sleep(1)
        작업데이터=json.loads(선입선출.get())
        print("작업을 시작합니다.")
        if 작업데이터["작업종류"] == "엑셀작업":
            print("엑셀작업이다.")
            try:
                print("서버측에 30초 엑셀파일을 보냈다.")
                time.sleep(10)
                platform=작업데이터["엑셀작업데이터"]["플랫폼"]
                workcom=작업데이터["엑셀작업데이터"]["pc이름"]
                kakao=작업데이터["엑셀작업데이터"]["카카오톡"]
                product_title=작업데이터["엑셀작업데이터"]["상품명"]
                review=작업데이터["엑셀작업데이터"]["리뷰"]
                photoreview="X"
                pointuse=작업데이터["엑셀작업데이터"]["사용포인트"]
                workstate=작업데이터["엑셀작업데이터"]["작업상태"]
                product_price=작업데이터["엑셀작업데이터"]["상품금액"]
                add_exceldata(platform,workcom,kakao,product_title,review,photoreview,pointuse,workstate,product_price)
            except:
                create_excel()
            finally:
                print("엑셀 작업이 끝났습니다.")
        #--------------서버정보업데이트----------------------.
        elif 작업데이터["작업종류"] == "서버정보업데이트": 
            waitlist=작업데이터["서버정보업데이트"]
            print("서버정보 업데이트 데이터를 받았습니다.")
        #--------------서버 간소화 정보----------------------.
        elif 작업데이터["작업종류"] == "서버간소화정보": 
            outip,outport=sock.getpeername()
            print(outip,outport)
            서버갯수=작업데이터["간소화정보"]
            print(f"서버간소화정보 데이터를 받았습니다. 응답: {서버갯수}")
            #+++++컴퓨터 추가시 추가작업+++++ 
            if guiparent != None: # 컴퓨터의 미니 작업갯수 표시를 바꾼다.
                if outip=="127.0.0.1" and outport == 12000:  #박경희
                    guiparent.server1_btn.setText(서버갯수) #부모의 gui에 서버숫자를 바꾼다.
                    print("서버간소화정보를 Gui에 업데이트 완료")
                elif outip=="127.0.0.1" and outport ==12001:  #임태원
                    guiparent.server2_btn.setText(작업데이터["간소화정보"])
                    print("서버간소화정보를 Gui에 업데이트 완료")
                elif outip=="127.0.0.1" and outport ==12002: #이상준
                    guiparent.server3_btn.setText(작업데이터["간소화정보"])
                    print("서버간소화정보를 Gui에 업데이트 완료")
                elif outip=="127.0.0.1" and outport ==12003: #이상현.
                    guiparent.server4_btn.setText(작업데이터["간소화정보"])
                    print("서버간소화정보를 Gui에 업데이트 완료")

#--------------데이터 보내는 파트.----------------------.
def socket_sender(sock,작업방식,가구매작업데이터=None): 
    ##--------------작업방식 데이터 보내기. ----------------------
    with 쓰레드락: #락을 걸어서 쓰레드가 겹치지 않게 한다.(일시적으로 한다 그러니 전체를 묶어도 된다)
        ##--------------1.가구매 작업 데이터 보내기.----------------------
        #1.가구매 작업 데이터 보내기.
        if 작업방식 == "가구매작업":
            보낼데이터={"작업종류": "가구매작업","가구매작업데이터": 가구매작업데이터}
            sock.sendall(json.dumps(보낼데이터).encode("utf-8"))
            print("가구매 작업 데이터를 보냈습니다.")

        ##--------------2.서버정보업데이트 정보 요청하기 ----------------------
        elif 작업방식 == "서버정보업데이트":
            보낼데이터={"작업종류": "서버정보업데이트","서버정보업데이트": 가구매작업데이터}
            sock.sendall(json.dumps(보낼데이터).encode("utf-8"))
            print("서버정보업데이트 데이터를 보냈습니다.")
            
        elif 작업방식 == "서버수정데이터":
            print("서버정보업데이트 수정데이터를 보냈습니다")
            보낼데이터={"작업종류": "서버수정데이터","서버수정데이터": waitlist}
            sock.sendall(json.dumps(보낼데이터).encode("utf-8"))
            print("서버수정데이터 데이터를 보냈습니다.")
                    
        elif 작업방식 == "서버간소화정보":
            보낼데이터={"작업종류": "서버간소화정보"}
            sock.sendall(json.dumps(보낼데이터).encode("utf-8"))
            print("서버간소화정보 보냈습니다.")

#--------------쉽게 사용하기 위한 함수.----------------------.
def soket_start(ip,port,guiparent=None):
    sock=initstater(ip,port)
    threading.Thread(target=receiver,args=(sock,)).start()
    threading.Thread(target=receiver_worker,args=(sock,guiparent)).start()
    return sock
    
#--------------사용방법을 설명해놓음 .----------------------.
if __name__ == '__main__':
    가구매작업데이터={ 
            "URL": "Https://copang",
            "URL2" : "공백",
            "플랫폼" : "쿠팡",
            "카카오톡" : "개발중",
            "작업시간" : datetime.now().strftime('%Y-%m-%d-%H:%M'),
            "장바구니" : False,
            "포인트" : False,
            "알림받기" : False,
            "최소가격" : 10000,
            "최대가격" : 10000,
            "찜작업" : True,
            "알림받기" : False,
            "페이지체류시간" : 130,
            "옵션1" : [["블랙,""화이트","그레이"]],
            "옵션2" : 3,
            "구매수량" : 1,
            "배송메세지" : "그냥 배송 잘 부탁드려요."
        }
    박경희컴퓨터sock=soket_start("127.0.0.1",12000) #한번실행되면 계속 연결을 유지한다.
    while True: #테스트 때문에 필요한것이다.
        작업방식=input("작업방식을 설정해주세요:") #추후에 gui에서 일회용으로 계속 데이터를 보낼것이다.
        socket_sender(박경희컴퓨터sock,작업방식,가구매작업데이터) #데이터를 보낸다.

       
