from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import undetected_chromedriver as uc
import random,os
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys 
from jamo import h2j, j2hcj 
import pyautogui,time,random,ctypes
from ctypes import wintypes
from bs4 import BeautifulSoup

#웨이팅 함수 불러오기.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def make_driver():
    global driver
    global ismobile
    ismobile=False
    try:
        chromedriver_autoinstaller.install()
        options=uc.ChromeOptions()

        options.user_data_dir ="C:/cookie"

        #모르지만 추가적으로 넣는 옵션들이다.
        # options.set_capability("detach", True)
        options.add_argument("--no-first-run --no-service-autorun --password-store=basic")    
        options.add_argument('--disable-logging')

        #비번을 하드에 저장한다?
        # options.add_argument("--password-store=basic") #
        # #기존의 저장된 비밀번호 입력할까요? 질문을 꺼버린다.
        # options.add_experimental_option(
        #     "prefs",
        #     {
        #         "credentials_enable_service": False,
        #         "profile.password_manager_enabled": False,
        #     },
        # )
        #특정버전으로 실행하기 위함이다.
        # uc.Chrome(options=options,version_main = 111)
        
        #드라이브 선언하기.
        driver=uc.Chrome(options=options)
        

        return driver
    except:
        print("논값을 뱉어낸다")
        driver=None
        return driver

##키보드 타이핑 모듈###

def keboard_typing(area):

    wintypes.ULONG_PTR = wintypes.WPARAM
    hllDll = ctypes.WinDLL("User32.dll", use_last_error=True)
    VK_CAPITAL = 0x14
    VK_HANGUL = 0x15


    class MOUSEINPUT(ctypes.Structure):
        _fields_ = (("dx",          wintypes.LONG),
                    ("dy",          wintypes.LONG),
                    ("mouseData",   wintypes.DWORD),
                    ("dwFlags",     wintypes.DWORD),
                    ("time",        wintypes.DWORD),
                    ("dwExtraInfo", wintypes.ULONG_PTR))


    class HARDWAREINPUT(ctypes.Structure):
        _fields_ = (("uMsg",    wintypes.DWORD),
                    ("wParamL", wintypes.WORD),
                    ("wParamH", wintypes.WORD))


    class KEYBDINPUT(ctypes.Structure):
        _fields_ = (("wVk",         wintypes.WORD),
                    ("wScan",       wintypes.WORD),
                    ("dwFlags",     wintypes.DWORD),
                    ("time",        wintypes.DWORD),
                    ("dwExtraInfo", wintypes.ULONG_PTR))


    class INPUT(ctypes.Structure):
        class _INPUT(ctypes.Union):
            _fields_ = (("ki", KEYBDINPUT),
                        ("mi", MOUSEINPUT),
                        ("hi", HARDWAREINPUT))
        _anonymous_ = ("_input",)
        _fields_ = (("type",   wintypes.DWORD),
                    ("_input", _INPUT))


    def check_is_hangul_state() -> bool:
        if hllDll.GetKeyState(VK_HANGUL) == 1:
            return True
        else:
            return False
        
    ###한글,영어 미리 체크하기###
    
    if check_is_hangul_state()==True:
        pass
    else:
        pyautogui.press("hangul")

    ##자음-초성/종성
    cons = {'r':'ㄱ', 'R':'ㄲ', 's':'ㄴ', 'e':'ㄷ', 'E':'ㄸ', 'f':'ㄹ', 'a':'ㅁ', 'q':'ㅂ', 'Q':'ㅃ', 't':'ㅅ', 'T':'ㅆ',
           'd':'ㅇ', 'w':'ㅈ', 'W':'ㅉ', 'c':'ㅊ', 'z':'ㅋ', 'x':'ㅌ', 'v':'ㅍ', 'g':'ㅎ'}
    ##모음-중성
    vowels = {'k':'ㅏ', 'o':'ㅐ', 'i':'ㅑ', 'O':'ㅒ', 'j':'ㅓ', 'p':'ㅔ', 'u':'ㅕ', 'P':'ㅖ', 'h':'ㅗ', 'hk':'ㅘ', 'ho':'ㅙ', 'hl':'ㅚ',
           'y':'ㅛ', 'n':'ㅜ', 'nj':'ㅝ', 'np':'ㅞ', 'nl':'ㅟ', 'b':'ㅠ',  'm':'ㅡ', 'ml':'ㅢ', 'l':'ㅣ'}
    # 자음-종성
    cons_double = {'rt':'ㄳ', 'sw':'ㄵ', 'sg':'ㄶ', 'fr':'ㄺ', 'fa':'ㄻ', 'fq':'ㄼ', 'ft':'ㄽ', 'fx':'ㄾ', 'fv':'ㄿ', 'fg':'ㅀ', 'qt':'ㅄ'}
    
    #모음,자음
    모음=[v for k,v in cons.items()]
    자음=[v for k,v in vowels.items()]
    자음종성=[v for k,v in cons_double.items()]
    
    jamo_str = j2hcj(h2j(area)) #글자를 분리해줌.
    
    def convert(t):
        if t in 모음:
            new_con=[k for k,v in cons.items() if v==t][0]            
        elif t in 자음:
            new_con=[k for k,v in vowels.items() if v==t][0]
        elif t in 자음종성:
            new_con=[k for k,v in cons_double.items() if v==t][0]
        elif t == " ":
            new_con="space"
        else:
            new_con=t #!@## 이런데이터는 그냥 그대로 아웃풋으로 념겨준다.
        return new_con  
    for a in jamo_str:
        result=convert(a)
        
        if len(result) == 2: #결과값이 2이면, 하나씩 입력해!
            for r in range(len(result)): # 길이만큼
                pyautogui.press(result[r])
                time.sleep(0.05+random.random()/20)
        else: #입력값이 한글자씩이면, 하나씩 입력하면 됨
            pyautogui.press(result)
            time.sleep(0.03+random.random()/100)



def randclick_cssver(css_selector):
    element=driver.find_element(By.CSS_SELECTOR,css_selector)
    width=element.size["width"]
    height=element.size["height"]
    # 엘리먼트안 속성을 담긴다. 그 안에 사이즈가 존재한다.
    targetX=random.randint(int(width*-0.4),int(width*0.4))
    targetY=random.randint(int(height*-0.4),int(height*0.4))

    ActionChains(driver).move_to_element(element).move_by_offset(targetX,targetY).pause(1).click().perform()

def exist_check_css(css_selector):
    element=driver.find_element(By.CSS_SELECTOR,css_selector)
    element_y=element.location["y"]
    element_height=element.size["height"]

    while True:
        cur_window=driver.get_window_size()
        cur_win_height=cur_window["height"]
        cur_win_scrolly=driver.execute_script("return window.scrollY")

        if cur_win_scrolly + cur_win_height < element_y + element_height +120 : #엘리먼트가 아래에 있다
            return False
        if cur_win_scrolly > element_y -120: #엘리먼트가 위에 있다.
            return False
        return True


def get_pattern():
    global index #메인보드함수에서 받아온다.
    
    #어느컴퓨터에서도 저장경로 통일화 시키기.
    filepath=filepathfix()

    if ismobile==False: #피시버전
        with open(f"{filepath}/Pc_Scroll.txt","r",encoding="utf-8") as f:
            line=f.readlines()

        #인덱스 조건 만들기.
        if index=="start":
            index=random.randint(0,len(line)-1)
        if index >= len(line):
            index=random.randint(0,len(line)-1)

        #언패킹을 하기 위한, 파싱작업이다.
        choice_pattern=line[index].rstrip().split("#") #실제로 인덱스를 뽑아내는곳이다.
        _,sx,sy,dy,dt=choice_pattern
        index=index+1
        return int(sx),int(sy),int(dy),float(dt)

    else: #모바일 버전일떄.
        with open(filepath,"r",encoding="utf-8") as f:
            line=f.readlines()
        
        #인덱스 조건 만들기.
        if index=="start":
            index=random.randint(0,len(line)-1)
        if index >= len(line):
            index=random.randint(0,len(line)-1)

        choice_pattern=line[index].rstrip()
        _,sx,sy,dy,dt=choice_pattern.split("#")
        index=index+1
        return int(sx),int(sy),int(dy),float(dt) #해상도는 모바일마다 다르다. 시작값을 설정하지말자.


def rand_move(direction="down"): # 스크롤 1회의 함수다. 1번할떄, 200을 갈수도, 114를 갈 수도 있다.
    sx,sy,dy,dt=get_pattern()
    
    if ismobile==False: #피시버전이라면
        sx=sx+offset_X
        sy=sy+offset_Y
        #방향에 따른 스크롤 값 정하기.
        if direction=="up":
            rand_y=dy*114 #업이다 결과적으로 마이너스면 된다.
        if direction=="down": #다운일떄
            rand_y=-dy*114 #결과적으로 양수여야 함.

    else: #모바일버전이라면

        #가로값
        screen_width=driver.get_window_size()["width"] #모바일은 기종마다 값이 다르다. 녹화했다가 오류가 날 확률이 있다. 기존의 화면의 값을가지고 온다.
        w_min_value=screen_width/2-screen_width*0.4
        w_max_value=screen_width/2+screen_width*0.4

        #세로값
        screen_height=driver.get_window_size()["height"] #
        h_min_value=screen_height/2-screen_height*0.4
        h_max_value=screen_height/2+screen_height*0.4
        #화면의 값을 받아와서, sx, sy값을 정한다.
        sx=random.randint(int(w_min_value),int(w_max_value))
        sy=random.randint(int(h_min_value),int(h_max_value))
    
        if direction=="up":
            rand_y=dy #결과적으로 음숙값이면 된다.
        if direction=="down":
            rand_y=-dy

    ActionChains(driver).scroll(sx,sy,0,rand_y).perform()
    
    #작업간격타임.
    dt=dt*offset_T
    time.sleep(dt)

def scroll_cssVer(css_selector):
    global offset_X,offset_Y,offset_T,index
    #사전재료다.
    element=driver.find_element(By.CSS_SELECTOR,css_selector)
    element_y=element.location["y"]
    element_height=element.size["height"]
    #랜덤값 재료.
    index="start" #초기값만 준다. 그 다음은 와일트루안에서 돈다.
    offset_X=random.randint(-200,200)
    offset_Y=random.randint(-100,100)
    offset_T=random.uniform(0.3,0.5)

    while not exist_check_css(css_selector):
        cur_win=driver.get_window_size()
        cur_win_height=cur_win["height"]
        cur_win_scrolly=driver.execute_script("return window.scrollY")

        if cur_win_scrolly + cur_win_height < element_y+ element_height +120 : 
            rand_move(direction="down")
        if cur_win_scrolly > element_y -120:
            rand_move(direction="up")



#엘리먼트 버전의 커스텀함수.
def randclick_elver(element):

    width=element.size["width"]
    height=element.size["height"]

    targetX=random.randint(int(width*-0.4),int(width*0.4))
    targetY=random.randint(int(height*-0.4),int(height*0.4))

    ActionChains(driver).move_to_element(element).move_by_offset(targetX,targetY).pause(1).click().perform() #한번에 합친 함수가 있네....

def exist_check_el(element):
    element_y=element.location["y"]
    element_height=element.size["height"]

    while True:
        cur_window=driver.get_window_size()
        cur_win_height=cur_window["height"]
        cur_win_scrolly=driver.execute_script("return window.scrollY")

        if cur_win_scrolly + cur_win_height < element_y + element_height +120 : #엘리먼트가 아래에 있다
            return False
        if cur_win_scrolly > element_y -120: #엘리먼트가 위에 있다.
            return False
        return True
    

def scroll_elVer(element):
    global offset_X,offset_Y,offset_T,index
    #사전재료다.
   
    #랜덤값 재료.
    index="start" #초기값만 준다. 그 다음은 와일트루안에서 돈다.
    offset_X=random.randint(-200,200)
    offset_Y=random.randint(-100,100)
    #속도를 관장하는 부분이다.
    offset_T=random.uniform(0.3,0.5)

    while not exist_check_el(element):
        #엘리먼트.
        element_y=element.location["y"]
        element_height=element.size["height"]
        #윈도우화면관련.
        cur_win=driver.get_window_size()
        cur_win_height=cur_win["height"]
        cur_win_scrolly=driver.execute_script("return window.scrollY")

        if cur_win_scrolly + cur_win_height < element_y+ element_height +120 : 
            rand_move(direction="down")
        if cur_win_scrolly > element_y -120:
            rand_move(direction="up")

def scroll_time(t=60,direction="down",speed="normal",rand_offset=True):
    global offset_X,offset_Y,offset_T,index
    
    #랜덤값 재료.
    index="start" #초기값만 준다. 그 다음은 와일트루안에서 돈다.
    if rand_offset:
        offset_X=random.randint(-200,200)
        offset_Y=random.randint(-100,100)
        
    curent_time=time.time()

    if rand_offset:
        #스피드관련. 타임의 랜덤값을 준다.
        if speed == "normal":
            offset_T=random.uniform(0.8,1.2)
        elif speed == "fast":
            offset_T=random.uniform(0.1,0.3)
        else: #SLOW버전이다.
            offset_T=random.uniform(1.1,1.5)
            
    #실질적인 움직이는 함수.
    while True:
        if time.time() -curent_time >= t:
            break
        sx,sy,dy,dt=get_pattern()
        
        sx=sx+offset_X
        sy=sy+offset_Y
            
        if direction=="down": #다운일때 
            dy=-dy*114
        else: #업일떄.
            dy=dy*114
        
        ActionChains(driver).scroll(sx,sy,0,dy).perform()
        dt=dt*offset_T
        time.sleep(dt)

def switch_handle(n):
    driver.switch_to.window(driver.window_handles[n])

def scroll_click_Css(css_selector):
    scroll_cssVer(css_selector)
    time.sleep(0.5)
    randclick_cssver(css_selector)

def scroll_click_El(element):
    scroll_elVer(element)
    time.sleep(0.5)
    randclick_elver(element)


#동적인 페이지 스크롤 하기#
def scroll_actionPage(css_selector,direction="down",speed="fast",t_freature=False,t=30): #엘리먼트가 아래에 있을떄만 사용가능함.
    global offset_X,offset_Y,offset_T,index

    #스크롤타임함수안의, x,y,time 랜덤값 만들기.
    offset_X=random.randint(-200,200)
    offset_Y=random.randint(-100,100)
    index="start"

    #스피드관련. 타임의 랜덤값을 준다.
    if speed == "normal":
        offset_T=random.uniform(0.8,1.2)
    elif speed == "fast":
        offset_T=random.uniform(0.3,0.5)
    else: #SLOW버전이다.
        offset_T=random.uniform(1.1,1.5)

    cur_time=time.time()

    while not exist_check_css(css_selector):
        scroll_time(t=0.1,direction=direction,speed=speed,rand_offset=False)

        if t_freature==True:
            if time.time()-cur_time >=t:
                break


#좀 특수한 상황에서 쓴다. (html에 css가 안잡힐때 예)동적페이지가 해당 css 처음에 못 불러올떄.
#위에와 차이점은, 해당요소가 나타날떄까지 스크롤이다. 위에는 화면에 위치시키는 차이가 존재함.
def scroll_actionPage2(target_css,start_handle=None,direction="down",speed="fast"):
    switch_handle(start_handle)
    while True:
        if existEl_check_Css(target_css):
            break
        elif existEl_check_Css(target_css)==False:
            scroll_time(t=0.5,direction=direction,speed=speed)
        else:
            print("무한스크롤 종료")



def existEl_check_Css(target_Css):
    html=driver.page_source
    soup=BeautifulSoup(html,"html.parser")
    exist=soup.select_one(target_Css)

    if exist == None:
        return False
    if exist != None:
        return True
    
def element_typer(css_selector,texts):
    element=driver.find_element(By.CSS_SELECTOR,css_selector)

    for i in range(len(texts)):
        element.send_keys(texts[i])
        t=random.uniform(0.25,0.55)
        time.sleep(t)


def el_wait(waittime=int,css_selector=str,startfungtion=None,errfungtion=None):
    try:
        WebDriverWait(driver,waittime).until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector)))
        startfungtion
        print("해당엘리먼트를 찾았습니다.")

    except:
        print("해당 엘리먼트가 나타나지 않았습니다.")
        #예외시 실행될 함수를 여기다 넣으면 된다.
        errfungtion
        pass

#컴퓨터마다. 경로 통일화 하기.
def filepathfix():
    if os.path.abspath("./").find("SILJUNCOUPANG") == -1:
        filepath=os.path.abspath("./SILJUNCOUPANG").replace("\\","/")
    else:
        filepath=os.path.abspath("./").replace("\\","/")
    return filepath



if __name__ == "__main__":
    driver=make_driver()
    time.sleep(2)
    driver.get("https://www.coupang.com/")
    input()
    # driver.implicitly_wait(10)
    # scroll_time(5)
  
 