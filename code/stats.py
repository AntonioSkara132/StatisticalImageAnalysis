import matplotlib as plt
import numpy as np

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

    def getData(self) -> np.ndarray:
        return self.data