import copy
import cv2

from pupil_apriltags import Detector
from getArgs import getArgs
from drawTags import drawTags

args = getArgs()

families = args.families
nthreads = args.nthreads
quad_decimate = args.quad_decimate
quad_sigma = args.quad_sigma
refine_edges = args.refine_edges
decode_sharpening = args.decode_sharpening
debug = args.debug

at_detector = Detector(
    families=families,
    nthreads=nthreads,
    quad_decimate=quad_decimate,
    quad_sigma=quad_sigma,
    refine_edges=refine_edges,
    decode_sharpening=decode_sharpening,
    debug=debug,
)

def aprilTagsCapture(frame):
    debug_frame = copy.deepcopy(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    tags = at_detector.detect(frame, 
                              estimate_tag_pose=False, 
                              camera_params=None, 
                              tag_size=None)
    
    debug_frame = drawTags(debug_frame, tags)
    return debug_frame

