import cv2
import utils
import os
import sys
from PIL import Image
import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt

def saveImages(images, save_path):
    os.chdir(save_path)
    for i in range(len(images)):
        cv2.imwrite("slika" + str(i) + ".jpg", images[i])
    pass

def gamma_corr(img_original, gamma):
    lookUpTable = np.empty((1, 256), np.uint8)
    for i in range(256):
        lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    return cv2.LUT(img_original, lookUpTable)


def main():
    gamma = 1
    if sys.argv[0] and len(sys.argv) > 2:
        src_path = sys.argv[1]
        save_path = sys.argv[2]
        if len(sys.argv[0] > 3):
            gamma = sys.argv[3]
    else:
        print("No directory specified!")
        exit(-1)

    files = utils.get_file_paths(src_path)
    images = [np.array(Image.open(file).convert('L')) for file in files]
    pr_images = [cv2.equalizeHist(image) for image in images]
    pr_images = [gamma_corr(image, gamma) for image in pr_images]
    saveImages(pr_images, save_path)

    """
    plt.figure()
    plt.imshow(images[0])
    plt.figure()
    plt.imshow(eq_images[0])
    plt.show()
    """

if __name__ == "__main__":
        main()
