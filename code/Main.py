import sys
import numpy as np
from frequency_analyzer import GalleryAnalyzer
import matplotlib.pyplot as plt
from two_d_analyzer import TwoDAnalyzer


def main():

    dir_path = "/home/antonio123/workspace/Github_projects/StatisticalImageAnalysis/data/*jpg"
    """
    if sys.argv[0]:
        dir_path = sys.argv[1]
    else:
        print("No directory specified!")
        exit(-1)
    """
    MyGa = GalleryAnalyzer(dir_path)
    fig1 = plt.figure()
    MyGa.createKDEHistogram()
    plt.title("Pixel distribution of entire dataset")
    fig2 = plt.figure()
    MyGa.createHistogram()
    plt.title("Density aproximation for pixel intensities of entire dataset")
    fig3 = plt.figure()
    My2D = TwoDAnalyzer(dir_path)
    My2D.plotAvgVal2DHist()
    fig4 = plt.figure()
    My2D.plotAccVal2DHist()


    if len(sys.argv) > 2:
        fig1.savefig(sys.argv[2] % "smoothed_pixel_distribution")
        fig2.savefig(sys.argv[2] % "pixel_distribution")
        fig3.savefig(sys.argv[2] % '2D distribution of average pixel value')
        fig4.savefig(sys.argv[2] % '2D distribution of accumulated pixel value')
    else:
        plt.show()



if __name__ == "__main__":
        main()
