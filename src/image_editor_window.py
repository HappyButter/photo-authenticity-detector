from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
import cv2
import numpy as np
from result_window import ResultWindow

class Ui_image_editor_window(object):
    def setupUi(self, image_editor_window):
        self.image_editor_window = image_editor_window
        image_editor_window.setObjectName("image_editor_window")
        image_editor_window.resize(1113, 605)
        self.centralwidget = QtWidgets.QWidget(image_editor_window)
        self.centralwidget.setObjectName("centralwidget")
        self.original_image_label = QtWidgets.QLabel(self.centralwidget)
        self.original_image_label.setGeometry(QtCore.QRect(110, 30, 381, 321))
        self.original_image_label.setText("")
        self.original_image_label.setPixmap(QtGui.QPixmap("../images/examples-examples.jpg"))
        self.original_image_label.setScaledContents(True)
        self.original_image_label.setObjectName("original_image_label")
        self.changed_imag_label = QtWidgets.QLabel(self.centralwidget)
        self.changed_imag_label.setGeometry(QtCore.QRect(670, 30, 381, 321))
        self.changed_imag_label.setText("")
        self.changed_imag_label.setPixmap(QtGui.QPixmap("../images/examples-examples.jpg"))
        self.changed_imag_label.setScaledContents(True)
        self.changed_imag_label.setObjectName("changed_imag_label")
        self.checker_button = QtWidgets.QPushButton(self.centralwidget)
        self.checker_button.setGeometry(QtCore.QRect(980, 520, 121, 41))
        self.checker_button.setObjectName("checker_button")
        self.RGB_check_box = QtWidgets.QGroupBox(self.centralwidget)
        self.RGB_check_box.setGeometry(QtCore.QRect(770, 400, 105, 114))
        self.RGB_check_box.setObjectName("RGB_check_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.RGB_check_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.r_canal_check_box = QtWidgets.QCheckBox(self.RGB_check_box)
        self.r_canal_check_box.setObjectName("r_canal_check_box")
        self.verticalLayout.addWidget(self.r_canal_check_box)
        self.green_color__check_box_2 = QtWidgets.QCheckBox(self.RGB_check_box)
        self.green_color__check_box_2.setObjectName("green_color__check_box_2")
        self.verticalLayout.addWidget(self.green_color__check_box_2)
        self.blue_color_check_box = QtWidgets.QCheckBox(self.RGB_check_box)
        self.blue_color_check_box.setObjectName("blue_color_check_box")
        self.verticalLayout.addWidget(self.blue_color_check_box)
        self.convert_to_gray_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.convert_to_gray_check_box.setGeometry(QtCore.QRect(760, 550, 151, 20))
        self.convert_to_gray_check_box.setObjectName("convert_to_gray_check_box")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 380, 441, 197))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.contrast_label = QtWidgets.QLabel(self.layoutWidget)
        self.contrast_label.setObjectName("contrast_label")
        self.gridLayout.addWidget(self.contrast_label, 0, 0, 1, 1)
        self.contrast_slider = QtWidgets.QSlider(self.layoutWidget)
        self.contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider.setObjectName("contrast_slider")
        self.contrast_slider.setMaximum(300)
        self.contrast_slider.setMinimum(100)
        self.contrast_slider.setSingleStep(10)
        self.contrast_slider.setValue(100)
        self.gridLayout.addWidget(self.contrast_slider, 1, 0, 1, 1)
        self.gamma_slider = QtWidgets.QSlider(self.layoutWidget)
        self.gamma_slider.setOrientation(QtCore.Qt.Horizontal)
        self.gamma_slider.setObjectName("gamma_slider")
        self.gamma_slider.setMaximum(200)
        self.gamma_slider.setMinimum(1)
        self.gamma_slider.setSingleStep(10)
        self.gamma_slider.setValue(100)
        self.gridLayout.addWidget(self.gamma_slider, 1, 1, 1, 1)
        self.gaussian_label = QtWidgets.QLabel(self.layoutWidget)
        self.gaussian_label.setObjectName("gaussian_label")
        self.gridLayout.addWidget(self.gaussian_label, 2, 0, 1, 1)
        self.gaussian_slider = QtWidgets.QSlider(self.layoutWidget)
        self.gaussian_slider.setOrientation(QtCore.Qt.Horizontal)
        self.gaussian_slider.setObjectName("gaussian_slider")
        self.gaussian_slider.setMaximum(10)
        self.gaussian_slider.setMinimum(0)
        self.gaussian_slider.setValue(1)
        self.gridLayout.addWidget(self.gaussian_slider, 3, 0, 1, 1)
        self.gamma_label = QtWidgets.QLabel(self.layoutWidget)
        self.gamma_label.setObjectName("gamma_label")
        self.gridLayout.addWidget(self.gamma_label, 0, 1, 1, 1)
        image_editor_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(image_editor_window)
        QtCore.QMetaObject.connectSlotsByName(image_editor_window)

    def retranslateUi(self, image_editor_window):
        _translate = QtCore.QCoreApplication.translate
        image_editor_window.setWindowTitle(_translate("image_editor_window", "MainWindow"))
        self.checker_button.setText(_translate("image_editor_window", "Check"))
        self.RGB_check_box.setTitle(_translate("image_editor_window", "filter RGB"))
        self.r_canal_check_box.setText(_translate("image_editor_window", "R"))
        self.green_color__check_box_2.setText(_translate("image_editor_window", "G"))
        self.blue_color_check_box.setText(_translate("image_editor_window", "B"))
        self.convert_to_gray_check_box.setText(_translate("image_editor_window", " Convert to gray scale"))
        self.contrast_label.setText(_translate("image_editor_window", "contrast"))
        self.gaussian_label.setText(_translate("image_editor_window", "gaussian blur"))
        self.gamma_label.setText(_translate("image_editor_window", "gamma"))


class ImageEditorWindow(Ui_image_editor_window):
    def __init__(self, window, start_window, user_image, model):
        self.result_window = None
        self.model = model
        self.start_window = start_window
        self.setupUi(window)
        self.window = window
        self.user_image = user_image
        original_image = user_image.resizeWithAspectRatio(user_image.original_image, width=381, height=321)

        (h, w) = original_image.shape[:2]

        self.original_image_label.setGeometry(QtCore.QRect(110, 30, w, h))
        self.changed_imag_label.setGeometry(QtCore.QRect(670, 30, w, h))

        bytesPerLine = 3 * w
        qImg = QImage(original_image.data, w, h, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        self.original_image_label.setPixmap(QtGui.QPixmap(qImg))

        manipulated_image = self.user_image.resizeWithAspectRatio(self.user_image.modified_image, width=381, height=321)
        qImg = QImage(manipulated_image.data, w, h, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        self.changed_imag_label.setPixmap(QtGui.QPixmap(qImg))

        self.checker_button.clicked.connect(self.check_action)
        self.convert_to_gray_check_box.stateChanged.connect(self.updateManipulatedImage)
        self.r_canal_check_box.stateChanged.connect(self.updateManipulatedImage)
        self.green_color__check_box_2.stateChanged.connect(self.updateManipulatedImage)
        self.blue_color_check_box.stateChanged.connect(self.updateManipulatedImage)
        self.contrast_slider.valueChanged.connect(self.updateManipulatedImage)
        self.gamma_slider.valueChanged.connect(self.updateManipulatedImage)
        self.gaussian_slider.valueChanged.connect(self.updateManipulatedImage)


    def show(self):
        self.image_editor_window.show()


    def updateManipulatedImage(self):
        manipulated_image = self.user_image.resizeWithAspectRatio(self.user_image.modified_image, width=381, height=321)
        if self.r_canal_check_box.isChecked():
            self.filterRed(manipulated_image)
        if self.green_color__check_box_2.isChecked():
            self.filterGreen(manipulated_image)
        if self.blue_color_check_box.isChecked():
            self.filterBlue(manipulated_image)
        manipulated_image = self.contrastControl(manipulated_image)
        manipulated_image = self.gammaControl(manipulated_image)
        manipulated_image = self.gaussianBlurControl(manipulated_image)

        if self.convert_to_gray_check_box.isChecked():
            manipulated_image = self.toGrayScale(manipulated_image)

        height, width, channel = manipulated_image.shape
        bytesPerLine = 3 * width
        qImg = QImage(manipulated_image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        self.changed_imag_label.setPixmap(QtGui.QPixmap(qImg))

    def manipulate_image(self):
        manipulated_image = self.user_image.modified_image.copy()
        if self.r_canal_check_box.isChecked():
            self.filterRed(manipulated_image)
        if self.green_color__check_box_2.isChecked():
            self.filterGreen(manipulated_image)
        if self.blue_color_check_box.isChecked():
            self.filterBlue(manipulated_image)
        manipulated_image = self.contrastControl(manipulated_image)
        manipulated_image = self.gammaControl(manipulated_image)
        manipulated_image = self.gaussianBlurControl(manipulated_image)

        if self.convert_to_gray_check_box.isChecked():
            manipulated_image = self.toGrayScale(manipulated_image)

        return manipulated_image

    def calculate_fake_rate(self):
        img = self.manipulate_image()
        img = img.astype('float64')
        img = img / 255.0
        height, width, channel = img.shape
        img = img.reshape(-1, width, height, 3)

        fake_rate = self.model.predict(img)
        return fake_rate

    def toGrayScale(self, manipulated_image):
        gray = cv2.cvtColor(manipulated_image, cv2.COLOR_BGR2GRAY)
        gray_three = cv2.merge([gray, gray, gray])
        return gray_three

    def filterRed(self, manipulated_image):
        manipulated_image[:, :, 2] = 0

    def filterGreen(self, manipulated_image):
        manipulated_image[:, :, 1] = 0

    def filterBlue(self, manipulated_image):
        manipulated_image[:, :, 0] = 0

    def contrastControl(self, manipulated_image):
        alpha = self.contrast_slider.value() / 100.
        new_image = cv2.convertScaleAbs(manipulated_image, alpha=alpha)
        return new_image

    def gammaControl(self, manipulated_image):
        gamma = self.gamma_slider.value() / 100.
        lookUpTable = np.empty((1, 256), np.uint8)
        for i in range(256):
            lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
        return cv2.LUT(manipulated_image, lookUpTable)

    def gaussianBlurControl(self, manipulated_image):
        blur = self.gaussian_slider.value() * 2 + 1
        if blur == 1:
            return manipulated_image
        return cv2.GaussianBlur(manipulated_image, (blur, blur), 0)


    def check_action(self):
        fake_rate = self.calculate_fake_rate()
        self.image_editor_window.hide()
        self.result_window = ResultWindow(self.start_window, self.image_editor_window)
        self.result_window.set_fake_rate(fake_rate[0])
        self.result_window.show()
