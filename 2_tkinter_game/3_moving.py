import tkinter

key = ""

def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ""

cx = 400
cy = 300

def main_proc():
    global cx, cy
    if key == "Up":
        cy = cy - 20
    if key == "Down":
        cy = cy + 20
    if key == "Left":
        cx = cx - 20
    if key == "Right":
        cx = cx + 20
    # canvas.coords("MYCHR", cx, cy) # 태그명을 사용한경우
    canvas.coords(img_id, cx, cy) # 아이디를 사용한경우
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("캐릭터 이동")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

canvas = tkinter.Canvas(width=800, height=600, bg="lightgreen")
canvas.pack()
img = tkinter.PhotoImage(file="mimi.png")
# canvas.create_image(cx, cy, image=img, tag="MYCHR") # 태그를 사용해서 이미지에 특정할 수 있는 이름을 붙인다
img_id = canvas.create_image(cx, cy, image=img) # 혹은 반환되는 아이디를 사용할 수 있음

main_proc()
root.mainloop()