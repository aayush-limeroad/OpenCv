import requests # request img from web
import shutil # save img locally
import cv2
import urllib.request
import numpy as np
import threading


resource = urllib.request.urlopen("https://img0.junaroad.com/scraps/scrap_63ac2a0badb8b84ef73a9622.png")
file_name = r'C:\Users\aayus\Desktop\Work\Computer Vision\image.jpg'
kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])

def download_image():
    output = open("file01.jpg","wb")
    output.write(resource.read())
    output.close()

def sharpen():
	img = cv2.imread("./file01.jpg")
    im = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(file_name,im)
    #  why this?  multithreading in python  how to put images in s3 bucket and how many can we put in one


if __name__ =="__main__":
	# creating thread
	t1 = threading.Thread(target=sharpen)
	t2 = threading.Thread(target=download_image)

	# starting thread 1
	t1.start()

	# starting thread 2
	t2.start()

	# wait until thread 1 is completely executed
	t1.join()
	# wait until thread 2 is completely executed
	t2.join()

	# both threads completely executed
	print("Done!")
