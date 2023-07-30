import concept2
import matplotlib.pyplot as plt

import concept1
def main():
    dir_path = "data/"
    MyGa = concept2.GalleryAnalyzer(dir_path)
    MyGa.createCommonHistogram()
    filter = lambda x:
    #MyGa.createMiHistogram(bins=32)
    #MyGa.createSdHistogram(bins=32)
    #MyGa.createMedHistogram(bins=32)
    MyGa.showHistograms()
    #MyGa.createCommonHistogram()

if __name__ == "__main__":
        main()
