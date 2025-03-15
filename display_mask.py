import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

mask_path = './guatemala-volcano_00000000_pre_disaster_target.png'

mask_img = Image.open(mask_path)

mask_np = np.asarray(mask_img)

print("mask color:", np.unique(mask_np))

plt.imshow(mask_img, cmap='gray')
plt.show()