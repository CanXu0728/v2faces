import cv2
import sys
import os 
# import dlib
import numpy as np
import argparse


### Extrate Faces from a given video
#   Input:
#       input_file: str, path to the video mp4 file
#       num_frames: int, maximum number of frames extracting
#       step: int, searching for faces per step_size frames
#       minSize: (int, int), minimum size of faces
#       eyes: boolean, if save eye images
def video_to_faces(input_file, num_frames=50, step=10, minSize=(28,28), eyes=False):
    counter = 0
    acc = 0

    # alternatively, use dlib face detector
    # detector = dlib.get_frontal_face_detector()

    # load face detector
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # load video file
    vc = cv2.VideoCapture(input_file)
    
    # check if video file successfully loaded
    if vc.isOpened():
        success, frame = vc.read()
    else:
        success = False


    while success:
        if acc % step == 0:

            # alternatively, use dlib face detector
            # detects = detector(frame, 1)
            # for i, face in enumerate(detects):
                # if eyes:
                    # vmid = int((face.top()+face.bottom())/2)
                    # hmid = int((face.left()+face.right())/2)
                    # imgleft = np.flip(frame[face.top():vmid, face.left():hmid], axis=1)
                    # imgright = frame[face.top():vmid, hmid:face.right()]

            # detect faces
            faces = detector.detectMultiScale(frame, minNeighbors=5, minSize=minSize)
            for (x, y, w, h) in faces:
                # save face image
                img = frame[y:y+h, x:x+w]
                save_path = input_file[:-4]+'_'+str(counter)+'.jpg'
                cv2.imwrite(save_path, img)

                if eyes: 
                    hmid = x + int(w/2)
                    vmid = y + int(h/2)
                    # flip left eye image to match with right eye image
                    imgleft = np.flip(frame[y:vmid, x:hmid], axis=1)
                    imgright = frame[y:vmid, hmid:x+w]
                
                    # save eye images
                    save_path_l = input_file[:-4]+'_'+str(counter)+'_left.jpg'
                    save_path_r = input_file[:-4]+'_'+str(counter)+'_right.jpg'
                    cv2.imwrite(save_path_l, imgleft)
                    cv2.imwrite(save_path_r, imgright)
                
                counter += 1
                if(counter >= num_frames):
                    # break after reading enough frames
                    break    

        success, frame = vc.read()
        acc += 1
    vc.release()
        
    print('successfully extract %d faces' % counter)

if __name__ == '__main__':
    input_file = sys.argv[1] # path to video
    try:
        eyes = sys.argv[2]
        if eyes == '-eyes':
            video_to_faces(input_file, eyes=True)
        else:
            print('Usage: video_path [-eyes]')
    except:
        video_to_faces(input_file)
        