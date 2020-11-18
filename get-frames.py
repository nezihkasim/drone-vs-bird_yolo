import cv2
vidcap = cv2.VideoCapture('00_09_30_to_00_10_09.mp4')
success,image = vidcap.read()
count = 3422
while success:
  cv2.imwrite("%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1