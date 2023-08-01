import glob
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from stats import Stats
from utils import getFilePaths
from utils import addFrequencies


class GalleryAnalyzer:
    "Computes statistical analysis for a given set of images, and creates histograms for working with Matlib.pyplot module"
    imageStats = []
    freqs = np.zeros([256])

    def __init__(self, file_dir: "str"):
        files = getFilePaths(file_dir)
        #print(files)
        for image in files:
            data = np.array(Image.open(image).convert('L')).ravel().astype(int)
            self.freqs = addFrequencies(self.freqs, data)
            self.imageStats.append((Stats(data)))

    def getImageStatistics(self) -> list:
        """returns list of Stats instances, Stats stSore statistical information od images in dataset"""
        return self.imageStats

    def createMiHistogram(self, bins=256):
        """creates histogram using the average values of the images"""
        mi_s = np.array(list(map(lambda x:x.getMi(), self.imageStats)))
        _ = plt.hist(mi_s, bins=bins, color = 'blue', alpha = 0.5, rwidth = 0.7, range = (0, 255))

    def createSdHistogram(self, bins=256):
        """creates a histogram using the standard deviations of the images"""
        sd_s = np.array(list(map(lambda x:x.getSd(), self.imageStats)))
        _ = plt.hist(sd_s, bins=bins, color = 'red', alpha = 0.5, rwidth = 0.7, range = (0, 255))

    def createMedHistogram(self, bins=256):
        """"creates a histogram using the median values of the images"""
        med_s = np.array(list(map(lambda x:x.getMed(), self.imageStats)))
        _ = plt.hist(med_s, bins=bins, color='green', alpha = 0.5, rwidth = 0.7, range = (0, 255))

    def filterData(self, modifier):
        """Modifies dataset using given filter function"""
        for i in range(256):
            self.freqs[i] = modifier(self.freqs[i], i)

    def getMi(self):
        """Returns average value of dataset that includes all pixels from all images in a directory"""
        intensities = np.arange(256)
        return np.average(intensities, weights=self.freqs)

    def getVar(self):
        """Returns variance of dataset that includes all pixels from all images in a directory"""
        mi = self.getMi()
        intensities = np.arange(256)
        dev = self.freqs * (intensities - mi) ** 2
        return dev.sum() / (self.freqs.sum() - 1)

    def getSd(self):
        """Returns standard deviation of dataset that includes all pixels from all images in a directory"""
        return np.sqrt(self.getVar())

    def createCommonHistogram(self, cutEdges = 0):
        """Creates histogram using dataset of pixels from all images in a directory"""
        freq = self.freqs
        for i in range(cutEdges):
            freq[i] = 0; freq[255-i] = 0
        bins = np.arange(257)
        intensities = np.arange(256)
        positions = range(len(intensities))
        plt.hist(intensities, bins=bins, weights=self.freqs)


