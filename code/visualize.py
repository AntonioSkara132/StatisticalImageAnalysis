import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from pycocotools import mask as maskUtils

# Path to your COCO annotation file
ann_file = '/annotations/_annotations.coco.json'

# Plot each annotation with segmentation mask
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from pycocotools.coco import COCO

# Path to your COCO annotation file

# Initialize COCO API
coco = COCO(ann_file)

# Select an image and its corresponding annotations
image_id = coco.getImgIds()[3]
annotations = coco.loadAnns(coco.getAnnIds(imgIds=image_id))

# Load the image dimensions from the image info
image_info = coco.loadImgs(image_id)[0]
image_height = 200
image_width = 200

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

