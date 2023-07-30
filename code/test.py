import numpy as np
from PIL import Image
from skimage import io
import matplotlib.pyplot as plt

data = np.array([1, 2, 1, 4, 5, 2, 1])
freq = np.zeros([6])
inten = np.arange(6)

def addFrequencies(frequencies, data):
    for i in data:
        frequencies[i] += 1
    return frequencies

freq = addFrequencies(freq, data)


image = np.array(Image.open("data1/slika1.jpg").convert('L'))

intensities = np.arange(256)
freq2 = np.zeros(256)
freq2 = addFrequencies(freq2, image)

def create_bar_chart(value_frequency_pairs):
    values, frequencies = zip(*value_frequency_pairs)
    positions = range(len(values))

    plt.bar(positions, frequencies, tick_label=values)

    # Label every tenth bar
    x_labels = [str(value) if i % 10 == 0 else "" for i, value in enumerate(values)]
    plt.xticks(positions, x_labels, rotation=45, ha="right")

    plt.xlabel('Values')
    plt.ylabel('Frequencies')
    plt.title('Bar Chart of Value Frequencies')
    plt.tight_layout()
    plt.show()


# Example data - value frequency pairs
value_frequency_pairs = [
    ('A', 15),
    ('B', 20),
    ('C', 40),
    ('D', 30),
    ('E', 10),
    ('F', 25),
    ('G', 5),
    # Add more data here if needed
]
image = np.array(Image.open("data1/slika1.jpg").convert('L')).ravel()
freq2 = np.zeros(256)
freq2 = addFrequencies(freq2, image)
edges = np.arange(257)
#_ = plt.stairs(freq2, intenisities, edges=edges)
#plt.hist(intensities, intensities,  weights=freq2)
_=plt.hist(image.ravel(), 256)
plt.show()
#create_bar_chart(value_frequency_pairs)
