# ch 6.6.1 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox, QPlainTextEdit, QHBoxLayout, 
                             QLineEdit, QComboBox, QLabel) # QLIneEdit, QComboBox 추
from PyQt5.QtGui import QIcon, QFont # QFont 추가
from PyQt5 import QtCore # 모듈 추가

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1=QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.lbl1=QLabel('v2.3.0', self) # 버전 정보 표시를 위한 lbl1 위젯 생성
        self.lbl1.setFont(QFont('Consolas', 10)) # 폰트 설정 추가, Consolas, 사이즈 10
        self.btn1 = QPushButton('Calc', self) # 버튼1 이름을 'Calc'로 변경
        self.btn2=QPushButton('Clear', self)

        self.le1=QLineEdit('0', self) # 라인 에디트1 추가
        self.le1.setAlignment(QtCore.Qt.AlignRight) # 라인 에디트1 문자열 배치 설정 (오른쪽 정렬)
        self.le1.setFocus(True) # 라인 에디트1에 포커스 설정
        self.le1.selectAll() # 텍스트 전체 선택 

        self.le2=QLineEdit('0', self) # 라인 에디트2 추가
        self.le2.setAlignment(QtCore.Qt.AlignRight) # 라인 에디트2 문자열 배치 설정 (오른쪽 정렬)

        self.cb=QComboBox(self) # 콤보 박스 추가
        self.cb.addItems(['+', '-', '*', '/']) # 콤보 박스 항목 추가(연산자로 사용), 거듭제곱 연산자 추가

        hbox_formular=QHBoxLayout() # 새로 정의한 위젯을 QHBoxLayout에 배치
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        hbox=QHBoxLayout()
        hbox.addWidget(self.lbl1) # 버전 정보 표시를 위한 lbl1 위젯 생성
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular) # hbox_formular 추가 배치
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('Calc.png'))
        self.resize(256,256)
        self.show()

    def setDisplay(self, text): # 메서드 이름 변경
        self.te1.appendPlainText(text)

    def clearMessage(self):
        self.te1.clear()
        