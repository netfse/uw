from __future__ import print_function
from getArgs import getArgs
from webcamVideoStream import WebcamVideoStream
from fps import FPS

from aprilTagsCapture import aprilTagsCapture
from straightLineCapture import straightLineCapture

import time
import copy
import cv2

key_actions = {
    ord('1'): 0,
    ord('2'): 1,
    ord('3'): 2,
}

controller_key_actions = {
    ord('1'): 0,
    ord('2'): 1,
    ord('3'): 2,
}

def textMode(frame, text):
    cv2.putText(frame,
                text,
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
                cv2.LINE_AA)
    
def process_frame(frame, mode):
    if mode == 1:
        processed_frame = aprilTagsCapture(frame)
        textMode(processed_frame, "AT Mode")
    elif mode == 2:
        processed_frame = straightLineCapture(frame)
        textMode(processed_frame, "SL Mode")
    else:
        processed_frame = copy.deepcopy(frame)
        textMode(processed_frame, "N Mode")
    return processed_frame


def videoCapture():
    args = getArgs()

    elapsed_time = 0
    delay_time = .001
    mode = 0
    
    try:
        cap = WebcamVideoStream(src=args.device, w=args.width, h=args.height).start()
    except Exception as e:
        print(f"Error starting video stream: {e}")
        return
    
    fps = FPS().start()

    while True:
        start_time = time.time()
        frame = cap.read()

        cv2.putText(frame,
                    "elisped time: {:.5f}".format(elapsed_time),
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
                    cv2.LINE_AA)

        time.sleep(delay_time)

        processed_frame = process_frame(frame, mode)
        cv2.imshow('Underwater_screen', processed_frame)

        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break
        elif key in key_actions:
            mode = key_actions[key]

        fps.update()
        elapsed_time = time.time() - start_time

    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    cv2.destroyAllWindows()
    cap.stop()
