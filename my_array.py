# a = [1,4,3,2,5,6,7,8,9,10]
# a.append(11)
# print(a)
# a.sort()
# print(a)
# b = [6,1,7,3,8,3]
# print(b[4])
# c = "Hello"
# print(c[1])
# d=[[1,2,3],[4,5,6],[7,8,9]]
# print(d)
# print(d[1][2])
# import numpy as np
# import cv2
# a = np.zeros((1000,1000),dtype=np.uint8)
# print(a)
# b=np.ones((1080,1920),dtype=np.uint8)*100
# print(b)
# cv2.imshow("image b",b)
# cv2.waitKey(0)
import numpy as np
a = np.ones((1,10),dtype=np.uint8)
print(a)
b=np.ones((10,1),dtype=np.uint8)*3
print(b)
c=a*b
print(c)
c[3][1:]=0
print(c)