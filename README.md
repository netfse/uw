# underwater

Imported libraries:
pyautogui
opencv-python
argparse
pupil_apriltags

Files:
1. main.py
2. videoCapture.py
3. webcamVideoStream.py
4. fps.py
5. getArgs.py
6. aprilTagsCapture.py
7. drawTags.py
8. straightLineCapture.py

Controller:
press keys to switch modes

"ESC" : close camera
"1" : normal mode
"2" : apriltags detection mode
"3" : straight line detection mode

Modes:
normal mode (finished)
apriltags detection mode (developing)
straight lines detection mode (developing)

Problems we faced:
1. File path is too long, error: [winerror 206] the filename or extension is too long pupil_apriltags
2. extensive CPU usage for aprilTagsCapture
3. WRN: Matrix is singular.
4. VM - Fault hit memory shortage

Plans:
1. underwater image enhancement
2. straight line detection
3. denoising frame for detecting ROV

Personal notes:
- weak red color + receive blue and green color
- light levels (indoor light vs outdoor light)
- noisy
- fps
