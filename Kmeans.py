import os
import cv2
import numpy
import joblib
from sklearn.cluster import KMeans
def clustering():
    eachClass = 15 # the image number we trained for each class
    Knumber = 200
    imagePath = "dataset/"
    imageClasses = os.listdir(imagePath)
    siftFeatures = numpy.zeros((0, 128))
    for imageClass in imageClasses:
        if imageClass != ".DS_Store":
            images = os.listdir(imagePath+imageClass)
            for i in range(eachClass):
                image = images[i] # read each image
                print(image)
                if image != ".DS_Store":
                    img = cv2.imread(imagePath+imageClass+"/"+image)
                    sift = cv2.xfeatures2d.SIFT_create()
                    keyPoint,descriptor = sift.detectAndCompute(img,None)
                    siftFeatures = numpy.append(siftFeatures,descriptor,axis=0) # we can use these data to do K-means
    
    print("sift done")
    cluster = KMeans(n_clusters=Knumber)
    cluster.fit(siftFeatures)
    joblib.dump(cluster,"kmeans.sav")
    print("Kmeans down")
if __name__ == "__main__":
    clustering()


