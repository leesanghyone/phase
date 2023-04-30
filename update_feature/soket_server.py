import socket,json,threading,time,sys
import socket,json,threading,time,sys
# from Coupang_work_fungtion import *

#--------------실행자 함수다..----------------------.
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
#--------------리시버 파트이다.(데이터를 받음)----------------------.
def receiver(c_sock):
    while True:
    #--------------가구매작업을 처리한다.---------------------.   
        작업방식=c_sock.recv(1024).decode("utf-8")
        if 작업방식=="가구매작업":
            print("가구매작업을 데이터를 받겠습니다.")
            작업데이터=json.loads(c_sock.recv(1024).decode("utf-8"))
            waitlist.append(작업데이터)
            print("가구매작업을 데이터를 받았습니다.")
            print(작업데이터)

    #--------------서버정보업데이트를 처리한다----------------------.            
        elif 작업방식=="서버정보업데이트":
            print("서버정보 업데이트를 클라이언트가 요청했습니다")
            
            #1. 클라이언트에게 작업방식을 보내준다.
            c_sock.sendall("서버정보업데이트".encode("utf-8"))
            
            #서버일감 정보를 보내준다.
            for work in waitlist:
                c_sock.sendall(json.dumps(work).encode("utf-8"))
            c_sock.sendall("작업끝".encode("utf-8"))
            
        else:
            print("작업방식이 잘못되었습니다.")

#--------------일을하는 작업자 파트.----------------------.
def worker(c_sock):
    #--------------받아온 자료로 일을 하는 파트다.----------------------.
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
        coupang_start(url=url,minprice=minprice,maxprice=maxprice,page_view_time=page_view_time,moq=moq,jjim=jjim,optionmenus1=optionmenus1,optionmenus2=optionmenus2,jangbaguni=jangbaguni,point=point,msg=msg)
    #--------------결과물을 클라측에 전송(엑셀자료)----------------------.
    print("결과물을 클라측에 전송(엑셀자료)")
    엑셀작업데이터={
        "pc이름": "https://copang.com",
        "플랫폼": "https://copang.com",
        "카카오톡아이디": "https://copang.com",
        "작업시간": "https://copang.com",
        "상품명": "https://copang.com",
        "금액": "https://copang.com",
        "사용포인트": "https://copang.com",
        "리뷰": "https://copang.com",
    }
    c_sock.sendall(json.dumps(엑셀작업데이터).encode("utf-8"))
    print("결과물을 클라측에 전송(엑셀자료) 완료")

#--------------타임매니저(웨잇리스트->워크리스트 일을 던져줌)----------
def timeamanager():
    pass
#--------------실행을 쉽게 도와주는 함수다.----------------------.
def socket_start(ip=str,port=int):
    c_sock=initstater(ip,port)
    threading.Thread(target=receiver,args=(c_sock,)).start()
    threading.Thread(target=worker,args=(c_sock,)).start()

#--------------사용설명을 도와주는 파트다.----------------------.
if __name__ == '__main__':
    socket_start("127.0.0.1",12000)

