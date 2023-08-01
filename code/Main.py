import sys
import galleryanalyzer as isa
import matplotlib.pyplot as plt

def main():

    #dir_path = "/home/antonio123/workspace/Github_projects/StatisticalImageAnalysis/test_data/*.gif"

    if sys.argv[0]:
        dir_path = sys.argv[1]
    else:
        print("No directory specified!")
        exit(-1)

    MyGa = isa.GalleryAnalyzer(dir_path)
    fig1 = plt.figure()
    MyGa.createCommonHistogram()
    plt.title("Pixel distribution")

    if len(sys.argv) > 2:
        fig1.savefig(sys.argv[2] % "pixel_histogram")
        fig2.savefig(sys.argv[2] % "med_mi_sd_histogram")
    else:
        plt.show()

if __name__ == "__main__":
        main()
