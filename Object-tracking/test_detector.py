import cv2
from frame_detector import LiveDetector


class Test:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.video_capture.set(3, 960)
        self.video_capture.set(4, 540)
        self.video_capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
        self.detector = LiveDetector()

    def run(self):
        while True:
            ret, frame = self.video_capture.read()

            outputImg = self.detector.track_objects(frame)

            yield outputImg