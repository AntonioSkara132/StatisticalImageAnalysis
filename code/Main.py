import sys
import ImageStatisticalAnalysisUtils as isa
import matplotlib.pyplot as plt

def main():

    #dir_path = "/home/antonio123/workspace/Github_projects/StatisticalImageAnalysis/data/*.jpg"

    if sys.argv[0]:
        dir_path = sys.argv[1]
    else:
        print("No directory specified!")
        exit(-1)

    MyGa = isa.GalleryAnalyzer(dir_path)
    fig1 = plt.figure()
    MyGa.createCommonHistogram()
    plt.title("Pixel distribution")
    fig2 = plt.figure()
    MyGa.createMedHistogram(bins = 32)
    MyGa.createMiHistogram(bins = 32)
    MyGa.createSdHistogram(bins = 32)
    _ = plt.legend(['Median', 'Average', 'Standard Deviation'])
    plt.title("Statistical data")
    plt.show()

    if len(sys.argv) > 2:
        fig1.savefig(sys.argv[2] % "pixel_histogram")
        fig2.savefig(sys.argv[2] % "med_mi_sd_histogram")
    else:
        plt.show()

if __name__ == "__main__":
        main()
