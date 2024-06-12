"""
실시간 키 입력 어플
>> bind 메소드를 사용해서 키보드 이벤트를 다룬다
"""
import tkinter

key = ''

def key_down(e): # bind 메소드에 의해 호출되며 이벤트를 매개변수로 받는다
    global key
    # key = e.keycode >> 윈도우와 맥의 코드값이 달라서 호환이 불가능해진다
    key = e.keysym # 키의 이름은 윈도우와 맥이 공통이다

def main_proc(): # 일정시간마다 key에 저장된 값을 label에 입력한다
    label["text"] = key
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("실시간 키입력")
root.bind("<KeyPress>", key_down)

label = tkinter.Label(font=("Times New Roman", 80))
label.pack()

main_proc()
root.mainloop()