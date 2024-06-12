# Checkbutton과 BooleanVar를 사용해서 체크상태 확인하기

import tkinter

def check():
    if val.get() == True: # get 메소드를 사용해서 상태 확인
        print("체크되어 있습니다")
    else:
        print("체크되어 있지 않습니다")

root = tkinter.Tk()
root.title("체크 상태 확인")
root.geometry("400x200")

val = tkinter.BooleanVar()
val.set(False)

cbtn = tkinter.Checkbutton(text="체크 버튼", variable=val, command=check)
cbtn.pack()

root.mainloop()