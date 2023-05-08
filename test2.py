import threading
import time

def Time_manager(stop_event):
    n=0
    while not stop_event.is_set():
        print(f"작업 수행 {n}번쨰")
        time.sleep(1)
        n=n+1
        if stop_event.is_set():
            print(f"쓰레드 종료할것입니다{n}번쨰")
        
        

# 처음 Time_manager 쓰레드 시작
stop_event = threading.Event()
time_manager_thread = threading.Thread(target=Time_manager, args=(stop_event,))
time_manager_thread.start()


def new_thred():
    global stop_event
    stop_event.set()
    stop_event = threading.Event()
    time_manager_thread = threading.Thread(target=Time_manager, args=(stop_event,))
    time_manager_thread.start()

while True:
    input("Enter 키를 누르면 기존 쓰레드를 중지하고 새로운 쓰레드를 시작합니다: ")
    new_thred()

    # # 새로운 이벤트 객체 생성 및 초기화
    # stop_event = threading.Event()

    # # 새로운 Time_manager 쓰레드 시작
    # time_manager_thread = threading.Thread(target=Time_manager, args=(stop_event,))
    # time_manager_thread.start()
