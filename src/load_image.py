import numpy as np
import cv2


class LoadImage:
    def __init__(self, image_path):
        self.img_path = image_path
        self.original_image = cv2.imread(image_path)
        self.modified_image = cv2.imread(image_path)


    def resizeWithAspectRatio(self, image, width, height, inter=cv2.INTER_AREA):
        dim = None
        (h, w) = image.shape[:2]

        if width is None or height is None:
            return image

        r = height / float(h)
        dim = (int(w * r), height)

        if(dim[0] > width):
            r = width / float(w)
            dim = (width, int(h * r))

        return cv2.resize(image, dim, interpolation=inter)

    def show(self):
        resize = self.resizeWithAspectRatio(self.original_image, width=381, height=321)
        cv2.imshow("resize", resize)
        cv2.waitKey(0)
        cv2.imshow("image", self.original_image)
        cv2.waitKey(0)

    def refresh_read(self):
        self.modified_image = cv2.imread(self.image_path)