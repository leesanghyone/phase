import socket,json,threading,time,sys
from datetime import datetime
# from Coupang_work_fungtion import *

#--------------실행자 함수다..----------------------.
def initstater(ip=str,port=int):
    global waitlist,workerlist,쓰레드락
    #--------------사전준비 자료다.----------------------.
    waitlist=[{"url": "https://copang.com","작업시간" : "2023-05-04-23:42","플랫폼" : "쿠팡"},{"url": "https://naver.com","작업시간" : "2022-05-04-05:42","플랫폼" : "네이버"}]
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
    global waitlist
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
            # Time_manager() #쓰레드로 새롭게 분배해줘야 한다.
            print(f"수정완료:{waitlist}")

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
    global waitlist,workerlist
    #--------------받아온 자료로 일을 하는 파트다.----------------------.
        #-------------리소스 절약 파트다..------------------
    if len(workerlist)==0:
        print("일감이 없어서 대기중입니다.")
        time.sleep(5)
        #--------------실질적으로 일을하는 파트다.----------------------.
    for work in workerlist:
        print(work)
        url=work["url"]
        minprice=work["minprice"]
        maxprice=work["maxprice"]
        page_view_time= work["page_view_time"]
        moq= work["moq"]
        jjim= work["jjim"]
        optionmenus1= work["optionmenus1"]
        optionmenus2= work["optionmenus2"]
        jangbaguni= work["jangbaguni"]
        point= work["point"]
        msg="그냥 잘 배송해주면 좋구요."
        # coupang_start(url=url,minprice=minprice,maxprice=maxprice,page_view_time=page_view_time,moq=moq,jjim=jjim,optionmenus1=optionmenus1,optionmenus2=optionmenus2,jangbaguni=jangbaguni,point=point,msg=msg)
        #--------------작업한 녀석은 지워야 한다----------------------
        with 쓰레드락:
            workerlist.remove(work)
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

#--------------타임매니저(웨잇리스트->워크리스트 일을 던져줌)----------
def Time_manager():
    global waitlist,workerlist
    while True:
        #-----------작업시간까지 대기하기----------
        with 쓰레드락:
            예약시간=str(waitlist[0]["작업시간"])
        작업대기시간=예약시간-datetime.now()
        time.sleep(작업대기시간)
        #-----------변경사항 없는지 체크하기.----------
        with 쓰레드락:
            if waitlist[0]["작업시간"]==예약시간:
                일감=waitlist.pop(0)
            elif waitlist[0]["작업시간"]!=예약시간:
                Time_manager()
        #-----------워크리스트로 일감 던지기.----------
        workerlist.append(일감)


    
#--------------실행을 쉽게 도와주는 함수다.----------------------.
def socket_start(ip=str,port=int,workcomname=str):
    global pcname
    pcname=workcomname
    c_sock=initstater(ip,port)
    threading.Thread(target=receiver,args=(c_sock,)).start()
    # threading.Thread(target=worker,args=(c_sock,)).start()
    # threading.Thread(target=Time_manager).start()

#--------------사용설명을 도와주는 파트다.----------------------.
if __name__ == '__main__':
    socket_start("127.0.0.1",12000)
