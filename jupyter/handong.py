# this is a way to read a file from a local drive

import matplotlib.pyplot as plt
from matplotlib.image import imread
img = imread('./images/2202.png')
plt.imshow(img)
plt.show()
