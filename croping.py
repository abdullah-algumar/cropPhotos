
# croping object from images using polygon

import numpy
from PIL import Image, ImageDraw
import os,glob
import itertools


count = 1

# read image as RGB (without alpha)
for (im,tx) in zip(glob.glob('images/*.png'),glob.glob('labelTxt-v1.5/1/*.txt')):
    file = os.path.splitext(im)
    text = os.path.splitext(tx)
    print(im,tx)
    img = Image.open(im).convert("RGB")

# # convert to numpy (for convenience)
    img_array = numpy.asarray(img)
# read text lines
    annotations = [x.replace("\n", "").replace(".0", "").split(" ") for x in open(tx).readlines()]
    annotations = [x for x in annotations if 'ship' in x]

    for annotation in annotations:
        polygon = [(int(annotation[0]), int(annotation[1])), (int(annotation[2]), int(annotation[3])), (int(annotation[4]), int(annotation[5])), (int(annotation[6]), int(annotation[7]))]

    #  # create new image ("1-bit pixels, black and white", (width, height), "default color")
        mask_img = Image.new('1', (img_array.shape[1], img_array.shape[0]), 0)
    #
        ImageDraw.Draw(mask_img).polygon(polygon, outline=1, fill=1)
        mask = numpy.array(mask_img)
    #
    #     # assemble new image (uint8: 0-255)
        new_img_array = numpy.empty(img_array.shape, dtype='uint8')
    #
    #     # copy color values (RGB)
        new_img_array[:,:,:3] = img_array[:,:,:3]
    #
    #     # filtering image by mask
        new_img_array[:,:,0] = new_img_array[:,:,0] * mask
        new_img_array[:,:,1] = new_img_array[:,:,1] * mask
        new_img_array[:,:,2] = new_img_array[:,:,2] * mask
    #
    #     # back to Image from numpy
        newIm = Image.fromarray(new_img_array, "RGB")
        print(count)
                # filepath = os.path.join('planes')
        newIm.save('ship' + str(count) + '.png')
        count += 1
    count = count + 1

