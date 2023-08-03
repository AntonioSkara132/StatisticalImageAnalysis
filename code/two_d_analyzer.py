import matplotlib.pyplot as plt
import numpy as np
import utils
from PIL import Image

class TwoDAnalyzer:
    sum_matrix: 'np.ndarray'
    number_of_images: 'int'
    def __init__(self, dir_path):
        images = utils.get_file_paths(dir_path)
        image1 = np.array(Image.open(images[0]))
        self.sum_matrix = np.zeros(
            [len(image1), len(image1[0])])  # gonna contain accumulated values of pixels at respective coordinates
        for image in images:
            self.sum_matrix += np.array(Image.open(image).convert('L'))
        self.number_of_images = len(images)

    def plotAvgVal2DHist(self):
        avg_mat = np.round(self.sum_matrix / self.number_of_images)
        plt.imshow(avg_mat)
        plt.colorbar()

    def plotAccVal2DHist(self):
        plt.imshow(self.sum_matrix)
        plt.colorbar()
