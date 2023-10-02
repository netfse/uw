from __future__ import print_function
from webcamVideoStream import WebcamVideoStream
from fps import FPS

from aprilTagsCapture import aprilTagsCapture
from straightLineCapture import straightLineCapture

import time
import copy
import cv2

from getArgs import getArgs

def textMode(frame, text):
    cv2.putText(frame,
                text,
                (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
                cv2.LINE_AA)
    
def videoCapture():
    args = getArgs()

    current_fps = 0
    delay_time = .001
    mode = 0

    cap = WebcamVideoStream(src=args.device, w=args.width, h=args.height).start()
    fps = FPS().start()
   
    while True:
        start_time = time.time()
        frame = cap.read()

        cv2.putText(frame,
                   "{} fps".format(current_fps),
                   (10, 60), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
                   cv2.LINE_AA)
        
        time.sleep(delay_time)

        if mode == 1:
            apriltag_frame = aprilTagsCapture(frame)
            textMode(apriltag_frame, "AT Mode")
            cv2.imshow('Underwater_screen', apriltag_frame)
        elif mode == 2:
            straightLine_frame = straightLineCapture(frame)
            textMode(straightLine_frame, "SL Mode")
            cv2.imshow('Underwater_screen', straightLine_frame)
        else:
            normal_frame = copy.deepcopy(frame)
            textMode(normal_frame, "N Mode")
            cv2.imshow('Underwater_screen', normal_frame)

        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break
        elif key == ord('1'):
            mode = 0
        elif key == ord('2'):
            mode = 1
        elif key == ord('3'):
            mode = 2

        fps.update()
        current_fps = 1 // (time.time() - start_time)

    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    
    cv2.destroyAllWindows()
    cap.stop()