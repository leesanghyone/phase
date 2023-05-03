import socket,json,threading,time,sys
import socket,json,threading,time,sys
from Coupang_work_fungtion import *

def purchase_soket_Start(pc_name="이상현"):
    #####서버를 여는 역할을 한다. #######
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 12000))
    sock.listen()
    print("서버를 창설했습니다.")
    # ----------------------------------------------------------------
    #연결을 받고, 일을 하고, 데이터를 보내고, 종료한다.
    while True: 
        print("클라이언트를 기다리는 중입니다.")
        c_sock, addrs=sock.accept() 
        print("클라이언트가 들어왔다.")

        #작업방식을 설정하는 데이터.
        wark_way=c_sock.recv(1024).decode("utf-8")
        print(f"작업방식은 {wark_way}이다.(데이터를 받았다)")
        time.sleep(1) #이게 없으면 오류가 나네...

        #쿠팡 구매 작업하는 경우다.
        if wark_way == "구매작업": 
            print("구매작업으로 시작합니다.")
            #데이터를 받는 구간이다.
            url_soket_data=json.loads(c_sock.recv(1024).decode("utf-8"))#URL1, URL2
            platforminfo_soket_data=json.loads(c_sock.recv(1024).decode("utf-8")) #플랫폼,카카오톡, 
            PaymentOptions_soket_data=json.loads(c_sock.recv(1024).decode("utf-8"))#결제방식(일반,장바구니) , 포인트
            ActionOption_soket_data=json.loads(c_sock.recv(1024).decode("utf-8"))#(최소가격,최대가격), (찜작업,알림받기) , 페이지체류시간
            PurchaseOptions_soket_data=json.loads(c_sock.recv(1024).decode("utf-8"))#([[옵션1],[옵션2]...]) , 구매수량 , 배송메세지

            print(f"받은 메세지는 : {url_soket_data} 입니다")
            print(f"받은 메세지는 : {platforminfo_soket_data} 입니다")
            print(f"받은 메세지는 : {PaymentOptions_soket_data} 입니다")
            print(f"받은 메세지는 : {ActionOption_soket_data} 입니다")
            print(f"받은 메세지는 : {PurchaseOptions_soket_data} 입니다")


            ###------작업파트 :셀레니움 ------#### 
            url=url_soket_data[0]
            minprice=ActionOption_soket_data[0]
            maxprice=ActionOption_soket_data[1]
            page_view_time= ActionOption_soket_data[4]
            moq= PurchaseOptions_soket_data[1]
            jjim=ActionOption_soket_data[2]
            optionmenus1=PurchaseOptions_soket_data[0][0]
            optionmenus2=PurchaseOptions_soket_data[0][1]
            jangbaguni=PaymentOptions_soket_data[0]
            point=PaymentOptions_soket_data[1]
            msg=PurchaseOptions_soket_data[2]
            
            print(url,minprice,maxprice,page_view_time,moq,jjim,optionmenus1,optionmenus2,jangbaguni,point,msg)
            coupang_start(url=url,minprice=minprice,maxprice=maxprice,page_view_time=page_view_time,moq=moq,jjim=jjim,optionmenus1=optionmenus1,optionmenus2=optionmenus2,jangbaguni=jangbaguni,point=point,msg=msg)


            ####결과물 데이터를 보내기####
            IDinformation_soket_data=[pc_name,platforminfo_soket_data[0],"카톡개발중"]  #pc이름,플랫폼,카카오톡아이디
            Productinfo_soket_data=["가상의상품",19000,2000] #상품명,금액,사용포인트
            Review_soket_data=["행복","리뷰좋아요"] #리뷰
        
            send_group=[IDinformation_soket_data,Productinfo_soket_data,Review_soket_data]
            for send_data in send_group:
                c_sock.sendall(json.dumps(send_data).encode("utf-8"))
                time.sleep(2) #이게 없다면 서버 과부화가 걸린다.
                print("작업할 컴퓨터(서버측)에 데이터를 보냈다")
                    
            ###소켓종료하기####
            c_sock.close()
            print("서버를 종료했다.")
        #리뷰업데이트 작업시.
        elif wark_way=="test1":
            pass
        
        #리뷰작성기능 작동.
        elif wark_way=="test2":
            pass
        else:
            print(f"에러가남{wark_way}")
            print("재귀함수 작동한다.")
            purchase_soket_Start() #재귀함수다.


#사용방법을 설명한다.
if __name__=="__main__":
    purchase_soket_Start(pc_name="박경희")