'''
마우스의 이동과 클릭 시 
해당 이벤트를 처리하는 과정을 알아본다
'''

import tkinter

root = tkinter.Tk()
root.title("마우스 입력")
root.resizable(False, False)


mouse_x = 0
mouse_y = 0
mouse_c = 0 # 포인터 클릭 여부

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y
root.bind("<Motion>", mouse_move)

def mouse_press(e):
    global mouse_c
    mouse_c = 1
root.bind("<ButtonPress>", mouse_press)

def mouse_release(e):
    global mouse_c
    mouse_c = 0
root.bind("<ButtonRelease>", mouse_release)


def game_main():
    fnt = ("Times New Roman", 30)
    txt = "mouse({},{}){}".format(mouse_x, mouse_y, mouse_c)
    canvas.delete("TEST") # 기존 문자열 삭제
    canvas.create_text(456, 384, text=txt, fill="black", font=fnt, tag="TEST")
    root.after(100, game_main)


canvas = tkinter.Canvas(root, width=912, height=768)
canvas.pack()

game_main()
root.mainloop()