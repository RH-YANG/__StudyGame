# Text 위젯을 사용해서 여러줄 입력 필드를 사용해보기

import tkinter

def click_btn():
    text.insert(tkinter.END, "몬스터가 나타났다!")

root = tkinter.Tk()
root.title("여러 행 텍스트 입력")
root.geometry("400x200")

button = tkinter.Button(text="메시지", command=click_btn)
button.pack()

text = tkinter.Text()
text.pack()

root.mainloop()