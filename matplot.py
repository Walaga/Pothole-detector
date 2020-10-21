import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

# Plotting the bounding boxes by manually placing in the coordinates gotten from the json file

im = np.array(Image.open('pothole 3.jpg'), dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)
#Coordinates had to be interchanged from those in label box due to different coordinate systems, top to left, left to top, height to width and width to height.
# Create a Rectangle patch
rect1 = patches.Rectangle((209,337),69,19,linewidth=1,edgecolor='r',facecolor='none')
rect2 = patches.Rectangle((293,356),33,21,linewidth=1,edgecolor='r',facecolor='none')
rect3 = patches.Rectangle((93,291),10,19,linewidth=1,edgecolor='r',facecolor='none')
rect4 = patches.Rectangle((52,290),14,9,linewidth=1,edgecolor='r',facecolor='none')
rect5 = patches.Rectangle((18,289),12,7,linewidth=1,edgecolor='r',facecolor='none')
rect6 = patches.Rectangle((40,264),34,5,linewidth=1,edgecolor='r',facecolor='none')
rect7 = patches.Rectangle((92,276),12,7,linewidth=1,edgecolor='r',facecolor='none')

# Add the patch to the Axes
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)
ax.add_patch(rect4)
ax.add_patch(rect5)
ax.add_patch(rect6)
ax.add_patch(rect7)

plt.show()