from concurrent.futures import ThreadPoolExecutor
import requests
import cv2
import urllib.request
import numpy as np
import schedule
import threading
import csv
import time

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def sharpen_one(lines,index):
    
    lines=listToString(lines)
                
    resource = urllib.request.urlopen(lines)
                
                # input_loc="/media/aayush/3236805D368023C7/Users/aayus/Desktop/Work/Computer Vision/input"
    input = open("./Computer Vision/input/image-{}.jpg".format(index),"wb")
    input.write(resource.read())
    input.close()

            
    img=cv2.imread("./Computer Vision/input/image-{}.jpg".format(index))
    kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]]) #why this?  multithreading in python  how to put images in s3 bucket and how many can we put in one
    im = cv2.filter2D(img, -1, kernel)
                
    # output_loc="/media/aayush/3236805D368023C7/Users/aayus/Desktop/Work/Computer Vision/output"
    cv2.imwrite("./Computer Vision/output/image-{}.jpg".format(index),im)
    # time.sleep(0.1)
    return f"image-{index}"
    
    
def sharpen_all():
    
    start=time.perf_counter()
    
    location="/home/aayush/Downloads/upid_images(1).csv"
    
    with open(location, mode ='r')as file:
        csvFile = csv.reader(file)
        
        index=0
        list=[]
        pool=ThreadPoolExecutor(5)
        for lines in csvFile:
           
            if(index>3):
                
                list.insert(1,pool.submit(sharpen_one,lines,index))
                
                # t=threading.Thread(target=sharpen_one,args=(lines,index))
                # list.insert(1,t)
                # t.start()
                
                
                
            
            index=index+1
            
            
            if(index==100):
                break 
        
        print(threading.active_count())
        for i in list:
            print(i.result())

start=time.perf_counter()

sharpen_all()

end=time.perf_counter()
print(f"Finished in {round(end-start,2)} seconds")
    




