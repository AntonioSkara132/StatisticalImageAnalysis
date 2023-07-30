import os

import imageStatistics
import  compute_statistics
from imageStatistics import ImageStatistics
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def get_file_paths(directory_path):

    file_paths = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

class GalleryAnalyzer:
    images = []
    data = []
    def __init__(self, file_dir):
        files = get_file_paths(file_dir)
        for file in files:
            image = ImageStatistics(file)
            self.images.append(image)
        data = list(map(lambda x: x.data, self.images))
        self.data = list(np.concatenate(data).flat)
    def createHistogram(self):
        _ = plt.hist(self.data, bins=256)
        plt.show()

    def getImageStatistics(self):
        pass
    def createMiHstogram(self):
        pass

    def createSdHistogram(self):
        pass

    def createMedHistogram(self):
        pass

    def getMi(self):
        return np.average(self.data)
    def getSd(self):
        return np.std(self.data)