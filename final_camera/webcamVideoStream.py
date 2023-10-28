from threading import Thread, Lock
import cv2

class WebcamVideoStream:
	def __init__(self, src=0, w=600, h=600, name="WebcamVideoStream"):
		self.stream = cv2.VideoCapture(src)
		if not self.stream.isOpened():
			raise ValueError("Could not open video stream")
		self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, w)
		self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
		(self.grabbed, self.frame) = self.stream.read()
		if not self.grabbed:
			raise ValueError("Could not read frame from video stream")
		self.name = name
		self.stopped = False
		self.lock = Lock()

	def start(self):
		t = Thread(target=self.update, name=self.name, args=())
		t.daemon = True
		t.start()
		return self

	def update(self):
		while True:
			if self.stopped:
				return
			
			self.grabbed, frame = self.stream.read()
			with self.lock:
				self.frame = frame

	def read(self):
		return self.frame

	def stop(self):
		self.stopped = True

	def __del__(self):
		self.stop()
		self.stream.release()
