import sys
import numpy as np
import ImageStatisticalAnalysisUtils as isa
import matplotlib.pyplot as plt

def main():

    dir_path = "/home/antonio123/workspace/Github_projects/StatisticalImageAnalysis/test_data/*.gif"

    if sys.argv[0]:
        dir_path = sys.argv[1]
    else:
        print("No directory specified!")
        exit(-1)

    MyGa = isa.GalleryAnalyzer(dir_path)
    fig1 = plt.figure()
    MyGa.createHistogram()
    #MyGa.createHistogram(cutEdges=2)
    plt.title("Normalized Pixel distribution")
    plt.ylabel("Frequency")
    plt.xlabel("Intensities")

    fig2 = plt.figure()
    bins = 17
    mi_data = MyGa.getMiData()
    sd_data = MyGa.getSdData()
    med_data = MyGa.getMedData()
    MSM_data = x = np.dstack((mi_data, sd_data, med_data))[0]
    #_ = plt.hist(MSM_data, bins=bins, rwidth=0.7, range=(0, 255), histtype='barstacked')
    _ = plt.hist(MSM_data, bins, histtype='bar', stacked=True, range=(0, 255), rwidth=0.7)
    _ = plt.legend(['Average', 'Standard deviation', 'Median'])
    plt.title("Comparison of median, average and standard deviation values")
    plt.ylabel("Frequency")
    plt.xlabel("Intensity bins")
    plt.xticks(np.linspace(0, 255, bins+1))

    if len(sys.argv) > 2:
        fig1.savefig(sys.argv[2] % "pixel_histogram")
        fig2.savefig(sys.argv[2] % "med_mi_sd_histogram")
    else:
        plt.show()

if __name__ == "__main__":
        main()
