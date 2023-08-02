import sys
import numpy as np
from frequency_analyzer import GalleryAnalyzer
import matplotlib.pyplot as plt

def main():

    #dir_path = "/home/antonio123/workspace/Github_projects/StatisticalImageAnalysis/code/data/*jpg"

    if sys.argv[0]:
        dir_path = sys.argv[1]
    else:
        print("No directory specified!")
        exit(-1)

    MyGa = GalleryAnalyzer(dir_path)
    fig1 = plt.figure()
    MyGa.createKDEHistogram()
    fig2 = plt.figure()
    MyGa.createHistogram()
    if len(sys.argv) > 2:
        fig1.savefig(sys.argv[2] % "pixel_distribution")
        fig2.savefig(sys.argv[2]) % "smoothed_pixel_distribution"
    else:
        plt.show()

if __name__ == "__main__":
        main()
