"""
Safety logic.
"""
try:
    from config import OBSTACLE_STOP_CM, AI_MIN_CONFIDENCE
except ImportError:
    from .config import OBSTACLE_STOP_CM, AI_MIN_CONFIDENCE


class SafetySystem:
    def __init__(self, drivebase, sensors=None):
        self.drivebase = drivebase
        self.sensors = sensors

    def obstacle_too_close(self):
        if self.sensors is None:
            return False
        distance = self.sensors.read_distance_cm()
        return distance is not None and distance < OBSTACLE_STOP_CM

    def check_and_stop_if_needed(self):
        if self.obstacle_too_close():
            print("[SAFETY] obstacle too close, stopping")
            self.drivebase.stop()
            return True
        return False

    def safe_ai_command(self, command, confidence):
        if confidence < AI_MIN_CONFIDENCE:
            return "stop"
        if command not in ["forward", "backward", "left", "right", "stop"]:
            return "stop"
        return command
