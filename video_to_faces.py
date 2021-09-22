import cv2
import sys
import os

def video_to_frames(input_file, num_frames=50, step=10):

    counter = 0
    acc = 0
    # read first frame
    vidcap = cv2.VideoCapture(input_file)
    success, image = vidcap.read()

    frames = []

    # write output and extract more frames
    while success:
        if acc % 5 == 0:
            cv2.imwrite((output_file) % counter, image)
            counter += 1
            if(counter >= num_frames):
                break
                
        success, image = vidcap.read()
        acc += 1
        # break after reading enough frames
        
    print('successfully read %d frames' % counter)

def video_to_faces(input_file):
    video_to_frames

if __name__ == '__main__':
    input_file = sys.argv[1]
    video_to_faces(input_file)