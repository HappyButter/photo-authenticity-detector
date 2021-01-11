import numpy as np
import cv2


class LoadImage:
    def __init__(self, image_path):
        self.original_image = cv2.imread(image_path)
        self.modified_image = cv2.imread(image_path)

    def resizeWithAspectRatio(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        dim = None
        (h, w) = image.shape[:2]

        if width is None and height is None:
            return image
        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)
        else:
            r = width / float(w)
            dim = (width, int(h * r))

        return cv2.resize(image, dim, interpolation=inter)

    def show(self):
        resize = self.resizeWithAspectRatio(self.original_image, width=644)
        cv2.imshow("image", resize)
        cv2.waitKey(0)
