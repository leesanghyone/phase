from pynput.keyboard import Key, Listener

def on_press(key):
    print(key)
    if key == Key.f12 :
        # 파이썬 코드가 실행됩니다.
        print("Hello world!")

with Listener(on_press=on_press) as listener:
    listener.join()