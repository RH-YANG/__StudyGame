"""
매 초마다 숫자를 카운팅해서 보여주는 어플리케이션
>> after 메소드와 재귀호출을 사용해서 
   실시간 처리 구현한다
"""
import tkinter

tmr = 0

def count_up():
    global tmr # 전역변수를 호출할것이므로 global 키워드 사용
    tmr = tmr + 1
    label["text"] = tmr
    root.after(1000, count_up) # 재귀호출

root = tkinter.Tk()

label = tkinter.Label(font=("Times New Roman", 80))
label.pack()

root.after(1000, count_up) # 그냥 count_up()으로 호출하면 윈도우가 표시되기 전에 호출됨

root.mainloop()