import cv2
import numpy as np

lower = np.array([100, 100, 100])
upper = np.array([140, 255, 255])

#lower = np.array([0, 0, 0])
#upper = np.array([180, 255, 50])

def straightLineCapture(frame):
    straightLine_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(straightLine_frame, lower, upper)
    mask_contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 500:
                x, y, w, h = cv2.boundingRect(mask_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    return frame
