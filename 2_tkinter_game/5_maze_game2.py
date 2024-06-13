'''
4_maze_game.py에 덧붙여서
이동한 칸은 핑크색으로 만들기
왼쪽Shift키를 누르면 처음부터 다시 시작하기
모든 바닥을 핑크색으로 칠하면 클리어 창 표시하기
기능을 추가한다.
'''

import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("바닥을 칠한다냥")

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
pink = 0
def main_proc():
    global mx, my, pink
    if key == "Shift_L" and pink > 1: #다시시작하기를 선택한 경우
        canvas.delete("PAINT")
        mx = 1
        my = 1
        pink = 0
        for y in range(7):
            for x in range(10):
                if maze[y][x] == 2:
                    maze[y][x] = 0
    if key == "Up" and maze[my - 1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my + 1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx - 1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx + 1] == 0:
        mx = mx + 1
    if maze[my][mx] == 0:
        maze[my][mx] = 2
        pink = pink + 1
        canvas.create_rectangle(mx * 80, my * 80, mx * 80 + 79, my * 80 + 79, fill="pink", width=0, tag="PAINT")
    canvas.delete("MYCHR") # 붉은색으로 색칠이 되었기 때문에 지우고 다시 그려야한다
    canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="MYCHR")
    if pink == 30: # 게임을 클리어한경우
        canvas.update()
        tkinter.messagebox.showinfo("축하합니다！", "모든 바닥을 칠했습니다！")
    else:
        root.after(300, main_proc)


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