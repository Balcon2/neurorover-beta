"""
Sensor helpers for VL53L1X, HC-SR04, and MPU6050.
Run: python src/sensors.py
"""
from time import sleep

try:
    import board, busio
    import adafruit_vl53l1x
    import adafruit_mpu6050
except Exception:
    board = busio = adafruit_vl53l1x = adafruit_mpu6050 = None

try:
    from gpiozero import DistanceSensor
except Exception:
    DistanceSensor = None

try:
    from config import MOCK_HARDWARE, HC_SR04_TRIG, HC_SR04_ECHO
except ImportError:
    from .config import MOCK_HARDWARE, HC_SR04_TRIG, HC_SR04_ECHO


class Sensors:
    def __init__(self):
        self.mock = MOCK_HARDWARE
        self.tof = None
        self.imu = None
        self.ultrasonic = None

        if self.mock:
            print("[MOCK] sensors initialized")
            return

        if board and busio:
            try:
                i2c = busio.I2C(board.SCL, board.SDA)
                if adafruit_vl53l1x:
                    self.tof = adafruit_vl53l1x.VL53L1X(i2c)
                    self.tof.distance_mode = 1
                    self.tof.timing_budget = 50
                    self.tof.start_ranging()
                if adafruit_mpu6050:
                    self.imu = adafruit_mpu6050.MPU6050(i2c)
            except Exception as e:
                print(f"[WARN] I2C init failed: {e}")

        if DistanceSensor:
            try:
                self.ultrasonic = DistanceSensor(echo=HC_SR04_ECHO, trigger=HC_SR04_TRIG, max_distance=2.0)
            except Exception as e:
                print(f"[WARN] HC-SR04 init failed: {e}")

    def read_tof_cm(self):
        if self.mock:
            return 100
        if self.tof is None:
            return None
        try:
            if self.tof.data_ready:
                value = self.tof.distance
                self.tof.clear_interrupt()
                return value
        except Exception as e:
            print(f"[WARN] ToF read failed: {e}")
        return None

    def read_ultrasonic_cm(self):
        if self.mock:
            return 100
        if self.ultrasonic is None:
            return None
        try:
            return self.ultrasonic.distance * 100
        except Exception as e:
            print(f"[WARN] ultrasonic read failed: {e}")
            return None

    def read_distance_cm(self):
        return self.read_tof_cm() or self.read_ultrasonic_cm()

    def read_imu(self):
        if self.mock:
            return {"acceleration": (0, 0, 0), "gyro": (0, 0, 0), "temperature": 25}
        if self.imu is None:
            return None
        return {"acceleration": self.imu.acceleration, "gyro": self.imu.gyro, "temperature": self.imu.temperature}


if __name__ == "__main__":
    s = Sensors()
    while True:
        print("distance cm:", s.read_distance_cm(), "imu:", s.read_imu())
        sleep(0.5)
