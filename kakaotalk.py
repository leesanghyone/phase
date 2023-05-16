import win32gui,time
import win32process
import time, win32con, win32api, win32gui, ctypes
import time, win32con, win32api, win32gui, ctypes
import win32clipboard
import pandas as pd
from chatgpt_automation import *
import chatgpt_automation
from pynput.keyboard import Key, Listener


#업데이트 사항1.
# 카카오톡과 지피티를 연결하였다. 여기서 지피티를 임포트해서 사용한다. 





#현재 실행 중인 모든 창 핸들 가져오기
def kakao_room_serach():
    #1.현재 실행 중인 모든 창 핸들 가져오기
    while True:
        windows = []
        win32gui.EnumWindows(lambda hwnd, lParam: windows.append(hwnd), None)
        kakao_title=[]
        #1.카카오톡 프로세스 저장
        for window in windows:
            try:
                # 창 제목, 윈도우 클래스 이름, 해당 프로세스의 PID 출력
                window_title = win32gui.GetWindowText(window)
                window_class_name = win32gui.GetClassName(window)
                _, process_id = win32process.GetWindowThreadProcessId(window)
                # print(f"창 제목: {window_title}, 윈도우 클래스 이름: {window_class_name}, PID: {process_id}")
                
                if window_title == "카카오톡":
                    카카오톡프로세스아이디=process_id
                    print(f"카카오톡 프로세스 아이디:{카카오톡프로세스아이디}")
            except:
                pass
        #2.카카오톡 대화창 찾기.
        for window in windows:
            try:
                # 창 제목, 윈도우 클래스 이름, 해당 프로세스의 PID 출력
                window_title = win32gui.GetWindowText(window)
                window_class_name = win32gui.GetClassName(window)
                _, process_id = win32process.GetWindowThreadProcessId(window)
                # print(f"창 제목: {window_title}, 윈도우 클래스 이름: {window_class_name}, PID: {process_id}")
                #카카오톡 대화창은 클래스명이 #32770이다. 
                if process_id==카카오톡프로세스아이디 and window_class_name == "#32770":
                    kakao_title.append(window_title)  
            except:
                pass
        if len(kakao_title) < 1:
            print(f"카카오톡 대화창이 없습니다.")
            time.sleep(5)
            win32api.MessageBox(win32con.NULL, '카카오톡 창이 업습니다.', '카카오톡 창 과다.', win32con.MB_OK)
        elif len(kakao_title) > 1:
            print(f"한개 이상의 창이 켜져 있습니다.")
            win32api.MessageBox(win32con.NULL, '카카오톡 창이 한개 이상켜져있습니다.', '카카오톡 창 과다.', win32con.MB_OK)
            time.sleep(5)
        elif len(kakao_title) == 1:
            print(f"대화창수집완료하였습니다:{kakao_title[0]} ")
            return kakao_title[0]


# 조합키 쓰기 위해
def PostKeyEx(hwnd, key, shift, specialkey):
    global w
    w = win32con
    #사전실행 변수들.
    PBYTE256 = ctypes.c_ubyte * 256
    _user32 = ctypes.WinDLL("user32")
    GetKeyboardState = _user32.GetKeyboardState
    SetKeyboardState = _user32.SetKeyboardState
    PostMessage = win32api.PostMessage
    SendMessage = win32gui.SendMessage
    FindWindow = win32gui.FindWindow
    IsWindow = win32gui.IsWindow
    GetCurrentThreadId = win32api.GetCurrentThreadId
    GetWindowThreadProcessId = _user32.GetWindowThreadProcessId
    AttachThreadInput = _user32.AttachThreadInput
    MapVirtualKeyA = _user32.MapVirtualKeyA
    MapVirtualKeyW = _user32.MapVirtualKeyW
    MakeLong = win32api.MAKELONG
    #실질적으로 작동하는 함수들이다.
    if IsWindow(hwnd):

        ThreadId = GetWindowThreadProcessId(hwnd, None)

        lparam = MakeLong(0, MapVirtualKeyA(key, 0))
        msg_down = w.WM_KEYDOWN
        msg_up = w.WM_KEYUP

        if specialkey:
            lparam = lparam | 0x1000000

        if len(shift) > 0:  # Если есть модификаторы - используем PostMessage и AttachThreadInput
            pKeyBuffers = PBYTE256()
            pKeyBuffers_old = PBYTE256()

            SendMessage(hwnd, w.WM_ACTIVATE, w.WA_ACTIVE, 0)
            AttachThreadInput(GetCurrentThreadId(), ThreadId, True)
            GetKeyboardState(ctypes.byref(pKeyBuffers_old))

            for modkey in shift:
                if modkey == w.VK_MENU:
                    lparam = lparam | 0x20000000
                    msg_down = w.WM_SYSKEYDOWN
                    msg_up = w.WM_SYSKEYUP
                pKeyBuffers[modkey] |= 128

            SetKeyboardState(ctypes.byref(pKeyBuffers))
            time.sleep(0.01)
            PostMessage(hwnd, msg_down, key, lparam)
            time.sleep(0.01)
            PostMessage(hwnd, msg_up, key, lparam | 0xC0000000)
            time.sleep(0.01)
            SetKeyboardState(ctypes.byref(pKeyBuffers_old))
            time.sleep(0.01)
            AttachThreadInput(GetCurrentThreadId(), ThreadId, False)
            
        else:  # Если нету модификаторов - используем SendMessage
            SendMessage(hwnd, msg_down, key, lparam)
            SendMessage(hwnd, msg_up, key, lparam | 0xC0000000)


# PostKeyEx(hwndListControl, ord('A'), [w.VK_CONTROL], False)
# PostKeyEx(hwndListControl, ord('C'), [w.VK_CONTROL], False)


##챗팅방 찾아가기###
def kakao_chatroom_go(kakao_title):
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)

    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0,kakao_title)  
    #안정성위해필요
    time.sleep(1)   
    enter(hwndkakao_edit3)
    #글자 초기화 시켜놓기
    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, "")

def enter(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    time.sleep(0.5)

def send_msg(kakao_title:str,msg:str):
    ###타겟 챗팅방###
    hwndMain = win32gui.FindWindow(None,kakao_title)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)
    # win32gui.SetForegroundWindow(hwndMain)

    ###타겟 챗팅방에서 메세지 전송###
    win32api.SendMessage(hwndEdit,win32con.WM_SETTEXT, 0, msg) # 채팅창 입력
    enter(hwndEdit)

def send_img(kakao_title,imgpath):
    ###타겟 챗팅방###
    hwndMain = win32gui.FindWindow( None,kakao_title)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)
    # win32gui.SetForegroundWindow(hwndMain)

    ###타겟 챗팅방에서 메세지 전송###
    win32api.SendMessage(hwndEdit,win32con.WM_SETTEXT, 0, "진혁아 안녕?") # 채팅창 입력
    enter(hwndEdit)

    ###타겟 챗팅방에서 이미지 보내기###
    cliboard_imacopy(imgpath)

    time.sleep(0.5)
    win32gui.PostMessage(hwndEdit, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON,0) #클릭을 안하면 복붙이 씹힌다.
    PostKeyEx(hwndEdit, ord('V'), [w.VK_CONTROL], False)
    PostKeyEx(hwndEdit, ord('V'), [w.VK_CONTROL], False)

    time.sleep(0.5)
    hwndMain2 = win32gui.FindWindow( None,"#32770 (Dialog)")
    hwndEdit3 = win32gui.FindWindowEx(hwndMain2, None, "#32770", None)
    enter(hwndEdit3)

    win32gui.PostMessage(hwndMain, win32con.WM_CLOSE, 0, 0)


#이미지 클립보드에 복사하기.
def cliboard_imacopy(filepath):
    from io import BytesIO
    import win32clipboard
    from PIL import Image
    def send_to_clipboard(clip_type, data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(clip_type, data)
        win32clipboard.CloseClipboard()

    # filepath ='5.png'
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data) #클립보드 복사.



#판다스로, 최신 메세지와 ,구메세지를 구분이 가능하다.
# def kakakao_getText(hwnd):
#     w = win32con
#     hwndMain = win32gui.FindWindow(None,hwnd)
#     hwndEdit = win32gui.FindWindowEx(hwndMain, None, "EVA_VH_ListControl_Dblclk", None)
    
#     PostKeyEx(hwndEdit, ord('A'), [w.VK_CONTROL], False)
#     time.sleep(0.5)
#     PostKeyEx(hwndEdit, ord('C'), [w.VK_CONTROL], False)
#     win32clipboard.OpenClipboard()
#     content = win32clipboard.GetClipboardData()
#     win32clipboard.CloseClipboard()
#     print(content)
#     a = content.split('\r\n')   # \r\n 으로 스플릿 __ 대화내용 인용의 경우 \r 때문에 해당안됨
#     df = pd.DataFrame(a)    # DF 으로 바꾸기
#     print(df)
#     df[0] = df[0].str.replace('\[([\S\s]+)\] \[(오전|오후)([0-9:\s]+)\] ', '')  # 정규식으로 채팅내용만 남기기
#     print(df[0])
#     print(df.index[-2], df.iloc[-2, 0])
#     return df.index[-2], df.iloc[-2, 0]


def kakao_get_inputText(hwnd):
    hwndMain = win32gui.FindWindow(None,hwnd)
    hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RICHEDIT50W", None)
    time.sleep(0.1) #이거 없다면 "a" 눌리는 버그가 생긴다.
    PostKeyEx(hwndEdit, ord('A'), [win32con.VK_CONTROL], False) 
    time.sleep(0.1)
    PostKeyEx(hwndEdit, ord('C'), [win32con.VK_CONTROL], False)
    win32clipboard.OpenClipboard()
    content = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    # print(content)
    return content


def kakao_inputPast(hwnd,past_data):
    hwndMain = win32gui.FindWindow(None,hwnd)
    hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RICHEDIT50W", None)

    # 클립보드 열기
    print(past_data)
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard() #없으면 복사를 잘 못함.
    win32clipboard.SetClipboardText(past_data)
    win32clipboard.CloseClipboard()
    
    time.sleep(0.1)
    PostKeyEx(hwndEdit, ord('A'), [win32con.VK_CONTROL], False)
    time.sleep(0.1)
    PostKeyEx(hwndEdit, ord('V'), [win32con.VK_CONTROL], False)


#현재 채팅방에서, 입력창의 내용을 복사해서 gpt를 돌리고 결과값을 넣어준다.
def kakao_gpt():
    hwnd=kakao_room_serach()
    inputdate=kakao_get_inputText(hwnd)
    chatgpt_input(inputdate)
    print(f"입력값은 :\n {inputdate}")
    while True:
        if chatgpt_automation.Gpt_result_data != None:
            gpt_result=chatgpt_automation.Gpt_result_data
            break
    kakao_inputPast(hwnd,gpt_result)
    chatgpt_automation.Gpt_result_data=None

#f12누를때마다. gpt가 실행된다.
def on_press(key):
    global inputdata
    if key == Key.f12 :
        # 파이썬 코드가 실행됩니다.
        kakao_gpt()


def keyboard_listener():
    with Listener(on_press=on_press) as listener:
        listener.join()


def kakao_gpt_start():
    chatgpt_start()
    threading.Thread(target=keyboard_listener).start()



#------사용법------#
if __name__=="__main__": 
    # kakao_inputPast("상준","HELLOW")
    #1.퍈매자 채팅방 이름 찾기.
    # kakao_room_serach()

    #2.채팅방에 이미지 보내기.
    # img_path='C:/Users/lsh92/Desktop/asdasd.png'
    # send_img("상준",img_path)

    kakao_gpt_start()






