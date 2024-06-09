# 시스템에서 사용가능한 폰트 확인해보기

import tkinter
import tkinter.font # 서브모듈을 가져와야지만 사용할 수 있음

root = tkinter.Tk()

print(tkinter.font.families()) # 사용가능한 폰트 확인