import socket,json,threading,time,datetime
from PyQt5.QtWidgets import QTableWidgetItem
# from excel import *

waitlist = None

def initstater(ip=str,port=int):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))
    outip,outport=sock.getpeername() #연결된 대상의 ip와, 포트번호를 보여준다.
    print(f"'{outip}'로 접속하였습니다, 포트는'{outport}'입니다")
    return sock


#--------------리시버 파트----------------------.
def receiver(sock):
    global waitlist,miniwaitlist
    miniwaitlist=None
    while True:
        작업종류설정=sock.recv(1024).decode("utf-8")
        if 작업종류설정=="가구매작업":
            print("가구매작업 결과물 데이터를 받았습니다.")
        #--------------넘어온 데이터로 엑셀 작업파트----------------------.
            # try:
            #     platform="쿠팡"
            #     workcom="박경희"
            #     kakao="개발중"
            #     product_title="경추베개"
            #     review="너무 좋아요, 우리 모두 그렇게 했으면 좋겠어요. \n 아니야 !!!"
            #     photoreview="X"
            #     pointuse=None 
            #     workstate="구매완료"
            #     product_price=13000
            #     add_exceldata(platform,workcom,kakao,product_title,review,photoreview,pointuse,workstate,product_price)
            # except:
            #     create_excel()

            # print("엑셀 작업중입니다.")
            # #쓰레드에 락을 걸어서 겹치지 않게 작업을 해야 한다.
            # print("소켓이 종료되었습니다.")
    #--------------서버정보업데이트----------------------.
        elif 작업종류설정=="서버정보업데이트":
            #--------------서버일감 데이터 받기----------------------.
            waitlist=sock.recv(8000).decode("utf-8")
            waitlist=json.loads(waitlist) 
            print("서버정보 업데이트 데이터를 받았습니다.")
            print(waitlist)
    
        elif 작업종류설정=="서버간소화정보":
            
            응답데이터=sock.recv(1024).decode("utf-8")
            print(f"서버간소화정보를 받았습니다.응답:{응답데이터}")
            miniwaitlist=응답데이터
        else:
            print(f"작업종류설정이 잘못들어왔습니다.{작업종류설정}")
            time.sleep(1)

#--------------데이터 보내는 파트.----------------------.
def socket_sender(sock,작업방식,가구매작업데이터=None):
    ##--------------작업방식 데이터 보내기. ----------------------
    sock.sendall(작업방식.encode("utf-8"))

    ##--------------1.가구매 작업 데이터 보내기.----------------------
    #1.가구매 작업 데이터 보내기.
    if 작업방식 == "가구매작업":
        print("가구매 작업 데이터를 보냅니다.")
        sock.sendall(json.dumps(가구매작업데이터).encode("utf-8"))

    ##--------------2.서버정보업데이트 정보 요청하기 ----------------------
    elif 작업방식 == "서버정보업데이트":
        print("서버정보업데이트 정보요청을 보냈습니다")

    elif 작업방식 == "서버수정데이터":
        print("서버정보업데이트 수정데이터를 보냈습니다")
        sock.sendall(json.dumps(waitlist).encode("utf-8"))
    
    elif 작업방식 == "서버간소화정보":
        print("서버간소화정보를 보냈습니다.")

def outdata():
    global waitlist
    return waitlist
#--------------쉽게 사용하기 위한 함수.----------------------.
def soket_start(ip,port):
    sock=initstater(ip,port)
    threading.Thread(target=receiver,args=(sock,)).start()
    return sock
    
#--------------사용방법을 설명해놓음.----------------------.
if __name__ == '__main__':
    가구매작업데이터={ 
            "URL": "Https://copang",
            "URL2" : "공백",
            "플랫폼" : "쿠팡",
            "카카오톡" : "개발중",
            "작업시간" : datetime.datetime.now().strftime('%Y-%m-%d-%H:%M'),
            "장바구니" : False,
            "포인트" : False,
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

       
