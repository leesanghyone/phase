import socket,json,threading,time,sys
from datetime import datetime,timedelta
# from Coupang_work_fungtion import *

#--------------실행자 함수다..----------------------.
def initstater(ip=str,port=int):
    global waitlist,workerlist,쓰레드락
    #--------------사전준비 자료다.----------------------.
    waitlist=[{"URL": "https://copang.com","작업시간" : (datetime.now()+timedelta(minutes=15)).strftime('%Y-%m-%d-%H:%M'),"플랫폼" : "쿠팡"},{"URL": "https://naver.com","작업시간" : (datetime.now()+timedelta(minutes=30)).strftime('%Y-%m-%d-%H:%M'),"플랫폼" : "네이버"}]
    workerlist=[]
    쓰레드락=threading.Lock()
    #--------------실행자 함수다..----------------------.
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((ip,port))
    sock.listen()
    print("서버를 창설했습니다.")
    c_sock,addr=sock.accept()
    print("클라이언트가 들어왔다.")
    return c_sock
#--------------리시버 파트이다.(데이터를 받음)----------------------.
def receiver(c_sock):
    global waitlist,stop_event
    while True:
    #--------------가구매작업을 처리한다.---------------------.   
        작업방식=c_sock.recv(1024).decode("utf-8")
        if 작업방식=="가구매작업":
            print("가구매작업을 데이터를 받겠습니다.")
            작업데이터=json.loads(c_sock.recv(4000).decode("utf-8"))
            with 쓰레드락:
                waitlist.append(작업데이터)
            print("가구매작업을 데이터를 받았습니다.")
            print(작업데이터)
    #--------------서버정보업데이트를 처리한다----------------------.            
        elif 작업방식=="서버정보업데이트":
            print("서버정보 업데이트를 클라이언트가 요청했습니다")

            #1.클라이언트에게 데이터 받을 준비해라.
            c_sock.sendall("서버정보업데이트".encode("utf-8"))
            
            #서버일감 정보를 보내준다.
            with 쓰레드락:
                server_waitlist=waitlist.copy()
            #원본 그대로 보내는 부분이다.
            보낼데이터=server_waitlist
            c_sock.sendall(json.dumps(보낼데이터).encode("utf-8"))
        
        elif 작업방식=="서버수정데이터":  
            print("서버수정데이터를 받았습니다")
            수정데이터=json.loads(c_sock.recv(4000).decode("utf-8"))
            with 쓰레드락:
                waitlist=수정데이터
            print(f"수정완료:{waitlist}")
            #-------------작동중인 타임 쓰레드 멈추고 새롭게 갈아끼우기.--------------------.     
            stop_event.set()
            #새로운 쓰레드 시작시키기.
            stop_event=threading.Event() #새롭게 변수에 들어가도, 쓰레드에 들어간 쓰레드이벤트는 사라지지않는다.
            time_thread=threading.Thread(target=Time_manager,args=(stop_event,))
            time_thread.start()
            
        elif 작업방식=="서버간소화정보":
            c_sock.sendall("서버간소화정보".encode("utf-8"))
            with 쓰레드락:
                보낼데이터=str(len(waitlist))
            print(f"서버간소화정보:{보낼데이터}")
            c_sock.send((보낼데이터).encode("utf-8"))

        else:
            print("작업방식이 잘못되었습니다.")


#--------------일을하는 작업자 파트.----------------------.
def worker(c_sock):
    global workerlist
    while True:
        #--------------받아온 자료로 일을 하는 파트다.----------------------.
        #-------------리소스 절약 파트다..------------------
        if len(workerlist)==0:
            print("일감이 없어서 대기중입니다.")
            time.sleep(10)
        #--------------실질적으로 일을하는 파트다.----------------------.
        elif len(workerlist) >=1:
            with 쓰레드락:
                work=workerlist.pop(0)
            url=work["URL"]
            print(f"작업중인 url:{url}")
            # minprice=work["minprice"]
            # maxprice=work["maxprice"]
            # page_view_time= work["page_view_time"]
            # moq= work["moq"]
            # jjim= work["jjim"]
            # optionmenus1= work["optionmenus1"]
            # optionmenus2= work["optionmenus2"]
            # jangbaguni= work["jangbaguni"]
            # point= work["point"]
            # msg="그냥 잘 배송해주면 좋구요."
            # coupang_start(url=url,minprice=minprice,maxprice=maxprice,page_view_time=page_view_time,moq=moq,jjim=jjim,optionmenus1=optionmenus1,optionmenus2=optionmenus2,jangbaguni=jangbaguni,point=point,msg=msg)
            # --------------작업한 녀석은 지워야 한다---------------------
            print("일감을 처리했습니다.")


            #--------------결과물을 클라측에 전송(엑셀자료)----------------------.
            # print("결과물을 클라측에 전송(엑셀자료)")
            # 엑셀작업데이터={
            #     "pc이름": pcname,
            #     "플랫폼": "https://copang.com",
            #     "카카오톡아이디": "https://copang.com",
            #     "작업시간": "https://copang.com",
            #     "상품명": "https://copang.com",
            #     "금액": "https://copang.com",
            #     "사용포인트": "https://copang.com",
            #     "리뷰": "https://copang.com",
            # }
            # c_sock.sendall(json.dumps(엑셀작업데이터).encode("utf-8"))
            # print("결과물을 클라측에 전송(엑셀자료) 완료")

            #--------------결과물을 클라측에 전송(엑셀자료)----------------------.
            #클라이언츠측에 서버간소화정보를 보내준다.
            c_sock.sendall("서버간소화정보".encode("utf-8"))
            with 쓰레드락:
                보낼데이터=str(len(waitlist))
                print(f"서버간소화정보:{보낼데이터}")
            c_sock.send((보낼데이터).encode("utf-8"))

#--------------타임매니저(웨잇리스트->워크리스트 일을 던져줌)----------
def Time_manager(stop_event):
    global waitlist, workerlist
    print("타임매니저 초기 작동시작")
    while not stop_event.is_set():
        print("타임매니저 무한 작동중")
        #-----------작업시간까지 대기하기----------
        with 쓰레드락:
            if not waitlist:
                print("대기 리스트가 비어있습니다. 대기 중...")
                time.sleep(10)
                continue
            예약시간 = datetime.strptime(waitlist[0]["작업시간"], '%Y-%m-%d-%H:%M')
            print(f"예약시간:{예약시간}")
        작업대기시간 = (예약시간 - datetime.now()).total_seconds() // 60
        if 작업대기시간 < 0:
            작업대기시간 = 0
        print(f"작업대기시간은 {작업대기시간}초 입니다.")
        time.sleep(작업대기시간)
        #쓰레드 종료 장치 넣어둠.
        if stop_event.is_set():
            print("타임매니저 작동종료")
            return
        #-----------변경사항 없는지 체크하기.----------
        with 쓰레드락:
            if 예약시간 == datetime.strptime(waitlist[0]["작업시간"], '%Y-%m-%d-%H:%M'):
                일감 = waitlist.pop(0)
                workerlist.append(일감)
            else:
                print("예약시간이 변경되었습니다. 다음 예약시간을 확인합니다.")
                continue


#--------------실행을 쉽게 도와주는 함수다.----------------------.
def socket_start(ip=str,port=int,workcomname=str):
    global pcname,stop_event
    #사전준비.
    pcname=workcomname
    stop_event=threading.Event()
    #실제 실행.
    c_sock=initstater(ip,port)
    receiver_thred=threading.Thread(target=receiver,args=(c_sock,))
    worker_thred=threading.Thread(target=worker,args=(c_sock,))
    Time_manager_thred=threading.Thread(target=Time_manager,args=(stop_event,))
    #쓰레드 시작.
    receiver_thred.start()
    worker_thred.start()
    Time_manager_thred.start()
    print("쓰레드 시작 완료")
    


#--------------사용설명을 도와주는 파트다.----------------------.
if __name__ == '__main__':
    socket_start("127.0.0.1",12000,"박경희")
