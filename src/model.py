import sys
import traceback
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from tensorflow.keras import models


class ModelSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    """
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)


class Model(QRunnable):
    trained_model = None

    def __init__(self):
        super(Model, self).__init__()

        self.signals = ModelSignals()

    def predict(self, img):
        return self.trained_model.predict(img)

    @pyqtSlot()
    def run(self):

        """
        Your code goes in this function
        """

        try:
            self.trained_model = models.load_model("../model/model_trained_animals_batch_16_imagenet.hdf5")
        except:
            # traceback.print_exc()
            self.trained_model = None
            # exctype, value = sys.exc_info()[:2]
            # self.signals.error.emit((exctype, value, traceback.format_exc()))
        finally:
            self.signals.finished.emit()  # Done
