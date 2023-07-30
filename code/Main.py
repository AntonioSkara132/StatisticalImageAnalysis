import sys
import ImageStatisticalAnalysisUtils as isa
import matplotlib.pyplot as plt

def main():

    if sys.argv[0]:
        dir_path = sys.argv[1]
    else:
        print("No directory specified!")
        exit(-1)

    dir_path = "data/*.jpg"
    MyGa = isa.GalleryAnalyzer(dir_path)
    plt.figure()
    MyGa.createCommonHistogram()
    plt.title("Pixel distribution")
    plt.figure()
    MyGa.createMedHistogram(bins = 32)
    MyGa.createMiHistogram(bins = 32)
    MyGa.createSdHistogram(bins = 32)
    _ = plt.legend(['Median', 'Average', 'Standard Deviation'])
    plt.title("Statistical data")
    plt.show()

if __name__ == "__main__":
        main()
