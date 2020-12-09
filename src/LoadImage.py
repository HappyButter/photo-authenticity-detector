import numpy as np
import cv2

class LoadImage:
    def __init__(self, image_path):
        self.original_image = cv2.imread(image_path)
        self.modified_image = cv2.imread(image_path)

    def show(self):
        cv2.imshow("image", self.original_image)
        cv2.waitKey(0)