
# croping black background from images

import cv2
import os,glob

count = 1
for im in glob.glob('ships_croped/*.png'):
    file = os.path.splitext(im)
    src = cv2.imread(im, 1)
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    print(count)
    cv2.imwrite('Ship_' + str(count) + ".png", dst)
    count += 1
