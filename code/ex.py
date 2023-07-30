import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import xml.etree.ElementTree as ET
import sys, os, glob


#file_dir = "./data/*.xml"
print(sys.argv)

def get_file_paths(directory_path):
    file_paths = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths
def read_content(xml_file: str):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    list_with_all_boxes = []

    filename = ""

    for boxes in root.iter('object'):

        filename = root.find('filename').text

        ymin, xmin, ymax, xmax = None, None, None, None

        ymin = int(boxes.find("bndbox/ymin").text)
        xmin = int(boxes.find("bndbox/xmin").text)
        ymax = int(boxes.find("bndbox/ymax").text)
        xmax = int(boxes.find("bndbox/xmax").text)

        list_with_single_boxes = [xmin, ymin, xmax, ymax]
        list_with_all_boxes.append(list_with_single_boxes)

    return filename, np.asarray(list_with_all_boxes)


def get_object_attributes(bb) -> np.array:
    centroid = np.array([(bb[1] + bb[3])/2, (bb[0] + bb[2])/2])     # (x_c, y_c)
    size = (bb[3] - bb[1])*(bb[2] - bb[0])
    return centroid, size


def get_files(dir) -> str:
    files = glob.glob(dir)
    return files


def main():

    centroid = []
    size = []

    if sys.argv[0]:
        file_dir = sys.argv[1]
    else:
        print("No directory specified!")
        exit(-1)

    files = get_file_paths(file_dir)
    print("Total number of files: ", len(files))

    if len(files) == 0:
        print(files)
        print("No files found.")
        exit(-1)

    for file in files:
        name, boxes = read_content(file)

        for cnt, box in enumerate(boxes):
            centroid_, size_ = get_object_attributes(box)
            centroid.append(centroid_)
            size.append(size_)

    centroid = np.asarray(centroid)
    size = np.asarray(size)

    print("Total number of instances: ", centroid.shape[0])

    fig1 = plt.figure()
    h1 = plt.hist2d(centroid[:, 0], centroid[:, 1], norm=colors.Normalize())
    plt.title('Object centroid distribution')
    plt.xlim([0, 1024])
    plt.ylim([0, 1280])
    plt.colorbar(h1[3])

    fig2 = plt.figure()
    h2 = plt.hist(size)
    plt.title('Object size distribution')

    if len(sys.argv) > 2:
        fig1.savefig(sys.argv[2] % "centroid")
        fig2.savefig(sys.argv[2] % "size")
    else:
        plt.show()


if __name__ == "__main__":
    main()
