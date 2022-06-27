# this is a way to read a file from a url
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
import PIL

url = 'https://github.com/idebtor/KMOOC-ML/blob/master/ipynb/images/joyai/person.png?raw=true'
img = np.array(PIL.Image.open(urllib.request.urlopen(url)))
plt.imshow(img)
plt.show()
