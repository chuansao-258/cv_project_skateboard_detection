import joblib
import numpy
import os
import cv2
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
            for i in range(eachClass,len(images)):
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
def Test():
    test,label = transform()
    classifier = joblib.load("svm.sav")
    predictResult = classifier.predict(test)
    succ = 0
    for i in range(test.shape[0]):
        print("pre:",predictResult[i])
        print("truth:",label[i])
        if predictResult[i] == label[i]:
            succ = succ + 1
    return succ / test.shape[0],succ
if __name__ == "__main__":
    acc,succ = Test()
    print(acc)