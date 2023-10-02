import argparse
import pyautogui

def getArgs():
    parser = argparse.ArgumentParser()

    # WebcamVideoStream Settings
    parser.add_argument("-d", "--device", type=None, default=0)
    parser.add_argument("-wd", "--width", help='the size of the screen width', type=int, default=pyautogui.size()[0])
    parser.add_argument("-hg", "--height", help='the size of the screen height', type=int, default=pyautogui.size()[1])

    # WebcamVideoStream Settings
    parser.add_argument("--families", type=str, default='tag36h11')
    parser.add_argument("--nthreads", type=int, default=1)
    parser.add_argument("--quad_decimate", type=float, default=2.0)
    parser.add_argument("--quad_sigma", type=float, default=0.0)
    parser.add_argument("--refine_edges", type=int, default=1)
    parser.add_argument("--decode_sharpening", type=float, default=0.25)
    parser.add_argument("--debug", type=int, default=0)

    args = parser.parse_args()

    return args