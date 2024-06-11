import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=400, height=600)
canvas.pack() # 윈도우에 캔버스 배치

hyunju = tkinter.PhotoImage(file="hyunju.png") # 이미지파일 로딩
canvas.create_image(200, 300, image=hyunju) # 캔버스에 이미지 그리기

root.mainloop()