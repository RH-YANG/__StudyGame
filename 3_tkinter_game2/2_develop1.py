'''
격자 배경에 마우스를 올렸을 때,
해당되는 칸에 커서가 나타나도록 하는 로직을 구성한다
'''
import tkinter

root = tkinter.Tk()
root.title("커서 표시")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()
bg = tkinter.PhotoImage(file="./source/neko_bg.png")
cvs.create_image(456, 384, image=bg)


# 마우스의 위치별 커서의 위치 지정하기
cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y
root.bind("<Motion>", mouse_move)

cursor = tkinter.PhotoImage(file="./source/neko_cursor.png")
def game_main():
    global cursor_x, cursor_y
    if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
        cursor_x = int((mouse_x - 24) / 72)
        cursor_y = int((mouse_y - 24) / 72)
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR") # 60은 여백 24와 한칸의 크기 72의 중점인 36을 더해서 나온 숫자
    root.after(100, game_main)


game_main()
root.mainloop()