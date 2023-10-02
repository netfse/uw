# import the necessary packages
from threading import Thread
import cv2

class WebcamVideoStream:
	def __init__(self, src=0, w=600, h=600, name="WebcamVideoStream"):
		self.stream = cv2.VideoCapture(src)
		self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, w)
		self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
		(self.grabbed, self.frame) = self.stream.read()
		self.name = name
		self.stopped = False

	def start(self):
		t = Thread(target=self.update, name=self.name, args=())
		t.daemon = True
		t.start()
		return self

	def update(self):
		while True:
			if self.stopped:
				return
			
			(self.grabbed, self.frame) = self.stream.read()

	def read(self):
		return self.frame

	def stop(self):
		self.stopped = True
