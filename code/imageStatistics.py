import numpy as np
from PIL import Image
import statistics

from matplotlib import pyplot as plt
from skimage import io
import numpy as np


class ImageStatistics:
    data = []
    mi = 0
    sd = 0
    med = 0

    def __init__(self, img_path):
        self.img = img_path
        image = io.imread(img_path)
        self.data = image.ravel()
        self.mi = np.average(self.data)
        self.sd = np.std(self.data)
        self.med = np.median(self.data)

    def createHistogram(self):
        _ = plt.hist(self.data, bins=256)
        plt.show()

    def getMi(self) -> float:
        return self.mi
    def getSd(self) -> float:
        return self.sd
    def getMed(self) -> float:
        return self.med
    def getData(self):
        return self.data
class GalleryAnalyzer():
    data = {}
    def __init__(self, images):
        data = load













