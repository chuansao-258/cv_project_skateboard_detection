import numpy
import joblib
import cv2
import os
from sklearn import svm
def Poll(sifts,clusters):
    K = 500
    eigenVector = numpy.zeros((1,K))
    for i in numpy.nditer(clusters.predict(numpy.array(sifts, dtype=numpy.float16))):
        eigenVector[0,i] += 1
    return eigenVector
def transform():
    K = 500
    eachClass = 15
    clusters = joblib.load("kmeans.sav")
    vectors = numpy.zeros((0,K))
    labels = numpy.zeros(0)
    imagePath = "dataset/"
    imageClasses = os.listdir(imagePath)
    counter = 1
    for imageClass in imageClasses:
        if imageClass != ".DS_Store":
            images = os.listdir(imagePath+imageClass)
            for i in range(eachClass):
                image = images[i] # read each image
                label = numpy.array([counter])
                if image != ".DS_Store":
                    img = cv2.imread(imagePath+imageClass+"/"+image)
                    sift = cv2.xfeatures2d.SIFT_create()
                    keyPoint,descriptor = sift.detectAndCompute(img,None)
                    imageVector = Poll(descriptor,clusters)
                    vectors = numpy.append(vectors,imageVector,axis=0)
                    labels = numpy.append(labels,label,axis=0)
        counter = counter + 1
    return vectors,labels
                    
def trainSVM(vectors,labels):
    classifier = svm.SVC().fit(vectors,labels)
    joblib.dump(classifier,"svm.sav")
if __name__ == "__main__":
    vectors,labels = transform()
    trainSVM(vectors,labels)