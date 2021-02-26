import cv2

im_g = cv2.imread("smallgray.png",0)
print(im_g)

im_rgb = cv2.imread("smallgray.png",1)
print(im_rgb)

cv2.imwrite("smallgray2.png",im_g)