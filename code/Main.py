import sys
import numpy as np
from frequency_analyzer import GalleryAnalyzer
import matplotlib.pyplot as plt
from two_d_analyzer import TwoDAnalyzer
import utils
from tqdm import tqdm

def main():
    #dir_path = "/home/antonio123/Documents/Praksa/defects_analysis/train/img-236-_bmp.rf.f195b4f05a3ab43cc35444c3da3a7394_mask.png"

    if sys.argv[0]:
        if len(sys.argv) > 1:
            dir_path = sys.argv[1]
        else:
            dir_path = "/home/antonio123/workspace/Github_projects/StatisticalImageAnalysis/data/all_images/*.jpg"
    else:
        print("No directory specified!")
        exit(-1)

    progress_bar = tqdm(total=100)
    MyGa = GalleryAnalyzer(dir_path, False)
    figures = []
    progress_bar.update(20)

    figures.append(plt.figure())
    MyGa.createKDEHistogram()
    plt.title("Density aproximation for pixel intensities of entire dataset(underfitted)")
    progress_bar.update(10)

    figures.append(plt.figure())
    MyGa.createHistogram(cutEdges=False)
    plt.title("Pixel distribution of entire dataset")
    progress_bar.update(10)

    figures.append(plt.figure())
    MyGa.createHistogram(cutEdges=True)
    plt.title("Pixel distribution of entire dataset(with clipped edges)")
    My2D = TwoDAnalyzer(dir_path)
    progress_bar.update(10)

    figures.append(plt.figure())
    My2D.plotAccVal2DHist()
    plt.title("Spatial distribution of accumulated pixel value")
    progress_bar.update(10)

    figures.append(plt.figure())
    My2D.plotAvgVal2DHist()
    plt.title("Spatial distribution of average pixel \n value")
    progress_bar.update(20)

    figures.append(plt.figure())
    MyGa.showMeasuers()
    progress_bar.update(20)

    if len(sys.argv) > 2:
        size = len(figures)
        names = [str(i) for i in range(size)]
        filenames = [("./results/" + name + ".png") for name in names]

        for i in range(size):
            figures[i].savefig(filenames[i])

        utils.saveAsExcel(sys.argv[2], filenames)

    else:
        plt.show()

if __name__ == "__main__":
        main()
