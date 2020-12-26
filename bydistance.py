import cv2
from numpy import *
import numpy as np
import math

for i in range(1,21):
    k1 =  str(i) + ".jpg"
    k2 = r"C:\Users\93733\STUDY\31\cv\123123\static"
    k = k2 + '\\' +k1
    print(k)
    image = cv2.imread(k)
    (imagex,imagey,imagez) = image.shape
    (B,G,R) = cv2.split(image)
    #print(image.shape)


    person = False
    person_high = 0
    bird =  False
    bird_low = 10000
    plane = False
    plane_low = 10000

    person_left = 10000
    person_right = 0
    skateboard_left = 10000
    skateboard_right = 0
    for x in range(0,imagex):
        for y in range(0,imagey):
            if(R[x][y]==128 and G[x][y]==0):#plane
                plane = True
                plane_low = min(plane_low,x)
                skateboard_left = min(skateboard_left,y)
                skateboard_right = max(skateboard_right,y)

            elif(R[x][y]==128 and G[x][y]==128):#bird
                bird = True
                bird_low = min(bird_low,x)
                skateboard_left = min(skateboard_left,y)
                skateboard_right = max(skateboard_right,y)
            elif(R[x][y]==192):#person
                person = True
                person_high = max(person_high,x)
                person_left = min(person_left,y)
                person_right = max(person_right,y)
    if(person==False):
        print("static")
        continue
    if(bird==False and plane==False):
        if(person==True):
            print("sliding")
        else:
            print("static")
        continue
    if(person_high<imagex*0.4):
        print("overhead")
        continue
    distance = 0
    if(bird==True):
        distance = max(0,bird_low-person_high)
    if(plane==True):
        distance = max(distance,plane_low-person_high)
    if((skateboard_left<person_right and skateboard_right>=person_right)or (skateboard_left<=person_left and skateboard_right>person_left)):
        if(distance>10):
            print('overhead')
            continue
        else:
            print('sliding')
            continue
    else:
        print('static')
        continue
    

#overhead:11/20
#sliding:6/20
#static:12/20
#total:29/60=48.3%