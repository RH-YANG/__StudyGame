'''
격자별로 어떤 고양이가 위치하는지
리스트로 관리하는 로직을 알아본다.
'''

import tkinter

root = tkinter.Tk()
root.title("2차원 리스트로 위치 관리")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()
bg = tkinter.PhotoImage(file="./source/neko_bg.png")
cvs.create_image(456, 384, image=bg)


# 숫자별 고양이의 이미지
img_neko = [
    None, 
    tkinter.PhotoImage(file="./source/neko1.png"),
    tkinter.PhotoImage(file="./source/neko2.png"),
    tkinter.PhotoImage(file="./source/neko3.png"),
    tkinter.PhotoImage(file="./source/neko4.png"),
    tkinter.PhotoImage(file="./source/neko5.png"),
    tkinter.PhotoImage(file="./source/neko6.png"),
    tkinter.PhotoImage(file="./source/neko_niku.png")
]

# 격자별 고양이의 위치 그리기
neko = [
    [1, 0, 0, 0, 0, 0, 7, 7],
    [0, 2, 0, 0, 0, 0, 7, 7],
    [0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 3, 4, 5, 6]
]
def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]])
                

draw_neko()
root.mainloop()