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
    mask_files = utils.get_file_paths(dir_path + "/*.png")
    mask_files.sort()
    files = utils.get_file_paths(dir_path + "/*.jpg")
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

def sectionImages(images: "list", dimension):
    #if not os.path.exists(output_dir):
        #os.makedirs(output_dir)

    threshold = 12

    patches = []
    for idx, image in enumerate(images):
        tmp = patchify.patchify(image, (dimension, dimension), step=dimension)
        image_patches = []

        for row in tmp:
            for patch in row:
                #if not (np.all(patch == 0) or np.all(patch == 2)):
                if not np.all(patch < threshold):
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

def sectionMaks(maks, images, dimension):
    # if not os.path.exists(output_dir):
    # os.makedirs(output_dir)

    threshold = 12

    patches = []
    for idx, image in enumerate(save_images):
        s_tmp = patchify.patchify(save_images[idx], (dimension, dimension), step=dimension)
        t_tmp = patchify.patchify(test_images[idx], (dimension, dimension), step=dimension)
        image_patches = []

        cond = lambda x: not np.all(x < threshold)

        for i in range(len(t_tmp)):
            for j in range(len(t_tmp[0])):
                # if not (np.all(patch == 0) or np.all(patch == 2)):
                if not cond(t_tmp[i][j]):
                    image_patches.append(utils.filterImage(s_tmp[i][j], 1))
                else: print(np.max(t_tmp[i][j]))
        # subdir_path = os.path.join(output_dir, str(idx))
        # os.makedirs(subdir_path)

        # for i, patch in enumerate(image_patches):
        # patch_filename = f"patch_{i}.png"  # You can change the naming pattern
        # patch_path = os.path.join(subdir_path, patch_filename)

        # Convert and save the patch as an image
        # patch_image = Image.fromarray(patch)
        # patch_image.save(patch_path)

        patches.extend(image_patches)
    return patches

def sectionImages2(save_images, test_images, dimension, cond):
    # if not os.path.exists(output_dir):
    # os.makedirs(output_dir)

    maks_patches = []
    image_patches = []
    for idx, image in enumerate(save_images):
        s_tmp = patchify.patchify(save_images[idx], (dimension, dimension), step=dimension)
        t_tmp = patchify.patchify(test_images[idx], (dimension, dimension), step=dimension)
        batch = []

        for i in range(len(t_tmp)):
            for j in range(len(t_tmp[0])):
                # if not (np.all(patch == 0) or np.all(patch == 2)):
                if cond(t_tmp[i][j]):
                    batch.append(s_tmp[i][j])
                else:
                    print(np.max(t_tmp[i][j]))

        image_patches.extend(batch)
    return image_patches


def saveImages(images, save_path, start_index):
    org = os.getcwd()
    os.chdir(save_path)
    for i in range(len(images)):
        cv2.imwrite("patch_" + str(start_index + i) + ".jpg", images[i])
    os.chdir(org)
    pass

def saveImages2(images, save_path, filenames):
    org = os.getcwd()
    os.chdir(save_path)
    for i in range(len(images)):
        cv2.imwrite(os.path.basename(filenames[i]), images[i])
        print(filenames[i])
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

    #space to code
    if sys.argv[0] and len(sys.argv) > 2:
        src_path = sys.argv[1]
        save_path = sys.argv[2]
        if len(sys.argv) > 3:
            gamma = float(sys.argv[3])
    else:
        print("No directory specified!")
        exit(-1)

    u_files = utils.get_file_paths(src_path + "/*.jpg")
    l_files = utils.get_file_paths(src_path + "/*.png")
    l_files.sort()
    u_files.sort()
    print(l_files)
    print(u_files)

    l_images = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in l_files]
    u_images = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in u_files]
    #cond = lambda x: not (np.all(x == 0) or np.all(x == 2) )  #thid deteremines which patches are gomna be saved
    #patches = sectionImages2(u_images, l_images, dimension=400, cond=cond)
    #print(len(patches))
    images = []
    images = applyGamma(u_images, 0.5)
    print(len(images))

    #patches = [utils.filterImage(patch, 1) for patch in patches]
    saveImages2(images, save_path, u_files)

if __name__ == "__main__":
        main()

