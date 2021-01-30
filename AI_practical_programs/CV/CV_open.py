import matplotlib.pyplot as plt
import cv2
import numpy as np

row = 2
col = 3

OG_img = cv2.imread('1800.jpg' , cv2.COLOR_BGR2RGB)
other = cv2.imread('1800.jpg' , cv2.COLOR_BGR2RGB)
resize = cv2.resize(OG_img, (50, 50))

GRAY_img = cv2.imread('1800.jpg', 0)
IMG_1800 = OG_img[145:255, 80:325]
other[145:255, 80:325] = [0, 0, 0]

img_list = [OG_img, GRAY_img, IMG_1800, other, resize]
l = []

titles = [
    'Original',
    'Colour Change',
    'Only 1800',
    'Without 1800',
    'Resized'
]

fig = plt.figure()
plt.axis('off')

for index,img in enumerate(img_list):
    l.append(fig.add_subplot(row, col, index+1))
    sub_plot_title = titles[index]
    l[-1].set_title(sub_plot_title)
    plt.imshow(img)

fig.tight_layout()
plt.show()
