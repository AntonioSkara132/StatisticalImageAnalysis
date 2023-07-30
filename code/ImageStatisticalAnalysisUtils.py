import glob
import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def get_file_paths(directory_path):
    """Return a list of paths matching a pathname pattern."""
    return glob.glob(directory_path)

def addFrequencies(freqs, mat):
    """Counts index values"""
    for i in mat:
        freqs[i] += 1
    return freqs

class GalleryAnalyzer:
    imageStats = []
    freqs = np.zeros([256])

    def __init__(self, file_dir):
        files = get_file_paths(file_dir)
        print(files)
        for image in files:
            data = np.array(Image.open(image).convert('L')).ravel()
            self.freqs = addFrequencies(self.freqs, data)
            self.imageStats.append((Stats(data)))

    def getImageStatistics(self):
        return self.imageStats

    def createMiHistogram(self, bins=256):
        mi_s = np.array(list(map(lambda x:np.round(x.getMi()), self.imageStats)))
        print(mi_s)
        _ = plt.hist(mi_s, bins=bins, color = 'blue', alpha = 0.5)
        #plt.show()

    def createSdHistogram(self, bins=256):
        sd_s = np.array(list(map(lambda x:np.round(x.getSd()), self.imageStats)))
        _ = plt.hist(sd_s, bins=bins, color = 'red', alpha = 0.5)
        #plt.show()

    def createMedHistogram(self, bins=256):
        """Creates histogram using average pixel value of every image in a directory"""
        med_s = np.array(list(map(lambda x:np.round(x.getMed()), self.imageStats)))
        _ = plt.hist(med_s, bins=bins, color = 'green', alpha = 0.5)
        #plt.show()

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
        intensities = np.arange(256)
        return np.sqrt(self.getVar())

    def createCommonHistogram(self, cutEdges = 0):
        """Creates histogram using dataset of pixels from all images in a directory"""
        freq = self.freqs
        for i in range(cutEdges):
            freq[i] = 0; freq[255-i] = 0
        bins = np.arange(257)
        intensities = np.arange(256)
        positions = range(len(intensities))
        #  plt.bar(positions, self.freq, tick_label=intensities)
        plt.hist(intensities, bins=bins, weights=self.freqs)

class Stats:
    data = []
    def __init__(self, data):
        self.data = data

    def createHistogram(self):
        _ = plt.hist(self.data, bins=256)
        plt.show()

    def getMi(self) -> float:
        return np.average(self.data)
    def getSd(self) -> float:
        return np.std(self.data)
    def getMed(self) -> float:
        return np.median(self.data)
    def getData(self):
        return self.data

