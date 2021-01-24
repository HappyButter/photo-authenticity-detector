from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_result_window(object):
    def setupUi(self, result_window):
        self.result_window = result_window
        result_window.setObjectName("result_window")
        result_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(result_window)
        self.centralwidget.setObjectName("centralwidget")
        self.modify_image_button = QtWidgets.QPushButton(self.centralwidget)
        self.modify_image_button.setGeometry(QtCore.QRect(30, 530, 93, 28))
        self.modify_image_button.setObjectName("modify_image_button")
        self.to_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.to_menu_button.setGeometry(QtCore.QRect(670, 530, 93, 28))
        self.to_menu_button.setObjectName("to_menu_button")
        self.result_image = QtWidgets.QLabel(self.centralwidget)
        self.result_image.setGeometry(QtCore.QRect(210, 110, 401, 341))
        self.result_image.setText("")

        self.result_image.setScaledContents(True)
        self.result_image.setObjectName("result_image")
        self.result_info_label = QtWidgets.QLabel(self.centralwidget)
        self.result_info_label.setGeometry(QtCore.QRect(320, 470, 221, 16))
        self.result_info_label.setObjectName("result_info_label")
        result_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(result_window)
        QtCore.QMetaObject.connectSlotsByName(result_window)

    def retranslateUi(self, result_window):
        _translate = QtCore.QCoreApplication.translate
        result_window.setWindowTitle(_translate("result_window", "MainWindow"))
        self.modify_image_button.setText(_translate("result_window", "Modify again"))
        self.to_menu_button.setText(_translate("result_window", "menu"))
        self.result_info_label.setText(_translate("result_window", "Tekst o procentach"))


class ResultWindow(Ui_result_window):
    def __init__(self, start_window, image_editor_window):

        self.start_window = start_window
        self.image_editor_window = image_editor_window

        self.window_2 = QtWidgets.QMainWindow()
        self.setupUi(self.window_2)

        self.modify_image_button.clicked.connect(self.modify_image_btn_action)
        self.to_menu_button.clicked.connect(self.to_menu_btn_action)

    def set_fake_rate(self, fake_rate):
        _translate = QtCore.QCoreApplication.translate
        if fake_rate[1] > fake_rate[0]:
            self.result_image.setPixmap(QtGui.QPixmap("../images/OK.png"))
            info = "Your picture is real in: {:2.5f}% ".format(fake_rate[1] * 100)
        else:
            self.result_image.setPixmap(QtGui.QPixmap("../images/busted.png"))
            info = "Your picture is fake in: {:2.5f}%".format(fake_rate[0] * 100)

        self.result_info_label.setText(_translate("result_window", info))

    def modify_image_btn_action(self):
        self.result_window.close()
        self.image_editor_window.show()

    def to_menu_btn_action(self):
        self.result_window.close()
        self.start_window.show()

    def show(self):
        self.result_window.show()
