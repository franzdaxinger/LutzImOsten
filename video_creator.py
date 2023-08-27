import cv2
import numpy as np
import os
import time

# generate characters with https://avachara.com/avatar/

def prepare_file_structure(vid_path, restart):
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

def create_video(ws_path, vid_path):
    img = [cv2.imread(vid_path + f) for f in os.listdir(vid_path) if os.path.isfile(vid_path + f)]
    height,width,layers=img[1].shape
    video=cv2.VideoWriter(ws_path + 'video.avi', cv2.VideoWriter_fourcc(*'mp4v'), 6, (width,height))

    for j in range(len(img)):
        video.write(img[j])

    cv2.destroyAllWindows()
    video.release()

def add_image(img1_orig, img2_orig, pos, dim):
    img1 = img1_orig.copy()
    img2_raw = img2_orig.copy()
    img2 = cv2.resize(img2_raw, dim, interpolation = cv2.INTER_AREA)
    h, w = img2.shape[0],img2.shape[1]
    hh, ww = img1.shape[0], img1.shape[1]

    min_height = min(pos[0] + h, hh)
    min_width = min(pos[1] + w - 3, ww)

    img11 = img1[max(0, pos[0]):min_height, max(0, pos[1]):min_width]
    img22 = img2[-min(0, pos[0]):min_height-pos[0], -min(0, pos[1]):min_width-pos[1]]

    for i in range(len(img22)):
        for j in range(len(img22[0])):
            if (img22[i, j][0] == 222) and (img22[i, j][1] == 255) and (img22[i, j][2] == 229):
                img22[i, j] = img11[i, j]
    img1[max(0, pos[0]):min_height, max(0, pos[1]):min_width] = img22
    return img1


def main():
    ws_path = 'C:/Users/franz/Desktop/LUTZ!imOsten/Werbung/'
    vid_path = ws_path + 'vid/'

    franz = cv2.imread(ws_path + 'images/characters/franz/franz.png')
    franz_talking = cv2.imread(ws_path + 'images/characters/franz/franz_talking.png')
    franz_closed_eyes = cv2.imread(ws_path + 'images/characters/franz/franz_closed_eyes.png')
    franz_glasses = cv2.imread(ws_path + 'images/characters/franz/franz_glasses.png')
    franz_crazy = cv2.imread(ws_path + 'images/characters/franz/franz_crazy.png')

    philipp = cv2.imread(ws_path + 'images/characters/philipp/philipp.png')
    philipp_talking = cv2.imread(ws_path + 'images/characters/philipp/philipp_talking.png')
    philipp_closed_eyes = cv2.imread(ws_path + 'images/characters/philipp/philipp_closed_eyes.png')
    philipp_glasses = cv2.imread(ws_path + 'images/characters/philipp/philipp_glasses.png')
    philipp_crazy = cv2.imread(ws_path + 'images/characters/philipp/philipp_crazy.png')

    moose = cv2.imread(ws_path + 'images/characters/moose/moose.png')
    moose_talking = cv2.imread(ws_path + 'images/characters/moose/moose_talking.png')
    moose_closed_eyes = cv2.imread(ws_path + 'images/characters/moose/moose_closed_eyes.png')
    moose_glasses = cv2.imread(ws_path + 'images/characters/moose/moose_glasses.png')
    moose_crazy = cv2.imread(ws_path + 'images/characters/moose/moose_crazy.png')

    boesch = cv2.imread(ws_path + 'images/characters/boesch/boesch.png')
    boesch_talking = cv2.imread(ws_path + 'images/characters/boesch/boesch_talking.png')
    boesch_closed_eyes = cv2.imread(ws_path + 'images/characters/boesch/boesch_closed_eyes.png')
    boesch_glasses = cv2.imread(ws_path + 'images/characters/boesch/boesch_glasses.png')
    boesch_crazy = cv2.imread(ws_path + 'images/characters/boesch/boesch_crazy.png')

    marco = cv2.imread(ws_path + 'images/characters/marco/marco.png')
    marco_talking = cv2.imread(ws_path + 'images/characters/marco/marco_talking.png')
    marco_closed_eyes = cv2.imread(ws_path + 'images/characters/marco/marco_closed_eyes.png')
    marco_glasses = cv2.imread(ws_path + 'images/characters/marco/marco_glasses.png')
    marco_crazy = cv2.imread(ws_path + 'images/characters/marco/marco_crazy.png')

    cedi = cv2.imread(ws_path + 'images/characters/cedi/cedi.png')
    cedi_talking = cv2.imread(ws_path + 'images/characters/cedi/cedi_talking.png')
    cedi_closed_eyes = cv2.imread(ws_path + 'images/characters/cedi/cedi_closed_eyes.png')
    cedi_glasses = cv2.imread(ws_path + 'images/characters/cedi/cedi_glasses.png')
    cedi_crazy = cv2.imread(ws_path + 'images/characters/cedi/cedi_crazy.png')

    marie = cv2.imread(ws_path + 'images/characters/marie/marie.png')
    marie_talking = cv2.imread(ws_path + 'images/characters/marie/marie_talking.png')
    marie_closed_eyes = cv2.imread(ws_path + 'images/characters/marie/marie_closed_eyes.png')
    marie_glasses = cv2.imread(ws_path + 'images/characters/marie/marie_glasses.png')
    marie_crazy = cv2.imread(ws_path + 'images/characters/marie/marie_crazy.png')

    bruno = cv2.imread(ws_path + 'images/characters/bruno/bruno.png')
    bruno_talking = cv2.imread(ws_path + 'images/characters/bruno/bruno_talking.png')
    bruno_closed_eyes = cv2.imread(ws_path + 'images/characters/bruno/bruno_closed_eyes.png')
    bruno_glasses = cv2.imread(ws_path + 'images/characters/bruno/bruno_glasses.png')
    bruno_crazy = cv2.imread(ws_path + 'images/characters/bruno/bruno_crazy.png')

    jan = cv2.imread(ws_path + 'images/characters/jan/jan.png')
    jan_talking = cv2.imread(ws_path + 'images/characters/jan/jan_talking.png')
    jan_closed_eyes = cv2.imread(ws_path + 'images/characters/jan/jan_closed_eyes.png')
    jan_crazy = cv2.imread(ws_path + 'images/characters/jan/jan_crazy.png')

    kuehnis = cv2.imread(ws_path + 'images/characters/kuehnis/kuehnis.png')
    kuehnis_talking = cv2.imread(ws_path + 'images/characters/kuehnis/kuehnis_talking.png')
    kuehnis_closed_eyes = cv2.imread(ws_path + 'images/characters/kuehnis/kuehnis_closed_eyes.png')
    kuehnis_crazy = cv2.imread(ws_path + 'images/characters/kuehnis/kuehnis_crazy.png')

    dim_background = (1080, 1920)
    dim_character = (720, 1200)
    bandroom = cv2.resize(cv2.imread(ws_path + 'images/background/bandroom.png'), dim_background, interpolation = cv2.INTER_AREA)
    bar = cv2.resize(cv2.imread(ws_path + 'images/background/bar.png'), dim_background, interpolation = cv2.INTER_AREA)
    stage = cv2.resize(cv2.imread(ws_path + 'images/background/stage.png'), dim_background, interpolation = cv2.INTER_AREA)
    technobruno = cv2.resize(cv2.imread(ws_path + 'images/background/technobruno.png'), dim_background, interpolation = cv2.INTER_AREA)
    restart = True

    prepare_file_structure(vid_path, restart)

    '''# scene one
    idx_intro = 4
    idx_walking = 30
    idx_talking = 40

    for i in range(idx_intro):
        cv2.imwrite(vid_path + 'frame_' +str(i).zfill(5) + '.jpg', bandroom)

    for i in range(idx_walking):
        filename = vid_path + 'frame_' + str(i + idx_intro).zfill(5) + '.jpg'
        pos_philipp = (730, -560 + 31 * min(11, i))
        pos_cedi = (740, 920 - 25 * min(18 - 5, max(5, i) - 5))
        pos_franz = (720, -560 + 45 * min(23 - 10, max(10, i) - 10))
        pos_moose = (750, 920 - 46 * min(27 - 14, max(14, i) - 14))
        pos_boesch = (1900 - 75 * min(26 - 17, max(17, i) - 17), 220)
        pos_marco = (1900 - 78 * min(28 - 19, max(19, i) - 19), 550)

        image = add_image(bandroom, cedi, pos_cedi, dim_character)
        if i % 18 == 1:
            image = add_image(image, cedi_closed_eyes, pos_cedi, dim_character)
        image = add_image(image, philipp, pos_philipp, dim_character)
        if i % 16 == 0:
            image = add_image(image, philipp_closed_eyes, pos_philipp, dim_character)
        image = add_image(image, moose, pos_moose, dim_character)
        if i % 16 == 8:
            image = add_image(image, moose_closed_eyes, pos_moose, dim_character)
        image = add_image(image, franz, pos_franz, dim_character)
        if i % 18 == 5:
            image = add_image(image, franz_closed_eyes, pos_franz, dim_character)
        image = add_image(image, boesch, pos_boesch, dim_character)
        if i % 17 == 12:
            image = add_image(image, boesch_closed_eyes, pos_boesch, dim_character)
        image = add_image(image, marco, pos_marco, dim_character)
        if i % 14 == 9:
            image = add_image(image, marco_closed_eyes, pos_marco, dim_character)

        cv2.imwrite(filename, image)

    for i in range(idx_talking):
        filename = vid_path + 'frame_' + str(i + idx_intro + idx_walking).zfill(5) + '.jpg'
        pos_philipp = (730, -560 + 31 * min(11, idx_walking - 1))
        pos_cedi = (740, 920 - 25 * min(18 - 5, max(5, idx_walking - 1) - 5))
        pos_franz = (720, -560 + 45 * min(23 - 10, max(10, idx_walking - 1) - 10))
        pos_moose = (750, 920 - 46 * min(27 - 14, max(14, idx_walking - 1) - 14))
        pos_boesch = (1900 - 75 * min(26 - 17, max(17, idx_walking - 1) - 17), 220)
        pos_marco = (1900 - 78 * min(28 - 19, max(19, idx_walking - 1) - 19), 550)

        franz_talk_end = 21
        answer_start = 24
        answer_end = 31
        crazy_start = 34

        image = add_image(bandroom, cedi, pos_cedi, dim_character)
        if i % 18 == 1:
            image = add_image(image, cedi_closed_eyes, pos_cedi, dim_character)
        if (i > answer_start) and (i < answer_end):
            if i % 6 < 3:
                image = add_image(image, cedi_talking, pos_cedi, dim_character)
        if i > crazy_start:
            image = add_image(image, cedi_crazy, pos_cedi, dim_character)

        image = add_image(image, philipp, pos_philipp, dim_character)
        if i % 16 == 0:
            image = add_image(image, philipp_closed_eyes, pos_philipp, dim_character)
        if (i > answer_start) and (i < answer_end):
            if i % 6 < 4:
                image = add_image(image, philipp_talking, pos_philipp, dim_character)
        if i > crazy_start:
            image = add_image(image, philipp_crazy, pos_philipp, dim_character)

        image = add_image(image, moose, pos_moose, dim_character)
        if i % 16 == 8:
            image = add_image(image, moose_closed_eyes, pos_moose, dim_character)
        if (i > answer_start) and (i < answer_end):
            if i % 6 < 4:
                image = add_image(image, moose_talking, pos_moose, dim_character)
        if i > crazy_start:
            image = add_image(image, moose_crazy, pos_moose, dim_character)

        image = add_image(image, franz, pos_franz, dim_character)
        if i % 18 == 5:
            image = add_image(image, franz_closed_eyes, pos_franz, dim_character)
        if (i > 0) and (i < franz_talk_end):
            if i % 6 < 4:
                image = add_image(image, franz_talking, pos_franz, dim_character)
        if i > crazy_start:
            image = add_image(image, franz_crazy, pos_franz, dim_character)

        image = add_image(image, boesch, pos_boesch, dim_character)
        if i % 17 == 12:
            image = add_image(image, boesch_closed_eyes, pos_boesch, dim_character)
        if (i > answer_start) and (i < answer_end):
            if i % 6 < 3:
                image = add_image(image, boesch_talking, pos_boesch, dim_character)
        if i > crazy_start:
            image = add_image(image, boesch_crazy, pos_boesch, dim_character)

        image = add_image(image, marco, pos_marco, dim_character)
        if i % 14 == 9:
            image = add_image(image, marco_closed_eyes, pos_marco, dim_character)
        if (i > answer_start) and (i < answer_end):
            if i % 6 < 5:
                image = add_image(image, marco_talking, pos_marco, dim_character)
        if i > crazy_start:
            image = add_image(image, marco_crazy, pos_marco, dim_character)
        cv2.imwrite(filename, image)'''

    # scene three
    idx_intro = 0
    idx_walking = 20
    idx_talking = 30

    for i in range(idx_intro):
        cv2.imwrite(vid_path + 'frame_' +str(i).zfill(5) + '.jpg', technobruno)

    for i in range(idx_walking):
        filename = vid_path + 'frame_' + str(i + idx_intro).zfill(5) + '.jpg'
        pos_philipp = (740, -560 + 46 * min(15, i))
        pos_franz = (720, -560 + 45 * min(17 - 10, max(10, i) - 10))
        pos_bruno = (720, 515)

        image = add_image(technobruno, bruno, pos_bruno, dim_character)
        if i % 15 == 1:
            image = add_image(image, bruno_closed_eyes, pos_bruno, dim_character)
        image = add_image(image, philipp, pos_philipp, dim_character)
        if i % 16 == 8:
            image = add_image(image, philipp_closed_eyes, pos_philipp, dim_character)
        image = add_image(image, franz, pos_franz, dim_character)
        if i % 15 == 6:
            image = add_image(image, franz_closed_eyes, pos_franz, dim_character)

        cv2.imwrite(filename, image)

    ''''# scene four
    idx_intro = 0
    idx_walking = 20
    idx_talking = 30

    for i in range(idx_intro):
        cv2.imwrite(vid_path + 'frame_' +str(i).zfill(5) + '.jpg', technobruno)

    for i in range(idx_walking):
        filename = vid_path + 'frame_' + str(i + idx_intro).zfill(5) + '.jpg'
        pos_philipp = (740, -560 + 46 * min(15, i))
        pos_franz = (720, -560 + 45 * min(17 - 10, max(10, i) - 10))
        pos_bruno = (720, 515)

        image = add_image(technobruno, bruno, pos_bruno, dim_character)
        if i % 15 == 1:
            image = add_image(image, bruno_closed_eyes, pos_bruno, dim_character)
        image = add_image(image, philipp, pos_philipp, dim_character)
        if i % 16 == 8:
            image = add_image(image, philipp_closed_eyes, pos_philipp, dim_character)
        image = add_image(image, franz, pos_franz, dim_character)
        if i % 15 == 6:
            image = add_image(image, franz_closed_eyes, pos_franz, dim_character)

        cv2.imwrite(filename, image)

    for i in range(idx_talking):
        filename = vid_path + 'frame_' + str(i + idx_intro + idx_walking).zfill(5) + '.jpg'
        pos_philipp = (740, -560 + 46 * min(15, idx_walking - 1))
        pos_franz = (720, -560 + 45 * min(17 - 10, max(10, idx_walking - 1) - 10))
        pos_bruno = (720, 515)

        talk_end = 13
        answer_start = 16
        answer_end = 23
        crazy_start = 25

        image = add_image(technobruno, bruno, pos_bruno, dim_character)
        if i % 15 == 1:
            image = add_image(image, bruno_closed_eyes, pos_bruno, dim_character)
        if (i > answer_start) and (i < answer_end):
            if i % 6 < 4:
                image = add_image(image, bruno_talking, pos_bruno, dim_character)
        if i > crazy_start:
            image = add_image(image, bruno_crazy, pos_bruno, dim_character)

        image = add_image(image, philipp, pos_philipp, dim_character)
        if i % 16 == 8:
            image = add_image(image, philipp_closed_eyes, pos_philipp, dim_character)
        if (i > 0) and (i < talk_end):
            if i % 6 < 4:
                image = add_image(image, philipp_talking, pos_philipp, dim_character)
        if i > crazy_start:
            image = add_image(image, philipp_crazy, pos_philipp, dim_character)

        image = add_image(image, franz, pos_franz, dim_character)
        if i % 15 == 6:
            image = add_image(image, franz_closed_eyes, pos_franz, dim_character)
        if i > crazy_start:
            image = add_image(image, franz_crazy, pos_franz, dim_character)

        cv2.imwrite(filename, image)'''

    create_video(ws_path, vid_path)

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed time: ", elapsed_time)
