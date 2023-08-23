import matplotlib.pyplot as plt
import numpy as np
import utils
from PIL import Image
import cv2


class TwoDAnalyzer:
    sum_matrix: 'np.ndarray'
    number_of_images: 'int'
    def __init__(self, dir_path):
        files = utils.get_file_paths(dir_path + "*.jpg")
        files.sort()
        image1 = np.array(Image.open(files[0]))
        self.sum_matrix = np.zeros(
            [len(image1), len(image1[0])])  # gonna contain accumulated values of pixels at respective coordinates
        for i in range(len(files)):
            img = cv2.imread(files[i], cv2.IMREAD_GRAYSCALE)
            self.sum_matrix = np.add(self.sum_matrix, img)
        self.number_of_images = len(files)

    def plotAvgVal2DHist(self):
        avg_mat = np.round(self.sum_matrix / self.number_of_images)
        plt.imshow(avg_mat)
        plt.colorbar()

    def plotAccVal2DHist(self):
        plt.imshow(self.sum_matrix)
        plt.colorbar()
