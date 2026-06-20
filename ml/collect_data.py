"""
Collect training images.
Run: python ml/collect_data.py
"""
from pathlib import Path
import time
import cv2

DATA_DIR = Path("data/raw")
for label in ["forward", "left", "right", "stop"]:
    (DATA_DIR / label).mkdir(parents=True, exist_ok=True)

camera = cv2.VideoCapture(0)
print("W/A/D/SPACE save images. Q quits.")

while True:
    ok, frame = camera.read()
    if not ok:
        print("camera error")
        break

    cv2.imshow("Collect Data", frame)
    key = cv2.waitKey(1) & 0xFF

    label = None
    if key == ord("w"):
        label = "forward"
    elif key == ord("a"):
        label = "left"
    elif key == ord("d"):
        label = "right"
    elif key == ord(" "):
        label = "stop"
    elif key == ord("q"):
        break

    if label:
        path = DATA_DIR / label / f"{label}_{int(time.time() * 1000)}.jpg"
        cv2.imwrite(str(path), frame)
        print("saved", path)

camera.release()
cv2.destroyAllWindows()
