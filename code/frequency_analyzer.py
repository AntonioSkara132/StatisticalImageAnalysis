import numpy as np
import matplotlib.pyplot as plt
from stats import Stats
import utils
from PIL import Image
import seaborn as sns
import pandas as pd

class GalleryAnalyzer:
    "Computes statistical analysis for a given set of images, and creates histograms for working with Matlib.pyplot module"
    imageStats = []
    freqs = np.zeros([256])
    histogram_data = []

    def __init__(self, file_dir: 'string'):
        files = utils.get_file_paths(file_dir)
        #print(files)
        for image in files:
            data = np.array(Image.open(image).convert('L')).ravel().astype(int)
            self.freqs = utils.addFrequencies(self.freqs, data)
            self.imageStats.append((Stats(data)))

    def getImageStatistics(self) -> list:
        """returns list of Stats instances, Stats store statistical information od images in dataset"""
        return self.imageStats

    def getMiData(self):
        """creates histogram using the average values of the images"""
        return np.array(list(map(lambda x:x.getMi(), self.imageStats)))

    def getSdData(self):
        """creates a histogram using the standard deviations of the images"""
        return np.array(list(map(lambda x:x.getSd(), self.imageStats)))

    def getMedData(self):
        """"creates a histogram using the median values of the images"""
        return np.array(list(map(lambda x:x.getMed(), self.imageStats)))

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

    def createHistogram(self, bins=255, cutEdges=False):
        """Creates histogram using dataset of pixels from all images in a directory"""
        freqs = self.freqs
        if cutEdges: freqs[0] = 0; freqs[255] = 0
        data = {'Frequency': freqs/np.sum(freqs), 'Intensity': np.arange(256)}
        sns.histplot(data, x='Intensity', weights='Frequency', bins=bins, discrete=True)
        plt.ylabel('Frequency')

    def createKDEHistogram(self, bw_adjust=0.065):
        """Creates histogram using dataset of pixels from all images in a directory"""
        data = {'Frequency': self.freqs / np.sum(self.freqs), 'Intensity': np.arange(256)}
        sns.kdeplot(data, x='Intensity', weights='Frequency', bw_adjust=bw_adjust)
        plt.ylabel("Frequency")
