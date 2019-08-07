
import cv2

import numpy as np


img = cv2.imread('task1.png',0)

height, width = img.shape

#Zeros Array for padding image
a = [[ 0 for x in range(width + 2)] for w in range(height + 2)]
b = [[ 0 for x in range(width)] for w in range(height)]
c = [[ 0 for x in range(width)] for w in range(height)]

#Generating image with padding
for i in range(600):
    for j in range(900):
        a[i+1][j+1]= img[i][j]

#Sobel Operators
sobel_H = [[-1,0,1],[-2,0,2],[-1,0,1]] 
sobel_V = [[-1,-2,-1],[0,0,0],[1,2,1]]

k,l = 1,1

#Applying Sobel operator
for k in range(601):
    for l in range(901):
        b[k-1][l-1] = a[k-1][l-1]*sobel_H[0][0] + a[k-1][l]*sobel_H[0][1] + a[k-1][l+1]*sobel_H[0][2] + a[k][l-1]*sobel_H[1][0] + a[k][l]*sobel_H[1][1] + a[k][l+1]*sobel_H[1][2] + a[k+1][l-1]*sobel_H[2][0] + a[k+1][l]*sobel_H[2][1] + a[k+1][l+1]*sobel_H[2][2]
        c[k-1][l-1] = a[k-1][l-1]*sobel_V[0][0] + a[k-1][l]*sobel_V[0][1] + a[k-1][l+1]*sobel_V[0][2] + a[k][l-1]*sobel_V[1][0] + a[k][l]*sobel_V[1][1] + a[k][l+1]*sobel_V[1][2] + a[k+1][l-1]*sobel_V[2][0] + a[k+1][l]*sobel_V[2][1] + a[k+1][l+1]*sobel_V[2][2]


#Find maximum 
max =0
for i in range(600):
	for j in range(900):
		if(max<b[i][j]):
			max = b[i][j]

for i in range(600):
	for j in range(900):
		if(b[i][j]<0):
			b[i][j] = b[i][j]*(-1)
		if(c[i][j]<0):
			c[i][j] = c[i][j]*(-1)

b = np.asarray(b)		
c = np.asarray(c)	

#Eliminating values
pos_edge_x=(b) /(max)
pos_edge_y=(c)/(max)

#Combining both X and Y
edge_magnitude = (pos_edge_x ** 2 + pos_edge_y ** 2)**(0.5)
m =0
for i in range(600):
	for j in range(900):
		if(m<edge_magnitude[i][j]):
			m = edge_magnitude[i][j]

edge_magnitude /= m


cv2.imshow('image_X_direction',pos_edge_x)
cv2.waitKey(0)
cv2.imshow('image_Y_direction',pos_edge_y)
cv2.waitKey(0)
cv2.imshow('image_Combined',edge_magnitude)
cv2.waitKey(0)

#Saving Images : Uncomment the following code to save images.

pos_edge_x *= 255
pos_edge_y *= 255
edge_magnitude *= 255
cv2.imwrite('X-direction.png',pos_edge_x)
cv2.imwrite('Y-direction.png',pos_edge_y)
cv2.imwrite('X&Y-direction.png',edge_magnitude)







