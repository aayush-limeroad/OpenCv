import  cv2
import numpy as np
import os
from PIL import Image

# print(os.getcwd())

os.chdir(r"C:\Users\aayus\Desktop\Udit data\New folder")
path="C:\\Users\\aayus\\Desktop\\Udit data\\New folder"

mwidth=0 
mheight=0

for file in os.listdir('.'):
    if(file.endswith(".jpg") or file.endswith(".jpeg")):
        img=cv2.imread(os.path.join(path,file))
        height = img.shape[0]
        width = img.shape[1]
        mwidth+=height
        mheight+=width

# mean_height = 0
# mean_width = 0
  
# num_of_images = len(os.listdir('.'))
# # print(num_of_images)
  
# for file in os.listdir('.'):
#     if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
#         im = Image.open(os.path.join(path, file))
#         width, height = im.size
#         mean_width += width
#         mean_height += height
    # im.show()   # uncomment this for displaying the image

mwidth=mwidth//len(os.listdir('.'))
mheight=mheight//len(os.listdir('.'))

for file in os.listdir('.'):
    if(file.endswith(".jpg") or file.endswith(".jpeg")):
        img=cv2.imread(os.path.join(path,file))
        resize=cv2.resize(img,(mwidth,mheight))
        cv2.imwrite(file, resize)

def generateVideo():

    image=[]
    for file in os.listdir('.'):
        if(file.endswith(".jpg") or file.endswith(".jpeg")):
            image.append(file)

    # print(len(image))

    
    os.chdir(r"C:\Users\aayus\Desktop\Udit data\New folder")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    frame=cv2.imread(os.path.join('.',image[0]))
    video = cv2.VideoWriter('video.avi', 0, 1, (frame.shape[1],frame.shape[0]))
    

    for images in image:
        video.write(cv2.imread(os.path.join('.',images)))

    cv2.destroyAllWindows()
    video.release()

generateVideo()

# mean_width = int(mean_width / num_of_images)
# mean_height = int(mean_height / num_of_images)


# for file in os.listdir('.'):
#     if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
#         # opening image using PIL Image
#         im = Image.open(os.path.join(path, file)) 
   
#         # im.size includes the height and width of image
#         width, height = im.size   
#         print(width, height)
  
#         # resizing 
#         imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS) 
#         imResize.save( file, 'JPEG', quality = 95) # setting quality
#         # printing each resized image name
#         print(im.filename.split('\\')[-1], " is resized") 

# def generate_video():
#     image_folder = '.' # make sure to use your folder
#     video_name = 'mygeneratedvideo.avi'
    
      
#     images = [img for img in os.listdir(image_folder)
#               if img.endswith(".jpg") or
#                  img.endswith(".jpeg") or
#                  img.endswith("png")]

#     print(images) 
  
#     frame = cv2.imread(os.path.join(image_folder, images[0]))
  
#     # setting the frame width, height width
#     # the width, height of first image
#     height, width, layers = frame.shape  
  
#     video = cv2.VideoWriter(video_name, 0, 1, (width, height)) 
  
#     # Appending the images to the video one by one
#     for image in images: 
#         video.write(cv2.imread(os.path.join(image_folder, image))) 
      
#     # Deallocating memories taken for window creation
#     cv2.destroyAllWindows() 
#     video.release()  # releasing the video generated

# generate_video()


    








