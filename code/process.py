import cv2
import utils
import os
import sys
from PIL import Image
import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt
from tqdm import tqdm
import patchify
import os

def ROI(dir_path):
    mask_files = utils.get_file_paths("/home/antonio123/workspace/Github_projects/StatisticalImageAnalysis/data/*.png")
    mask_files.sort()
    files = utils.get_file_paths(dir_path + "*.jpg")
    files.sort()
    images = []
    for count, file in enumerate(files, 0):
        print(count, file)
    for i in tqdm(range(len(files))):
        img = cv2.imread(files[i], cv2.IMREAD_GRAYSCALE)
        mask = cv2.imread(mask_files[i], cv2.IMREAD_GRAYSCALE)
        ROI_data = utils.getROI(img, mask)
        images.append(ROI_data)
    return images

def sectionImages(images: "list", dimension, output_dir):
    #if not os.path.exists(output_dir):
        #os.makedirs(output_dir)

    patches = []
    for idx, image in enumerate(images):
        tmp = patchify.patchify(image, (dimension, dimension), step=dimension)
        image_patches = []

        for row in tmp:
            for patch in row:
                if not (np.all(patch == 0) or np.all(patch == 2)):
                    image_patches.append(patch)

        #subdir_path = os.path.join(output_dir, str(idx))
        #os.makedirs(subdir_path)

        #for i, patch in enumerate(image_patches):
            #patch_filename = f"patch_{i}.png"  # You can change the naming pattern
            #patch_path = os.path.join(subdir_path, patch_filename)

            # Convert and save the patch as an image
            #patch_image = Image.fromarray(patch)
            #patch_image.save(patch_path)

        patches.extend(image_patches)

    return patches

def saveImages(images, save_path, start_index):
    org = os.getcwd()
    os.chdir(save_path)
    for i in range(len(images)):
        cv2.imwrite("slika" + str(start_index + i) + ".jpg", images[i])
    os.chdir(org)
    pass

def gamma_corr(img_original, gamma):
    lookUpTable = np.empty((1, 256), np.uint8)
    for i in range(256):
        lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    return cv2.LUT(img_original, lookUpTable)

def applyGamma(images, gamma):
    pr_images = [gamma_corr(image, gamma) for image in images]
    return pr_images

def main():
    gamma = 1
    if sys.argv[0] and len(sys.argv) > 2:
        src_path = sys.argv[1]
        save_path = sys.argv[2]
        if len(sys.argv) > 3:
            gamma = float(sys.argv[3])
    else:
        print("No directory specified!")
        exit(-1)

    files = utils.get_file_paths(src_path)
    print(files)
    files.sort()
    batch_size = 5
    # Process images in batches
    for batch_start in range(0, len(files), batch_size):
        batch_paths = files[batch_start:batch_start + batch_size]
        print(batch_paths)
        batch_images = [np.array(Image.open(file).convert('L')) for file in batch_paths]

        # Process the batch of images

        #gamma = input("What gamma do you want to apply")
        #images = images = applyGamma(images, int(gamma))

        #if cond == "yes": images = applyHistEq(images)
        batch_images = sectionImages(batch_images, 200, save_path)
        saveImages(batch_images, save_path, batch_start)

    """
    plt.figure()
    plt.imshow(images[0])
    plt.figure()
    plt.imshow(eq_images[0])
    plt.show()
    """

if __name__ == "__main__":
        main()

