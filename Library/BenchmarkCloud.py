import numpy as np
import matplotlib.pyplot as plt
A1 = [5.99,5.59,5.60,6.12,5.59]
A2 = [10.92,11.00,10.78,8.68,11.02]
A3 = [18.83,15.53,15.33,19.55,18.92]
A4 = [32.96,27.2,32.91,33.49,28.41]
SD1 = [16.87,16.18,15.51,15.53,15.54]
SD2 = [28.46,28.14,27.43,28.23,27.71]
SD3 = [47.65,47.19,47.79,41.08,43.77]
SD4 = [72.75,74.77,60.59,73.23,76.35]
SD11 = [28.27,28.1,28.83,28.76,27.17]
SD12 = [43.14,49.91,47.56,42.64,48.8]
SD13 = [74.86,75.21,60.78,58.82,71.96]
SD1v2 = [23.84,23.05,21.04,14.23,17.03]
SD2v2 = [36.25,27.77,31.63,32.11,37.01]
SD3v2 = [48.16,46.68,46.62,48.04,46.62]
SD4v2 = [68.86,64.05,62.00,61.57,64.75]
SD11v2 = [37.81,36.07,37.22,35.31,33.38]
SD12v2 = [53.15,52.01,49.57,48.71,49.26]
SD13v2 = [61.68,60.58,63.48,64.42,61.28]
t2_micro = [2.06,2.10,2.09,2.53,2.13]
t2_small = [3.66,4.32,4.11,4.72,4.35]
t2_medium = [7.33,8.03,8.13,8.71,8.75]
t2_large = [12.67,12.55,13.03,12.68,10.50]
m4_large = [25.35,26.89,25.99,25.77,27.07]
m4_xlarge = [49.70,49.04,49.76,42.01,49.66]
m4_2xlarge = [67.72,75.96,81.18,80.15,70.36]
c4_large = [28.48,28.90,25.96,29.11,29.87]
c4_xlarge = [54.16,53.92,54.03,54.19,55.41]
c4_2xlarge = [89.68,73.46,92.04,67.75,87.29]
labels = ['A1', 'A2', 'A3', 'A4', 'SD1', 'SD2', 'SD3', 'SD4', 'SD11',
          'SD12', 'SD13', 'SD1v2', 'SD2v2', 'SD3v2', 'SD4v2', 'SD11v2',
          'SD12v2', 'SD13v2','t2.micro', 't2.small', 't2.medium', 't2.large',
          'm4.large', 'm4.xlarge', 'm4.2xlarge', 'c4.large',
          'c4.xlarge', 'c4.2xlarge']
arr = [A1, A2, A3, A4, SD1, SD2, SD3, SD4, SD11, SD12, SD13,SD1v2, SD2v2,
       SD3v2, SD4v2, SD11v2, SD12v2, SD13v2,t2_micro, t2_small, t2_medium,
       t2_large, m4_large, m4_xlarge, m4_2xlarge, c4_large, c4_xlarge, c4_2xlarge]
bp = plt.boxplot(arr)
index = np.arange(len(labels))
bar_width = 1
plt.xlabel('Cluster Name')
plt.ylabel('Operation per Minute')
plt.title('Scimark.Large')
plt.xticks(index+bar_width, labels, rotation='vertical')
plt.legend()
plt.tight_layout()
plt.show()
