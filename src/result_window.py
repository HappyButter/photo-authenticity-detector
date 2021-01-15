from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_result_window(object):
    def setupUi(self, result_window):
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
        self.result_image.setPixmap(QtGui.QPixmap("../images/examples-examples.jpg"))
        self.result_image.setScaledContents(True)
        self.result_image.setObjectName("result_image")
        self.result_info_label = QtWidgets.QLabel(self.centralwidget)
        self.result_info_label.setGeometry(QtCore.QRect(320, 470, 221, 16))
        self.result_info_label.setObjectName("result_info_label")
        self.busted_clear_label = QtWidgets.QLabel(self.centralwidget)
        self.busted_clear_label.setGeometry(QtCore.QRect(170, 20, 481, 61))
        self.busted_clear_label.setObjectName("busted_clear_label")
        result_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(result_window)
        QtCore.QMetaObject.connectSlotsByName(result_window)

    def retranslateUi(self, result_window):
        _translate = QtCore.QCoreApplication.translate
        result_window.setWindowTitle(_translate("result_window", "MainWindow"))
        self.modify_image_button.setText(_translate("result_window", "Modify again"))
        self.to_menu_button.setText(_translate("result_window", "menu"))
        self.result_info_label.setText(_translate("result_window", "Tekst o procentach"))
        self.busted_clear_label.setText(_translate("result_window", "No tutaj busted/clear jesli wyjdzie nam zaznaczanie gdzie jest fake"))

