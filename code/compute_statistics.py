from imageStatistics import ImageStatistics
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys
from skimage import io
import skimage
import os, sys

def get_file_paths(directory_path):

    file_paths = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

def calculateStatistics(images):
    image_statistics = []
    for img in images:
        pom = ImageStatistics(img)
        image_statistics.append(pom)
    return image_statistics

def calculateStatisticsForAll(images):
    data = np.array(map(lambda x:x.data, images)).ravel()

def main():
    file_dir = "data/"
    if sys.argv[0]:
         file_dir = sys.argv[1]
    else:
         print("No directory specified!")
         exit(-1)

    images = get_file_paths(file_dir)
    statistics = calculateStatistics(images)

    mi_s = list(map(lambda x: np.round(x.getMi()), statistics))
    sd_s = list(map(lambda x: np.round(x.getSd()), statistics))
    med_s = list(map(lambda x: np.round(x.getMed()), statistics))

    print(mi_s)
    print(sd_s)
    print(med_s)

    ax = plt.hist(mi_s, bins = 255)
    bx = plt.hist(sd_s, bins = 255)
    plt.show()

if __name__ == "__main__":
        main()

#print(get_file_paths("data/"))

def imagesToData(directory_path):
    files  = get_file_paths()