'''
실시간처리, 키입력, 2차원 리스트를 사용한 미로 요소들을 사용해서
미로를 이동하는 캐릭터 게임을 만든다.
'''

import tkinter

root = tkinter.Tk()
root.title("미로 안 이동하기")


# 입력된 키를 처리하는 로직
key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)


# 일정시간마다 캐릭터의 위치를 재조정하는 로직
mx = 1
my = 1
def main_proc():
    global mx, my
    if key == "Up" and maze[my - 1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my + 1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx - 1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx + 1] == 0:
        mx = mx + 1
    canvas.coords("MYCHR", mx * 80 + 40, my * 80 + 40)
    root.after(300, main_proc) # 실시간 처리 부분


# 미로 그리기
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 79, y * 80 + 79, fill="skyblue", width=0)


# 캐릭터 그리기
img = tkinter.PhotoImage(file="mimi2.png")
canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="MYCHR")


main_proc()
root.mainloop()