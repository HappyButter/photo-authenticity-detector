import sys
from start_window import StartWindow, QtWidgets


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    start_window = StartWindow(window)
    sys.exit(app.exec_())
