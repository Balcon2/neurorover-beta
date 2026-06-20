"""
Servo control using PCA9685.
Run: python src/servo.py
"""
from time import sleep

try:
    import board, busio
    from adafruit_pca9685 import PCA9685
    from adafruit_motor import servo
except Exception:
    board = busio = PCA9685 = servo = None

try:
    from config import MOCK_HARDWARE, SERVO_CHANNEL, SERVO_MIN_ANGLE, SERVO_MAX_ANGLE
except ImportError:
    from .config import MOCK_HARDWARE, SERVO_CHANNEL, SERVO_MIN_ANGLE, SERVO_MAX_ANGLE


class ServoController:
    def __init__(self):
        self.mock = MOCK_HARDWARE or board is None or PCA9685 is None or servo is None
        self.camera_servo = None
        if self.mock:
            print("[MOCK] servo initialized")
            return
        i2c = busio.I2C(board.SCL, board.SDA)
        self.pca = PCA9685(i2c)
        self.pca.frequency = 50
        self.camera_servo = servo.Servo(self.pca.channels[SERVO_CHANNEL])

    def set_angle(self, angle):
        angle = max(SERVO_MIN_ANGLE, min(SERVO_MAX_ANGLE, angle))
        if self.mock:
            print(f"[MOCK] servo angle {angle}")
        else:
            self.camera_servo.angle = angle


if __name__ == "__main__":
    s = ServoController()
    for angle in [45, 90, 135, 90]:
        s.set_angle(angle)
        sleep(1)
