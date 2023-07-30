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

def addFrequencies(frequencies, mat):
    for i in mat:
        for j in i:
            frequencies[j] += 1

    return frequencies

class GalleryAnalyzer:
    images = []
    freq = np.zeros([256])

    def __init__(self, file_dir):
        files = get_file_paths(file_dir)
        print(files)
        for file in files:
            data = np.array(Image.open(file).convert('L'))
            self.freq = addFrequencies(self.freq, data)
            self.images.append((ImageStatistics(file)))

    def getImageStatistics(self):
        return self.images

    def createMiHistogram(self, bins=256):
        mi_s = np.array(list(map(lambda x:np.round(x.getMi()), self.images)))
        print(mi_s)
        _ = plt.hist(mi_s, bins=bins, color = 'blue')
        #plt.show()

    def createSdHistogram(self, bins=256):
        sd_s = np.array(list(map(lambda x:np.round(x.getSd()), self.images)))
        _ = plt.hist(sd_s, bins=bins, color = 'red')
        #plt.show()

    def createMedHistogram(self, bins=256):
        """Creates histogram using average pixel value of every image in a directory"""
        med_s = np.array(list(map(lambda x:np.round(x.getMed()), self.images)))
        _ = plt.hist(med_s, bins=bins, color = 'green')
        #plt.show()

    def filterData(self, filter):
        """Modifies dataset using given filter function"""
        for i in range(256):
            self.freq[i] = filter(self.freq[i], i)
    def getMi(self):
        """Returns average value of dataset that includes all pixels from all images in a directory"""
        intensities = np.arange(256)
        return np.average(intensities, weights=self.freq)

    def getVar(self):
        """Returns variance of dataset that includes all pixels from all images in a directory"""
        mi = self.getMi()
        intensities = np.arange(256)
        dev = self.freq * (intensities - mi) ** 2
        return dev.sum() / (self.freq.sum() - 1)

    def getSd(self):
        """Returns standard deviation of dataset that includes all pixels from all images in a directory"""
        intensities = np.arange(256)
        return np.sqrt(self.getVar())

    def createCommonHistogram(self):
        """Creates histogram using dataset of pixels from all images in a directory"""
        bins = np.arange(257)
        intensities = np.arange(256)
        positions = range(len(intensities))
        #  plt.bar(positions, self.freq, tick_label=intensities)
        plt.hist(intensities, bins=bins, weights=self.freq)

    def showHistograms(self):
        plt.show()


