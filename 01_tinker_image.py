from PIL import Image
import numpy as np

image_raw = Image.open("/Users/tdrap/home/data/image.PNG") 
image = np.array(image_raw)

type(image)
pixel = image[0, 0, 0]
print(image[0,0,0])
print(type(pixel))
print(np.max(image))
print(np.min(image))