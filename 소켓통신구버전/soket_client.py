import socket,json,threading,time
from excel import *

##클라이언트 측이다.
def so_Worker(ip=str,port=int,soketGuiclass=None):
    #소켓 만들기
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #소켓연결하기.
    sock.connect((ip,port))
    
    #작업방식 전달.
    time.sleep(1) #너무 빨라도 버그가 난다.
    sock.sendall("구매작업".encode("utf-8"))
    print("작업방식을 보냄.")

#2.-------------------서버에 데이터 보내기-------------.
    send_group=[url_soket_data,platforminfo_soket_data,PaymentOptions_soket_data,ActionOption_soket_data,PurchaseOptions_soket_data]
    for send_data in send_group:
        sock.sendall(json.dumps(send_data).encode("utf-8"))
        time.sleep(1) #이게 없다면 서버 과부화가 걸린다.
        print("작업할 컴퓨터(서버측)에 데이터를 보냈다")

#3.----------------서버측에서 결과물이 넘어오는 파트-------------.
    IDinformation_soket_data=json.loads(sock.recv(1024).decode("utf-8")) #pc이름,플랫폼,카카오톡아이디
    Productinfo_soket_data=json.loads(sock.recv(1024).decode("utf-8")) #상품명,금액,사용포인트
    Review_soket_data=json.loads(sock.recv(1024).decode("utf-8")) #리뷰
    print(f"받은 데이터: {IDinformation_soket_data}") 
    print(f"받은 데이터: {Productinfo_soket_data}") 
    print(f"받은 데이터: {Review_soket_data}") 
    #------실시간 작업컴상태 업데이트하기.------------
    soketGuiclass.박경희_작업컴상태=True
    soketGuiclass.C_parck_check_btn.setEnabled(True)

#4--------------넘어온 데이터로 엑셀 작업파트----------------------.
    try:
        platform="쿠팡"
        workcom="박경희"
        kakao="개발중"
        product_title="경추베개"
        review="너무 좋아요, 우리 모두 그렇게 했으면 좋겠어요. \n 아니야 !!!"
        photoreview="X"
        pointuse=None 
        workstate="구매완료"
        product_price=13000
        add_exceldata(platform,workcom,kakao,product_title,review,photoreview,pointuse,workstate,product_price)
    except:
        create_excel()

    print("엑셀 작업중입니다.")
    #쓰레드에 락을 걸어서 겹치지 않게 작업을 해야 한다.
    print("소켓이 종료되었습니다.")


#--------------------------끝--------------------------------------


########전송 데이터를 설정하는 함수다.#############
def so_inputdata(url=list,platforminfo=list,PaymentOptions=list,ActionOption=list,PurchaseOptions=list):
    global url_soket_data,platforminfo_soket_data,PaymentOptions_soket_data,ActionOption_soket_data,PurchaseOptions_soket_data
    url_soket_data=url     #URL1, URL2
    platforminfo_soket_data=platforminfo #플랫폼,카카오톡, 
    PaymentOptions_soket_data=PaymentOptions #결제방식(일반,장바구니) , 포인트
    ActionOption_soket_data=ActionOption #(최소가격,최대가격), (찜작업,알림받기) , 페이지체류시간
    PurchaseOptions_soket_data=PurchaseOptions #([[옵션1],[옵션2]...]) , 구매수량 , 배송메세지
    


#---------------데이터 보내는 함수.------------------------------
def so_Send_data(ip=str,port=int,soketGuiclass=None):
    threading.Thread(target=so_Worker,args=(ip,port,soketGuiclass)).start()


#---------------사용방법--------------------------------
if __name__=="__main__":
    url=["url1","url2"] #URL1, URL2
    platforminfo=["쿠팡","개발중"] #플랫폼,카카오톡, 
    PaymentOptions=["보통구매",False] #결제방식(일반,장바구니) , 포인트
    ActionOption=[12000,13000,True,True,30] #(최소가격,최대가격), (찜작업,알림받기) , 페이지체류시간
    PurchaseOptions=[[1,None],2,"배송메세지."] #([[옵션1],[옵션2]...]) , 구매수량 , 배송메세지
    
    #핵심은 아래2가지다.
    so_inputdata(url=url,platforminfo=platforminfo,PaymentOptions=PaymentOptions,ActionOption=ActionOption,PurchaseOptions=PurchaseOptions)
    so_Send_data("127.0.0.1",12000,object) #2.데이터를 보낸다.#사용방법을 설명한다.