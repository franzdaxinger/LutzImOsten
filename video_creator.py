import cv2
import numpy as np
import os

# generate characters with https://avachara.com/avatar/

def create_video(vid_path):
    img = [cv2.imread(vid_path + f) for f in os.listdir(vid_path) if os.path.isfile(vid_path + f)]
    height,width,layers=img[1].shape
    video=cv2.VideoWriter(ws_path + 'video.avi', cv2.VideoWriter_fourcc(*'mp4v'), 6, (width,height))

    for j in range(len(img)):
        video.write(img[j])

    cv2.destroyAllWindows()
    video.release()

def add_image(img1_orig, img2_orig, pos):
    img1 = img1_orig.copy()
    img2 = img2_orig.copy()
    h, w = img2.shape[0],franz_open_mouth.shape[1]
    hh, ww = img1.shape[0], img1.shape[1]

    min_height = min(pos[0] + h, hh)
    min_width = min(pos[1] + w - 1, ww)

    img11 = img1[max(0, pos[0]):min_height, max(0, pos[1]):min_width]
    img22 = img2[-min(0, pos[0]):min_height-pos[0], -min(0, pos[1]):min_width-pos[1]]

    for i in range(len(img22)):
        for j in range(len(img22[0])):
            if (img22[i, j][0] == 222) and (img22[i, j][1] == 255) and (img22[i, j][2] == 229):
                img22[i, j] = img11[i, j]
    img1[max(0, pos[0]):min_height, max(0, pos[1]):min_width] = img22
    return img1

ws_path = 'C:/Users/franz/Desktop/LUTZ!imOsten/Werbung/'
vid_path = ws_path + 'vid/'
franz_open_mouth = cv2.imread(ws_path + 'images/franz/franz_talking.png')
franz_closed_mouth = cv2.imread(ws_path + 'images/franz/franz_closed_mouth.png')
franz_closed_eyes = cv2.imread(ws_path + 'images/franz/franz_closed_eyes.png')
bandroom = cv2.imread(ws_path + 'images/background/bandroom.png')
dimension = (1080, 1920)
restart = False


if not os.path.exists(vid_path):
    os.mkdir(vid_path)
if restart:
    try:
        files = os.listdir(vid_path)
        for file in files:
            file_path = os.path.join(vid_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except OSError:
        print("Error occurred while deleting files.")

result = bandroom.copy()
forrest = cv2.resize(result, dimension, interpolation = cv2.INTER_AREA)

cv2.imwrite(vid_path + 'frame_' +str(0).zfill(5) + '.jpg', forrest)
cv2.imwrite(vid_path + 'frame_' +str(1).zfill(5) + '.jpg', forrest)

for i in range(30):
    filename = vid_path + 'frame_' + str(i + 2).zfill(5) + '.jpg'
    position = (1150, -300 + 20*i)
    image = add_image(forrest, franz_closed_mouth, position)
    if i % 8 == 0:
        image = add_image(forrest, franz_closed_eyes, position)
    cv2.imwrite(filename, image)

for i in range(30):
    filename = vid_path + 'frame_' + str(i + 32).zfill(5) + '.jpg'
    position = (1150, 300)
    image = add_image(forrest, franz_closed_mouth, position)
    if i % 8 == 0:
        image = add_image(forrest, franz_closed_eyes, position)
    if (i % 3 == 0) or (i % 4 == 0):
        image = add_image(forrest, franz_open_mouth, position)
    cv2.imwrite(filename, image)

create_video(vid_path)
