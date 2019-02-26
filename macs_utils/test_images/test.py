import images as im
from PIL import Image
from macs_utils.utils import create_random_subarray
import os

image_paths = create_random_subarray(os.listdir(), min_length=5, max_length=10)

image_paths = [x for x in image_paths if '.jpg' in x]

images = [Image.open(x) for x in image_paths]

# result = im.tile_images_vertically(images=images, descriptions=image_paths, desc_row_height=20)

result = im.arrange_images_horizontally(images=images, descriptions=image_paths, desc_row_height=20, dilatation=5)

result.save('tiled.png')