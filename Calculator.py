from tkinter import *   # tkinter 인터페이스 불러오기 (tkinter는 파이썬이 기본 제공해주는 인터페이스이고, 다이얼로그를 만드는 기능)

win = Tk()               # tkinter를 window 변수에 담기
win.title("Calculator")  # 다이얼로그 타이틀 정하기


buttons = ['7', '8', '9', '+', 'C',     # buttons 변수에 리스트 형태로 버튼 배치
           '4', '5', '6', '-', ' ',
           '1', '2', '3', '*', ' ',
           '0', '.', '=', '/', ' ']

# for문을 통해 버튼을 생성
i = 0
for b in buttons:   # buttons를 순환하는 순환 변수 b
    cmd = lambda key = b: click(key) # lambda함수를 사용하여 순환 함수 b를 변수 key에 전달을 하고, key는 함수 click의 인수가 됨
    btn = Button(win, text = b, width = 5, relief = 'ridge', command = cmd) # 순환 변수 b를 text로 받고, relief는 위젯의 테두리
                                                                            # 스타일을 정하는 것으로 "ridge"는 테두리만 볼록한 것
                                                                            # 클릭했을 때 실행되는 command에는 cmd를 넣어줌

    btn.grid(row = i // 5 + 1, column = i % 5)  # 배치관리자 grid를 활용하여 가로가 5칸이기 때문에 column은 i를 5로 나눈 나머지로 해주고,
                                                # 세로도 5칸이지만 맨 첫 번째 줄은 entry로 지정을 해줄 거기 때문에 i를 5+1로 나눈 값으로 해줌
    i += 1


entry = Entry(win, justify = 'right', width = 33, bg = 'yellow')    # Entry는 한 줄의 텍스트를 사용자로부터 입력받는 필드이며, bg로 
                                                                    # 백그라운드 색상을 "yellow"로 해주고, width로 크기를 설정,
                                                                    # justify로 오른쪽 정렬

entry.grid(row = 0, column = 0, columnspan = 5) # coloumnspan은 열병합을 뜻하는 것으로 Entry 위젯이 5개의 셀을 차지하도록 설정


def click(key):
    if key == '=':  # '=' 버튼이 클릭되면 수식을 계산하여 결과를 표시
        try:
            result = eval(entry.get())      # eval은 내장함수이며, string type의 data를 계산 가능한 식으로 바꿔 계산하는 함수이며,
                                            # entry.get()을 통해 entry에 입력된 data를 가져오기
            entry.delete(0, END)            # 결과를 표시하기 전에 entry를 지우기
            entry.insert(END, str(result))  # 계산된 결과를 표시
        except:
            entry.insert(END, " ERROR")     # 계산이 되지 않는 식을 입력했을 때 " ERROR" 라는 문구가 뜨게 구현
    elif key == 'C':
        entry.delete(0, END)                # 'C' 버튼이 클릭되면 entry를 지우기
    else:
        entry.insert(END, key)              # 그 외에 다른 버튼이 클릭될 시에는 클릭된 key를 표시


win.mainloop()   # tkinter 프로그래밍할 때 윈도우 화면에서 발생하는 다양한 메세지들을 받고 처리하는 함수