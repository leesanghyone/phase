import pywin32
import time

# 카카오톡 채팅방의 토큰을 입력합니다.
token = "YOUR_TOKEN"

# 채팅방의 이름을 입력합니다.
room_name = "YOUR_ROOM_NAME"

# 특정 키워드를 입력합니다.
keyword = "YOUR_KEYWORD"

# 답변을 입력합니다.
response = "YOUR_RESPONSE"

# pywin32를 사용하여 카카오톡 채팅방에 연결합니다.
kakaotalk = pywin32.genpy.KakaoTalk()
kakaotalk.Login(token)

# 채팅방을 찾습니다.
room = kakaotalk.FindRoom(room_name)

# 채팅방의 메시지를 확인합니다.
while True:
    messages = room.GetMessages()
    for message in messages:
        # 메시지에 특정 키워드가 포함되어 있는지 확인합니다.
        if keyword in message.body:
            # 답변을 보냅니다.
            room.SendMessage(response)

    time.sleep(1)