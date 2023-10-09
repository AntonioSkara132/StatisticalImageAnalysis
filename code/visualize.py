import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from pycocotools.coco import COCO
import utils
import cv2


# Path to your COCO annotation file

def visualizeDataset(dir_path):
    files = utils.get_file_paths(dir_path)
    imgs = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in files]
    for i in range(20):
        plt.figure()
        plt.imshow(imgs[i])
        plt.show()

def visualize_coco(ann_file):

    # Plot each annotation with segmentation mask
    # Path to your COCO annotation file

    # Initialize COCO API
    coco = COCO(ann_file)

    # Select an image and its corresponding annotations
    image_id = coco.getImgIds()[3]
    annotations = coco.loadAnns(coco.getAnnIds(imgIds=image_id))

    # Load the image dimensions from the image info
    image_info = coco.loadImgs(image_id)[0]
    image_height = 2056
    image_width = 2464

    # Create a subplot for annotation visualization


    # Plot each annotation with polygon segmentation
    for i, ann in enumerate(annotations):
        if 'segmentation' in ann:
            segmentation = ann['segmentation']
            for seg in segmentation:
                x = seg[::2]
                y = seg[1::2]
                plt.figure(figsize=(8, 8))
                plt.imshow(np.zeros((image_height, image_width, 3)))  # Blank canvas
                plt.axis('off')
                poly = [(x[j], y[j]) for j in range(len(x))]
                polygon = Polygon(poly, edgecolor='r', facecolor='none', linewidth=2)
                plt.gca().add_patch(polygon)
                plt.text(x[0], y[0], str(i + 1), color='r', fontsize=12, verticalalignment='top')

    plt.show()

image = cv2.imread("/home/antonio123/workspace/Github_projects/StatisticalImageAnalysis/patches_masks/patch_11.jpg", cv2.IMREAD_GRAYSCALE)
utils.showImage(image)



