import numpy as np
import matplotlib.pyplot as plt
import ImageStatisticalAnalysisUtils as isa

np.random.seed(19680801)

n_bins = 10
MyGa = isa.GalleryAnalyzer("/home/antonio123/workspace/Github_projects/StatisticalImageAnalysis/test_data/*.gif")

#MyGa.createHistogram()
bins = 17
mi_data = MyGa.getMiData()
sd_data = MyGa.getSdData()
med_data = MyGa.getMedData()
x = np.dstack((mi_data, sd_data, med_data))[0]
print(x)

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)
print(len(x[0]))
colors = ['red', 'tan', 'lime']

ax1.hist(x[0], n_bins, density=True, histtype='bar', stacked=True)
ax1.set_title('stacked bar')



fig.tight_layout()
plt.show()