import glob
import numpy as np


def getFilePaths(directory_path: 'str') -> list:
    """Return a list of paths matching a pathname pattern."""
    return glob.glob(directory_path)

def addFrequencies(freqs, list) -> np.ndarray:
    """Counts index values"""
    for i in list:
        freqs[i] += 1
    return freqs
