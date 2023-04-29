import datetime
import time

def main():
    # 사용자로부터 예약 시간 입력 받기
    print("예약 시간을 입력하세요. (24시간 형식) 예시: 17:30")
    reservation_time = input()

    # 입력된 시간을 datetime 객체로 변환
    now = datetime.datetime.now()
    reservation_hour, reservation_minute = map(int, reservation_time.split(':'))
    reservation_datetime = now.replace(hour=reservation_hour, minute=reservation_minute, second=0, microsecond=0)

    # 예약 시간이 이미 지난 경우, 다음 날로 설정
    if now > reservation_datetime:
        reservation_datetime += datetime.timedelta(days=1)

    # 현재 시간과 예약 시간 사이의 시간(초) 계산
    time_diff = (reservation_datetime - now).total_seconds()

    print(f"{reservation_datetime}에 알림이 설정되었습니다.")

    # 예약 시간까지 대기
    time.sleep(time_diff)

    # 알림 메시지 출력
    print("예약 시간입니다!")

if __name__ == "__main__":
    main()
