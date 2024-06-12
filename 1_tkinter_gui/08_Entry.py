# Entry 위젯을 사용하여 한줄 입력 필드 사용해보기

import tkinter

def click_btn():
    txt = entry.get() # 입력된 문구는 get 메소드 사용
    button["text"] = txt

root = tkinter.Tk()
root.title("첫 번째 테스트 입력 필드")
root.geometry("400x200")

entry = tkinter.Entry(width=20)
entry.place(x=20, y=20)

button = tkinter.Button(text="문자열 얻기", command=click_btn)
button.place(x=20, y=100)

root.mainloop()