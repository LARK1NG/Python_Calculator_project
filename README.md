# 파이썬 tkinter로 간단한 GUI 계산기 만들기

![image description](https://im5.ezgif.com/tmp/ezgif-5-2a5e6dc1e3.webp)

**[블로그 보기 click](https://ehyssng.tistory.com/170)**

안녕하세요. 이번에는 **파이썬 tkinter를 이용하여 간단한 GUI 계산기**를 만들어보았습니다.

</br>

tkinter는 파이썬에서 **기본으로 제공되는 인터페이스**로 **다이얼로그**를 만들어주는 인터페이스입니다.

</br>


``` python
from tkinter import *   # tkinter 인터페이스 불러오기 (tkinter는 파이썬이 기본 제공해주는 인터페이스이고, 다이얼로그를 만드는 기능) 
win = Tk()               # tkinter를 window 변수에 담기
win.title("Calculator")  # 다이얼로그 타이틀 정하기
```
**`from tkinter import *`** 로 먼저 tkinter 인터페이스를 불러오고, `TK()`함수를 win 변수에 담아주고 `win.title`을 이용하여 계산기의 영어인 "Calculator"로 타이틀을 정해주었습니다.

</br>

``` python
buttons = ['7', '8', '9', '+', 'C',  
           '4', '5', '6', '-', ' ',
           '1', '2', '3', '*', ' ',
           '0', '.', '=', '/', ' ']
# buttons 변수에 리스트 형태로 버튼 배치

# for문을 통해 버튼을 생성
i = 0
for b in buttons:   # buttons를 순환하는 순환 변수 b
    cmd = lambda key = b: click(key) 
# lambda함수를 사용하여 순환 함수 b를 변수 key에 전달을 하고, key는 함수 click의 인수가 됨
    btn = Button(win, text = b, width = 5, relief = 'ridge', command = cmd) 
# 순환 변수 b를 text로 받고, relief는 위젯의 테두리
# 스타일을 정하는 것으로 "ridge"는 테두리만 볼록한 것
# 클릭했을 때 실행되는 command에는 cmd를 넣어줌

    btn.grid(row = i // 5 + 1, column = i % 5)  
# 배치관리자 grid를 활용하여 가로가 5칸이기 때문에 column은 i를 5로 나눈 나머지로 해주고,
# 세로도 5칸이지만 맨 첫 번째 줄은 entry로 지정을 해줄 거기 때문에 i를 5+1로 나눈 값으로 해줌
    i += 1
```

그리고 `buttons`라는 변수에 리스트 형태로 계산기 버튼들을 **배치**해줍니다. 그리고 for 반복문을 통해 `buttons` 변수를 순환하는 **순환 변수 b**를 만들어주고,  **`btn`** 라는 변수를 만들어 순환 변수 b를 `text`로 받고, `relief`를 통해 버튼이 `"ridge"` 테두리만 볼록하게 해줍니다. 그리고 `width`를 이용해 크기도 정해주고 클릭했을 때 실행되는 `command`에 **cmd**를 넣어주었습니다.

cmd는 **lambda함수**를 이용하여 순환 함수 b를 변수 **`key`** 에 전달하고, `key`는 `click()` 함수의 인수가 되도록 해주었습니다. 

그리고 변수 `btn`은 배치관리자 `gird`를 활용하여 가로가 5칸으로 만들 예정이기 때문에 `column`은 **i % 5**로 주었고, 세로는 4칸이지만 첫 번째 줄은 클릭된 버튼 값을 받을 `entry`로 사용할 거기 때문에 `row`는 **i // 5 + 1**로 해주었습니다.

</br>

``` python
entry = Entry(win, justify = 'right', width = 33, bg = 'yellow')    
# Entry는 한 줄의 텍스트를 사용자로부터 입력받는 필드이며, bg로
# 백그라운드 색상을 "yellow"로 해주고, width로 크기를 설정,
# justify로 오른쪽 정렬

entry.grid(row = 0, column = 0, columnspan = 5) 
# coloumnspan은 열병합을 뜻하는 것으로 Entry 위젯이 5개의 셀을 차지하도록 설정
```

그리고 **클릭된 버튼들을 입력 받아 표시**해줄 `Entry`는 `entry`라는 변수에 우선 담아주고, `justify`를 통해 오른쪽 정렬을 해주고, `width`로 크기도 정해주고, `bg`를 통해 백그라운드 컬러를 `'yellow'`로 해주었습니다.

그리고 `entry.grid`를 이용하여 `entry`는 첫 번째 줄에 가로로 5셀을 사용하여야하기 때문에 `row`와 `coloumn`을 둘 다 0으로 주고, **열병합을 뜻**하는 `coloumnspan`을 5로 주어 가로 5개의 셀을 차지하도록 설정해주었습니다.

</br>

``` python
def click(key):
 if key == '=':  # '=' 버튼이 클릭되면 수식을 계산하여 결과를 표시
        try:
            result = eval(entry.get())      
# eval은 내장함수이며, string type의 data를 계산 가능한 식으로 바꿔 계산하는 함수이며,
# entry.get()을 통해 entry에 입력된 data를 가져오기
            entry.delete(0, END)            # 결과를 표시하기 전에 entry를 지우기
            entry.insert(END, str(result))  # 계산된 결과를 표시
        except:
            entry.insert(END, " ERROR")     # 계산이 되지 않는 식을 입력했을 때 " ERROR" 라는 문구가 뜨게 구현
    elif key == 'C':
        entry.delete(0, END)                # 'C' 버튼이 클릭되면 entry를 지우기
    else:
        entry.insert(END, key)              # 그 외에 다른 버튼이 클릭될 시에는 클릭된 key를 표시
```

그리고 `def`로 `click`이라는 함수를 만들어주어 위에 `순환 함수 b`를 받는 `key`를 넣어주어서 `key`를 받게 해줍니다. 그리고 조건문을 활용하여 **각 `key`마다 실행해야 일들을 설정**해주었는데요.

우선 if를 활용해 '=' 버튼은 `eval`라는 **string type의 data를 계산 가능한 식으로 바꿔 계산하는 함수**를 사용하여 `entry`의 data를 `entry.get()`으로 받아 `result` 변수에 넣어줍니다.
그리고 결과를 표시하기 전에 `entry`창을 초기화 해주기 위해 `entry.delete(0, END)`를 사용하였고, 계산된 결과를 표시해주기 위해 `entry.insert(END, str(result))`를 사용해주었습니다.

그리고 `except`로 **예외 처리**를 해주었는데요. 계산이 되지 않는 식이 입력되었을 땐 **' ERROR'** 라는 문구가 뜨도록 `entry.insert(END, " ERROR")`를 넣어주었습니다.

그리고 다음에는 `elif`를 통해 `entry`를 초기화 해주는 버튼인 **'C'** 를 `entry.delete(0, END)`로 해주었습니다.

그리고 그 외의 버튼들은 클릭되면 표시가 되도록 `else`를 통해 `entry.insert(END, key)`를 해주었습니다.

</br>

``` python
win.mainloop()   # tkinter 프로그래밍할 때 윈도우 화면에서 발생하는 다양한 메세지들을 받고 처리하는 함수
```

마지막으로 `tkinter` **프로그래밍을 할 때 윈도우 화면에서 발생하는 다양한 메세지들을 받고 처리할 수 있는 함수**인 `win.mainloop()`를 해줌으로써 이번에 **파이썬을 활용한 간단한 계산기 만들기 프로젝트를 완료**했습니다.

읽어주셔서 감사합니다.