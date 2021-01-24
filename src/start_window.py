import webbrowser
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThreadPool

from intro_window import IntroWindow
from load_image import LoadImage
from image_editor_window import ImageEditorWindow
from model import Model


class UiStartWindow(object):
    def setupUi(self, start_window):
        self.start_window = start_window
        self.start_window.setObjectName("start_window")
        self.start_window.resize(644, 677)
        self.start_window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.start_window.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(start_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 180, 351, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_menu_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_menu_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.main_menu_layout.setContentsMargins(12, 0, 12, 0)
        self.main_menu_layout.setSpacing(10)
        self.main_menu_layout.setObjectName("main_menu_layout")
        self.image_load_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.image_load_button.setIconSize(QtCore.QSize(20, 19))
        self.image_load_button.setObjectName("image_load_button")
        self.main_menu_layout.addWidget(self.image_load_button)
        self.open_description_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_description_button.setObjectName("open_description_button")
        self.main_menu_layout.addWidget(self.open_description_button)
        start_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(start_window)
        QtCore.QMetaObject.connectSlotsByName(start_window)

    def retranslateUi(self, start_window):
        _translate = QtCore.QCoreApplication.translate
        self.start_window.setWindowTitle(_translate("start_window", "MainWindow"))
        self.image_load_button.setText(_translate("start_window", "CHECK IMAGE"))
        self.open_description_button.setText(_translate("start_window", "PROJECT DESCRIPTION"))


class StartWindow(UiStartWindow):
    def __init__(self, start_window):
        self.setupUi(start_window)
        self.window = QtWidgets.QMainWindow()
        self.intro_window = IntroWindow(self.window, start_window)
        self.hide_window()
        self.threadpool = QThreadPool()
        self.model = Model()
        self.threadpool.start(self.model)
        self.model.signals.finished.connect(self.intro_window.after_model_load)
        self.image_editor_window = None

        self.image_load_button.clicked.connect(self.load_user_image)

        self.open_description_button.clicked.connect(self.show_project_description)

    def show_project_description(self):
        webbrowser.open_new("../project_description/AO_dokumentacja_projektu.pdf")

    def hide_window(self):
        self.start_window.hide()
        self.intro_window.intro_window.show()

    def load_user_image(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        imagePath, _ = QtWidgets.QFileDialog.getOpenFileName(self.start_window, "QFileDialog.getOpenFileName()", "",
                                                             "Image files (*.jpg *.png)", options=options)
        user_image = LoadImage(imagePath)
        if user_image.original_image is not None:
            self.start_window.hide()
            self.image_editor_window = ImageEditorWindow(self.window, self.start_window, user_image, self.model)
            self.image_editor_window.show()

    def start(self):
        self.intro_window.show()