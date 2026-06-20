"""
Camera helper.
Run: python src/camera.py
"""
import cv2

try:
    from config import CAMERA_INDEX, CAMERA_WIDTH, CAMERA_HEIGHT
except ImportError:
    from .config import CAMERA_INDEX, CAMERA_WIDTH, CAMERA_HEIGHT


class RobotCamera:
    def __init__(self, index=CAMERA_INDEX, width=CAMERA_WIDTH, height=CAMERA_HEIGHT):
        self.cap = cv2.VideoCapture(index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        if not self.cap.isOpened():
            print("[WARN] camera could not be opened")

    def read(self):
        ok, frame = self.cap.read()
        return frame if ok else None

    def release(self):
        self.cap.release()


if __name__ == "__main__":
    cam = RobotCamera()
    while True:
        frame = cam.read()
        if frame is None:
            break
        cv2.imshow("NeuroRover Camera Test", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cam.release()
    cv2.destroyAllWindows()
