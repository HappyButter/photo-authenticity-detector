from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QFont
from custom_elements import CustomLabel
import numpy as np


class UiIntroWindow(object):
    def setupUi(self, intro_window):
        self.intr_window = intro_window
        intro_window.setObjectName("intro_window")
        intro_window.resize(629, 619)
        self.centralwidget = QtWidgets.QWidget(intro_window)
        self.centralwidget.setObjectName("centralwidget")
        self.intro_image_label = QtWidgets.QLabel(self.centralwidget)
        self.intro_image_label.setGeometry(QtCore.QRect(0, 0, 629, 619))
        self.intro_image_label.setText("")
        self.intro_image_label.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.intro_image_label.setObjectName("intro_image_label")
        self.info_text_label = CustomLabel(self.centralwidget)
        self.info_text_label.setGeometry(QtCore.QRect(160, 520, 271, 41))
        self.info_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_text_label.setObjectName("info_text_label")
        self.go_further = QtWidgets.QPushButton(self.centralwidget)
        self.go_further.setGeometry(QtCore.QRect(0, -5, 629, 619))
        self.go_further.setText("")
        self.go_further.setFlat(True)
        self.go_further.setObjectName("go_further")
        intro_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(intro_window)
        QtCore.QMetaObject.connectSlotsByName(intro_window)

    def retranslateUi(self, intro_window):
        _translate = QtCore.QCoreApplication.translate
        intro_window.setWindowTitle(_translate("intro_window", "MainWindow"))
        self.info_text_label.setText(_translate("intro_window", "Click to continue"))
        self.info_text_label.setFont(QFont('Arial', 1))


class IntroWindow(UiIntroWindow):
    def __init__(self, window, start_window):
        self.start_window = start_window
        self.setupUi(window)
        self.transform_text()
        self.go_further.clicked.connect(self.close_window)

    def close_window(self):
        self.intr_window.close()
        self.start_window.show()

    def transform_text(self):
        self.anim = QPropertyAnimation(self.info_text_label, b"font")
        self.anim.setDuration(8000)
        self.anim.setStartValue(5)
        time_frames = np.linspace(0, 1, num=20)
        font_sizes = [i for i in range(5, 15)] + [i for i in range(15, 5, -1)]
        for time_frame, font_size in zip(time_frames, font_sizes):
            self.anim.setKeyValueAt(time_frame, font_size)
        self.anim.setEndValue(5)
        self.anim.setLoopCount(-1)
        self.anim.start()
