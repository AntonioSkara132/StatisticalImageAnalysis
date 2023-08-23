import numpy as np
import matplotlib.pyplot as plt
from stats import Stats
import utils
from PIL import Image
import seaborn as sns
from tqdm import tqdm
import cv2
import pandas as pd

class GalleryAnalyzer:
    "Computes statistical analysis for a given set of images, and creates histograms for working with Matlib.pyplot module"
    imageStats = []
    freqs = np.zeros([256])

    def __init__(self, dir_path):
        files = utils.get_file_paths(dir_path + "*.jpg")
        files.sort()
        progress_bar = tqdm(total=100)
        for i in range(len(files)):
            progress_bar.update(100/len(files))
            data = cv2.imread(files[i], cv2.IMREAD_GRAYSCALE)
            self.freqs = utils.addFrequencies(self.freqs, data)
            self.imageStats.append((Stats(data)))
        progress_bar.close()

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

    def getMed(self):
        """Returns median of dataset that includes all pixels from all images in a directory"""
        intensities = np.arange(256)
        return utils.calculate_median_from_counts(intensities, self.freqs)

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

    def showMeasuers(self):
        measures = ["OV. average", "OV. median", "OV. standard\ndeviation"]
        values = [self.getMi(), self.getMed(), self.getSd()]
        plt.barh(measures, values)
        xtick_positions = np.linspace(0, max(values), 20)
        plt.yticks(rotation=90)
