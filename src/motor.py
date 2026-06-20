"""
Motor control for NeuroRover Beta.
Uses 2x TB6612FNG motor drivers and 4x N20 motors.
Run: python src/motor.py
"""
from time import sleep

try:
    from gpiozero import DigitalOutputDevice, PWMOutputDevice
except Exception:
    DigitalOutputDevice = None
    PWMOutputDevice = None

try:
    from config import MOCK_HARDWARE, STBY_PIN, LEFT_FRONT, LEFT_REAR, RIGHT_FRONT, RIGHT_REAR
except ImportError:
    from .config import MOCK_HARDWARE, STBY_PIN, LEFT_FRONT, LEFT_REAR, RIGHT_FRONT, RIGHT_REAR


class Motor:
    def __init__(self, name: str, pwm_pin: int, in1_pin: int, in2_pin: int):
        self.name = name
        self.mock = MOCK_HARDWARE or DigitalOutputDevice is None or PWMOutputDevice is None
        if self.mock:
            self.pwm = self.in1 = self.in2 = None
            print(f"[MOCK] Motor {name}: PWM={pwm_pin}, IN1={in1_pin}, IN2={in2_pin}")
        else:
            self.pwm = PWMOutputDevice(pwm_pin, frequency=1000)
            self.in1 = DigitalOutputDevice(in1_pin)
            self.in2 = DigitalOutputDevice(in2_pin)

    def set_speed(self, speed: float):
        speed = max(-1.0, min(1.0, speed))
        if self.mock:
            print(f"[MOCK] {self.name} speed {speed:.2f}")
            return

        if speed > 0:
            self.in1.on()
            self.in2.off()
            self.pwm.value = speed
        elif speed < 0:
            self.in1.off()
            self.in2.on()
            self.pwm.value = abs(speed)
        else:
            self.stop()

    def stop(self):
        if self.mock:
            print(f"[MOCK] {self.name} stop")
            return
        self.pwm.value = 0
        self.in1.off()
        self.in2.off()


class DriveBase:
    def __init__(self):
        self.mock = MOCK_HARDWARE or DigitalOutputDevice is None
        if self.mock:
            self.stby = None
            print(f"[MOCK] STBY pin {STBY_PIN}")
        else:
            self.stby = DigitalOutputDevice(STBY_PIN)
            self.stby.on()

        self.left_front = Motor("left_front", LEFT_FRONT["pwm"], LEFT_FRONT["in1"], LEFT_FRONT["in2"])
        self.left_rear = Motor("left_rear", LEFT_REAR["pwm"], LEFT_REAR["in1"], LEFT_REAR["in2"])
        self.right_front = Motor("right_front", RIGHT_FRONT["pwm"], RIGHT_FRONT["in1"], RIGHT_FRONT["in2"])
        self.right_rear = Motor("right_rear", RIGHT_REAR["pwm"], RIGHT_REAR["in1"], RIGHT_REAR["in2"])

    def enable(self):
        if self.mock:
            print("[MOCK] drive enabled")
        else:
            self.stby.on()

    def disable(self):
        self.stop()
        if self.mock:
            print("[MOCK] drive disabled")
        else:
            self.stby.off()

    def set_left_right(self, left_speed: float, right_speed: float):
        self.left_front.set_speed(left_speed)
        self.left_rear.set_speed(left_speed)
        self.right_front.set_speed(right_speed)
        self.right_rear.set_speed(right_speed)

    def forward(self, speed=0.45):
        self.set_left_right(speed, speed)

    def backward(self, speed=0.35):
        self.set_left_right(-speed, -speed)

    def left(self, speed=0.35):
        self.set_left_right(-speed, speed)

    def right(self, speed=0.35):
        self.set_left_right(speed, -speed)

    def stop(self):
        self.left_front.stop()
        self.left_rear.stop()
        self.right_front.stop()
        self.right_rear.stop()


if __name__ == "__main__":
    drive = DriveBase()
    try:
        print("forward")
        drive.forward(0.35)
        sleep(1)
        print("left")
        drive.left(0.30)
        sleep(1)
        print("right")
        drive.right(0.30)
        sleep(1)
        print("backward")
        drive.backward(0.30)
        sleep(1)
    finally:
        drive.stop()
        print("finished")
