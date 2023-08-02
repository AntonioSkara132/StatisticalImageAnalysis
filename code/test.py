import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

image = np.array(Image.open("/home/antonio123/workspace/Github_projects/StatisticalImageAnalysis/test_data/2.gif").convert('L'))
image = image.ravel()
freqs = np.zeros([256])
for i in image:
    freqs[i] += 1

data = {'Counts': freqs/np.sum(freqs), 'Values': np.arange(256)}
print(freqs)
plt.figure()

plt.show()