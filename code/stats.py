import numpy as np
import matplotlib as plt

class Stats:
    "Calculates statistical information for given data"
    data = []

    def __init__(self, data):
        self.data = data

    def plotHistogram(self):
        """plots histogram of given data"""
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

    def getData(self) -> np.ndarray:
        """returns data"""
        return self.data