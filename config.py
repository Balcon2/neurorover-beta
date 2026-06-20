"""
NeuroRover Beta configuration.
Check every GPIO pin before wiring real hardware.
"""
MOCK_HARDWARE = False

STBY_PIN = 25

LEFT_FRONT = {"pwm": 18, "in1": 12, "in2": 16}
LEFT_REAR = {"pwm": 19, "in1": 20, "in2": 21}
RIGHT_FRONT = {"pwm": 13, "in1": 5, "in2": 6}
RIGHT_REAR = {"pwm": 22, "in1": 26, "in2": 27}

HC_SR04_TRIG = 23
HC_SR04_ECHO = 24

OBSTACLE_STOP_CM = 20
AI_MIN_CONFIDENCE = 0.60

CAMERA_INDEX = 0
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

SERVO_CHANNEL = 0
SERVO_MIN_ANGLE = 0
SERVO_MAX_ANGLE = 180
