import glob

import matplotlib.pyplot as plt
import xlsxwriter as xls
import numpy as np
import cv2

def get_file_paths(directory_path: 'str') -> list:
    """Return a list of paths matching a pathname pattern."""
    return glob.glob(directory_path)

def addFrequencies(freqs, list):
    """Counts index values"""
    for i in list:
        freqs[i] += 1
    return freqs

def saveAsExcel(name: 'str', filenames: 'list'):
    workbook = xls.Workbook(name)
    worksheet = workbook.add_worksheet()
    for i in range(len(filenames)):
        worksheet.insert_image(chr(66 + (i % 3) * 10) + str(2 + int((i / 3)) * 25), filenames[i]) #B1, L1, V1, B26, L26...
    workbook.close()

def getROI(image: 'np.ndarray', mask):
    valid_intensities = [1, 3]
    thresholded = np.where(np.logical_or(mask == valid_intensities[0], mask == valid_intensities[1]), 1, 0).astype(np.uint8)
    return image*thresholded

def calculate_median_from_counts(values, counts):
    # Sort the values and corresponding counts
    sorted_data = sorted(zip(values, counts))

    total_count = sum(counts)

    # Calculate cumulative frequency
    cumulative_frequency = [0]
    for count in counts:
        cumulative_frequency.append(cumulative_frequency[-1] + count)

    # Find the middle position
    middle_position = total_count / 2 if total_count % 2 == 1 else total_count / 2 - 1

    # Find the position within the cumulative frequency
    for idx, freq in enumerate(cumulative_frequency):
        if freq > middle_position:
            median_position = idx - 1
            break

    # Calculate the median value based on the cumulative frequency
    median_value = sorted_data[median_position][0]

    return median_value

def filterImage(image: 'np.ndarray', desired_intensity):
    return cv2.inRange(image, desired_intensity, desired_intensity)

def showImage(image: np.ndarray):
    plt.figure()
    plt.imshow(image)
    plt.colorbar()
    plt.show()

