import os
import cv2

path="Images"

Images=[]

list_of_files=os.listdir(path)

for i in list_of_files:
    name,extension=os.path.splitext(i)
    # print(i)
    # print(extension)
    # print(name)

    if extension in['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name=path+"/"+i
        # print(file_name)
        Images.append(file_name)
        # print(len(Images))

count=len(Images)
frame = cv2.imread(Images[0])
print(frame.shape)
height,width,channel=frame.shape
size=(width,height)
print(size)

output=cv2.VideoWriter("Gid.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)
    
for i in range(0,count):
    myframe=cv2.imread(Images[i])
    output.write(myframe)

    

output.release()
print("done")