# ch 5.2.1 main.py
import sys
from ui import View # ui.py의 View 클래스 추가
from ctrl import Control # ctrl.py의 Control 클래스 추가
from PyQt5.QtWidgets import QApplication

def main(): # 프로그램 실행(Application) 관련 내용 함수화
    calc = QApplication(sys.argv)
    app = QApplication(sys.argv)
    view = View() # View 클래스의 인스턴스 선언 및 생성
    Control(view=view) # Control 클래스의 인스턴스 선언 및 생성
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()