import glob
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def get_file_paths(directory_path: 'str') -> list:
    """Return a list of paths matching a pathname pattern."""
    return glob.glob(directory_path)

def addFrequencies(freqs, list):
    """Counts index values"""
    for i in list:
        freqs[i] += 1
    return freqs


class GalleryAnalyzer:
    "Computes statistical analysis for a given set of images, and creates histograms for working with Matlib.pyplot module"
    imageStats = []
    freqs = np.zeros([256])
    histogram_data = []

    def __init__(self, file_dir: "str"):
        files = get_file_paths(file_dir)
        #print(files)
        for image in files:
            data = np.array(Image.open(image).convert('L')).ravel().astype(int)
            self.freqs = addFrequencies(self.freqs, data)
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

    def createHistogram(self, cutEdges = 0):
        """Creates histogram using dataset of pixels from all images in a directory"""
        freq = self.freqs
        for i in range(cutEdges):
            freq[i] = 0; freq[255-i] = 0
        bins = np.arange(257)
        intensities = np.arange(256)
        positions = range(len(intensities))
        plt.hist(intensities, bins=bins, weights=self.freqs, density=True)


class Stats:
    "Calculates statistical information for given data"
    data = []

    def __init__(self, data):
        self.data = data

    def plotHistogram(self):
        """plots histogram using sdata"""
        _ = plt.hist(self.data, bins=256)
        plt.show()

    def getMi(self) -> float:
        """calculates average value of data"""
        return np.average(self.data)

    def getSd(self) -> float:
        """calculates standard deviation of data"""
        return np.std(self.data)

    def getMed(self) -> float:
        """calculates median of data"""
        return np.median(self.data)

    def getData(self):
        return self.data

