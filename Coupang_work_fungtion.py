from undetective_selenium import *
import random,re
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys 
from urllib import parse

##쿠팡 url에서 검색어,상품아이디 추출하는 함수.
def coupang_url_extract(url):
    global serch_keyword,serch_product_id
    serch_keyword = re.search(r"q=([^&]*)", url).group(1)
    serch_keyword=parse.unquote(serch_keyword)
    serch_keyword=serch_keyword.replace("+", " ")
    serch_product_id = int(re.search(r"products/(\d+)", url).group(1))
    print(f"검색키워드:{serch_keyword},상품아이디{serch_product_id}")

    return str(serch_keyword),int(serch_product_id)

def chrome_start(pc_name="박경희"):
    global driver, pcname
    pcname=pc_name
    driver=make_driver()
    driver.maximize_window()
    driver.get("https://www.coupang.com/")
    driver.implicitly_wait(10)

def Ac1_insert():
    chrome_start()
    time.sleep(random.uniform(1,2))
    element_typer("#headerSearchKeyword",serch_keyword)
    time.sleep(random.uniform(1,2))
    #엔터치기.
    driver.find_element(By.CSS_SELECTOR,"#headerSearchKeyword").send_keys(Keys.ENTER)


#가격필터 설정하기.
def price_filter(min_price,max_price):
    scroll_cssVer(".search-filter-options.search-price-filter")
    elements=driver.find_elements(By.CSS_SELECTOR,".param-pricerange")
    elements[0].send_keys(min_price)
    elements[1].send_keys(max_price)
    randclick_cssver(".btn-price-submit")

#가짜 페이지를 클릭하는 함수를 만들어야 함.
def fake_product(stat_handle=0,work_page=None,work_num=2,work_time=20):
    switch_handle(stat_handle)
    #해당페이지에서 작업할 경우.
    if work_page != None:
        select_page(work_page)
        time.sleep(random.uniform(1,3))
    #현재페이지의 상품을 수집을한다.
    Product_explore()
    #작업할 갯수를 설정한다.
    work_indexs=random.sample(Pure_Product_indexs,work_num)
    print(f"작업할 갯수는{work_num}, 작업할 인덱스는{work_indexs}")
    #상품 속성 불러오기.
    elements=driver.find_elements(By.CSS_SELECTOR,".search-product")
    for count in work_indexs:
        scroll_click_El(elements[count])
        time.sleep(3)
        pageview(start_handle=stat_handle+1,scroll_t=work_time)
        time.sleep(1)
        driver.close()
        switch_handle(stat_handle)
        time.sleep(1)

def Ac2_faketime(work_page=None,work_num=2,work_time=20):
    fake_product(stat_handle=0,work_page=work_page,work_num=work_num,work_time=work_time)


def Ac3_price_filter(minprice=None,maxprice=None):
    if minprice != None:
        price_filter(minprice,maxprice)


def Product_explore():
    global Pure_Product_ids,Pure_Product_indexs
    html=driver.page_source
    soup=BeautifulSoup(html,"html.parser")

    items=soup.select(".search-product")
    Pure_Product_ids=[]
    Pure_Product_indexs=[]
    for item in items:
        product_id=int(item.attrs["data-product-id"])
        #순수상품만 남긴다.
        if item.select_one(".search-product-wrap") !=None: #베스트아이템 아닌경우.
            if item.select_one(".ad-badge")==None: #광고상품이 아닌 경우.
                Pure_Product_ids.append(product_id)
                Pure_Product_indexs.append(int(items.index(item)))
            
def select_page(target_page=2):
    btns=driver.find_elements(By.CSS_SELECTOR,".btn-page>a")

    for btn in btns:
        if int(btn.text)==target_page:
            print(f"{btn.text}해당페이지로 이동")
            scroll_click_El(btn)
            break

#타겟을 서치하는 함수 만들어야 한다.
def target_serch(start_handle=0,start_page=2):
    global target_informations
    #상품 데이터를 수집한다.
    switch_handle(start_handle)
    while True:
        Product_explore()
        if serch_product_id in Pure_Product_ids:
            print("해당페이지에 상품이 존재한다.")

            #타겟 상품의 정보 추가하기(페이지,인덱스)
                #현재 페이지 찾아내기.
            btns=driver.find_elements(By.CSS_SELECTOR,".btn-page>a")
            for btn in btns:
                if len(btn.get_attribute("class")) >=1:
                    target_page=int(btn.text)
                    print(f"타겟 페이지는{target_page}")
                #타겟 인덱스 찾아내기.(중요함)
            target_index=Pure_Product_indexs[Pure_Product_ids.index(serch_product_id)]
                #타겟정보를 찐으로 담는다.
            target_informations={"target_page":target_page,"target_index":target_index}
            print(f"타겟페이지는 {target_page}, 타겟상품의 인덱스는{target_index}")
            break
        else: 
            print("해당페에지에 상품이 존재하지 않는다.")
            select_page(start_page)
            start_page=start_page+1

#페이지 스크롤 하는 함수 만들어야 됨.
def pageview(start_handle=1,scroll_t=30):
    switch_handle(start_handle)
    cur_time=time.time()

    #상품 더보기 클릭하기.<*상페의 상품더보기가 있든 없든, css걸린다. style속성값으로 유무를 구분한다.*>
    element=driver.find_element(By.CSS_SELECTOR,".product-detail-seemore")
    try:
        if element.get_attribute("style") == 'display: block;':
            print("상품더보기 상품 버튼이 존재한다.")
            scroll_click_Css("#productDetail > div.product-detail-seemore > div")
    except:
        print("상세페이지 더보기 없음.")
    #오류방지용(동적페이지라 밑에 속성을 css 다 안불러옴,)
    scroll_actionPage2(".sdp-review__title",start_handle,"down","fast")
    
    #시간초 채울떄까지 위아래 반복으로 이동한다.
    while True:
        if time.time() - cur_time >= scroll_t:
            break
        #아래로 이동한다.
        scroll_cssVer(".sdp-review__title")
        if time.time() - cur_time >= scroll_t:
            break
        #위로 이동한다.(쿠팡은 클래스로 집는게 좋다.)
        scroll_cssVer(".prod-buy-btn")
        
def cur_page():
    btns=driver.find_elements(By.CSS_SELECTOR,".btn-page>a")
    for btn in btns:
        if len(btn.get_attribute("class")) >=1:
            page=int(btn.text)
            print(f"타겟 페이지는{page}")
    return page

#타겟을 클릭하고 ,페이지 뷰까지 한번에 처리한다.
def target_go(start_handle=0,page_view_time=30):
    switch_handle(start_handle)
    target_page=target_informations["target_page"]
    target_index=target_informations["target_index"]

    if cur_page() != target_page:
        select_page(target_page)
        time.sleep(random.uniform(1,2))

    #상품 속성 불러오기.
    elements=driver.find_elements(By.CSS_SELECTOR,".search-product")
    scroll_click_El(elements[target_index])
    time.sleep(random.uniform(1,3))
    pageview(start_handle=start_handle+1,scroll_t=page_view_time)

def Ac4_targetgo(page_view_time):
    target_serch()
    target_go(page_view_time=page_view_time)

#결제전 사전 셋팅.
    #구매수량 입력하는 함수. 완성됨.
def purchase_quantity(num=int):
    element=driver.find_element(By.CSS_SELECTOR,".prod-quantity__input")
    scroll_elVer(element)
    #기존의 데이터 지우기.
    element.send_keys(Keys.CONTROL,"a")
    element.send_keys(Keys.DELETE)
    element.send_keys(num)

    time.sleep(random.uniform(1,3))
    #구매옵션을 설정하는 함수다.
def general_payoption(num1=int,num2=int):
    print("일반옵션 메뉴입니다..")
    select_option=[]
    select_option.append(num1)
    select_option.append(num2)

        #해당페이지에 구매옵션이 있는 경우다. #오류(.prod-option__item") 의외의 css는 하위메뉴 선택후 그 다음이 안됨
    main_elements=driver.find_elements(By.CSS_SELECTOR,".prod-option__item")
    for main in main_elements:
        try: #메인메뉴가 엘리먼트중에, 짝퉁으로 속성에 들어가는 경우가 있다.
            time.sleep(random.uniform(1,3))
            scroll_click_El(main)
            time.sleep(1)
            # #하위메뉴 선택하는 구간.
            sub_elements=driver.find_elements(By.CSS_SELECTOR,".prod-option__list")
                #상위메뉴와 인덱스로 연결한다.
            sub_elements2=sub_elements[main_elements.index(main)] #0번째 작업때, 0번 하위메뉴를 불러온다.
                #하위메뉴 선택지 선택지 하나하나다.
            sub_elements3=sub_elements2.find_elements(By.CSS_SELECTOR,".prod-option-dropdown-item")
                #하위메뉴를 클릭한다.
            sub_elements3[select_option[main_elements.index(main)]-1].click() #sub_elements3 인덱스가 하위메뉴 선택지다.
            time.sleep(random.uniform(1,3))
        except:
            pass

def image_payopion(num1=int,num2=int):
    #상위메뉴 사이즈 클릭하고 선택하기. 없는 경우도 대비한다.
    print("의류옵션메뉴입니다.")
    try:    
        scroll_click_Css(".Dropdown-Select__Label__Container")
        time.sleep(random.uniform(1,3))
            #하위메뉴를 클릭한다.
        element=driver.find_elements(By.CSS_SELECTOR,".Dropdown-Select__Dropdown__Item")
        print(len(element))
        randclick_elver(element[num1-1])
    except:
        print("상위메뉴가 없다.")
    
    #2번쨰 메뉴 작업코드다.
    try:
        #2번째 메뉴가 텍스트 옵션인경우 
        if existEl_check_Css(".Text-Select__Item__Border"):
            subEl=driver.find_elements(By.CSS_SELECTOR,".Text-Select__Item__Border")
            randclick_elver(subEl[num2-1])
            
        #2번째 메뉴가 이미지 옵션인경우 
        elif existEl_check_Css(".Image-Select__Item__Img__Status"):
            imageEls=driver.find_elements(By.CSS_SELECTOR,".Image-Select__Item__Img__Status")
            randclick_elver(imageEls[num2-1])
    except:
        print("서브메뉴가 없다.")

#메인메뉴가 하나인경우다.".Image-Select__Item"
def payoption(num1=int,num2=int):
    #의류 옵션이 사각박스인경우,
    if existEl_check_Css(".Dropdown-Select__Label__Container"):
        image_payopion(num1,num2)
        #선택이미지 박스만 있는 경우다.
    elif existEl_check_Css(".Image-Select__Item"):
        image_payopion(num1,num2)
        #텍스트 박스만 있는 경우다.
    elif existEl_check_Css(".Text-Select__Item__Border"):
        image_payopion(num1,num2)
    #일반적인 옵션이 경우(사각박스 선택지.)
    elif existEl_check_Css(".prod-option__selected.multiple"):
        general_payoption(num1,num2)

def making_screen_folder():
    global file_path
    file_path="//vmware-host/Shared Folders/vmware공유파일" 
    
    #실전, 테스트 환경을 구분하는 파트다.
    if os.path.exists(file_path):
        file_path="//vmware-host/Shared Folders/vmware공유파일/스크린샷폴더"
    else:    
        print("테스트환경이다.")
        file_path=filepathfix()
    
    #2폴더를 생성하는 파트다.
    if not os.path.exists(f"{file_path}"):
        os.mkdir(file_path)

    if not os.path.exists(f"{file_path}/쿠팡"):
        os.mkdir(f"{file_path}/쿠팡")

    if not os.path.exists(f"{file_path}/쿠팡/{coupang_product_name}"):
        os.mkdir(f"{file_path}/쿠팡/{coupang_product_name}")


def collect_productname():
    element=driver.find_element(By.CSS_SELECTOR,".prod-buy-header__title")
    product_name=element.text
    return product_name


#찜작업하는 함수.
def jjimwork():
    scroll_click_Css(".prod-favorite-btn")
    time.sleep(random.uniform(1,2))
    element=driver.find_element(By.CSS_SELECTOR,".prod-atf")
    element.screenshot(f"{file_path}/쿠팡/{coupang_product_name}/({pcname})찜.png")


    #구매수량,구매옵션, 찜작업을 해준다.
def Ac5_payoptions(moq=1,jjim=bool,optionmenus1=None,optionmenus2=None):
    global coupang_product_name
    coupang_product_name=collect_productname()
    making_screen_folder()
    #구입수량이 한개 이상일떄 작동한다.
    if moq > 1:
        purchase_quantity(num=moq)
    #찜 작업의 여부를 체크한다.
    if jjim:
        jjimwork()
    #옵션메뉴의 작동여부.
    if optionmenus1 != None or optionmenus2 != None:
        payoption(num1=optionmenus1,num2=optionmenus2)
    

    #결제 방식의 2가지
def showpingback():
    scroll_click_Css(".prod-cart-btn")
    time.sleep(0.5)
    #장바구니로 이동하기.
    scroll_click_Css(".prod-order-notifier-link")
    time.sleep(1)
    #두번째 창에서 구매버튼 누르기.
    scroll_click_Css(".goPayment")

#바로 구매 버튼으로 구매하기.
def directpaybtn():
    scroll_click_Css(".prod-buy-btn")

#장바구니, 바로구매 둘중하나 클릭을 한다.
def Ac6_payways(jangbaguni=bool):
    #2중 1택이다. 장바구니라면, 그것을 실행 아니면, 다른것 실행하면 된다.
    if jangbaguni:
        showpingback()
        time.sleep(3)
    else:
        directpaybtn()
        time.sleep(3)

##쿠팡 포인트사용##
def pointuse():
    scroll_click_Css(".insert-cash-toggle")
    time.sleep(1)
    #모두사용버튼 누르기
    randclick_cssver(".cashAllUsing")
    time.sleep(1)
    #캐시적용버튼 누르기.
    randclick_cssver(".apply active")

#배송메세지 입력하기.
def basongmsg(msg=str):
    #메세지 변경버튼 누르기
    switch_handle(1)
    scroll_click_Css("td>.delivery-request-message__popup-list-button")
    time.sleep(random.uniform(1,2))
    switch_handle(2)
        #선택옵션,기타버튼을 누른다.
    randclick_cssver("body > div > div > div.content-wrapper > div.content-body.content-body--fixed > div > form > div.preference-required.__AA01_OTHER_PLACE > label > span")
    time.sleep(random.uniform(1,2))
        #기존의 모든 내용을 지운다.
    element=driver.find_element(By.CSS_SELECTOR,"#__AA01_OTHER_PLACE")
    ActionChains(driver).click(element).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

        #배송메세지를 입력한다.
    element_typer("#__AA01_OTHER_PLACE",msg)

        #확인버튼 누른다.
    time.sleep(random.uniform(1,2))
    randclick_cssver(".delivery-preferences__save-button")

#결제 비번을 누른다.
def paymentpassworlds():
    psw_nums=[1,2,3,4,5]
    for psw_num in psw_nums:
        img_filepath=filepathfix()
        while True:
            try:
                exist_image=pyautogui.locateCenterOnScreen(f"{img_filepath}/C_Payment_password/{psw_num}.png")
            except:
                exist_image=pyautogui.locateCenterOnScreen("./C_Payment_password/1.png")
            if exist_image != None:
                break
        pyautogui.moveTo(exist_image)
        pyautogui.moveRel(random.randint(-20,20),random.randint(-5,5))
        pyautogui.click()
        time.sleep(random.randint(1,2))


#두번재 결제창을 누르는 함수.
def realpaymentbtns():
    switch_handle(1)
    scroll_click_Css("#paymentBtn")

#마지막 결제완료 후,스크린샷 남기는 것이다.
def lastscreenshot():
    element=driver.find_element(By.CSS_SELECTOR,".prod-atf")
    element.screenshot(f"{file_path}/쿠팡/{coupang_product_name}/({pcname})결제완료.png")
    

def Ac7_lastoption(point=bool,msg=None):
    #배송메세지 기능.
    if len(msg)>=1:
        basongmsg(msg)
    #포인트사용시
    if point:
        pointuse()

    realpaymentbtns()
    time.sleep(2)
    paymentpassworlds()

#구분을 위한 무늬 함수다.
def output():
    coupang_product_name
    #마지막에 포인트를 사용했다면 사용포인트.
    #결제가격을 크롤링해야 된다.

#잘 작동하는지 테스트가 필요하다.
def coupang_start(url,minprice=None or int,maxprice=None or int,page_view_time=120,moq=int,jjim=bool,optionmenus1=None or int,optionmenus2=None or int,jangbaguni=bool,point=bool,msg=None or str):
    try:
        coupang_url_extract(url=url)
        Ac1_insert()
        Ac2_faketime(work_page=None,work_num=2,work_time=20)
        Ac3_price_filter(minprice=minprice,maxprice=maxprice)
        Ac4_targetgo(page_view_time)
        Ac5_payoptions(moq=moq,jjim=jjim,optionmenus1=optionmenus1,optionmenus2=optionmenus2)
        Ac6_payways(jangbaguni=jangbaguni)
        Ac7_lastoption(point=point,msg=msg)
        output()
        print("가구매작업이 끝났습니다.")
    except Exception as e:
        print("문제가 발생되었습니다.")
        # print(f"오류 발생 위치: {e.__traceback__.tb_frame.f_code.co_name}")
        e.traceback.print_tb(e.__traceback__)
 
#----------------------------------------------사용방법-------------------------------------------------
if __name__ == "__main__":
    url="https://www.coupang.com/vp/products/6991549817?itemId=17113539517&vendorItemId=84287173261&q=%EA%B2%BD%EC%B6%94%EB%B2%A0%EA%B0%9C&itemsCount=36&searchId=7f07ee5bcf2d4dc88b0adc5c37ab3cbd&rank=3&isAddedCart="
    minprice=13000
    maxprice=20000
    page_view_time= 30
    moq= 2
    jjim=True
    optionmenus1=2
    optionmenus2=2
    jangbaguni=False
    point=False
    msg="그냥 잘 배송해주면 좋구요."
    coupang_start(url=url,minprice=minprice,maxprice=maxprice,page_view_time=page_view_time,moq=moq,jjim=jjim,optionmenus1=optionmenus1,optionmenus2=optionmenus2,jangbaguni=jangbaguni,point=point,msg=msg)