"""
Simple safe autopilot without ML.
Run: python src/autopilot.py
"""
from time import sleep

try:
    from motor import DriveBase
    from sensors import Sensors
    from safety import SafetySystem
except ImportError:
    from .motor import DriveBase
    from .sensors import Sensors
    from .safety import SafetySystem


def main():
    drive = DriveBase()
    sensors = Sensors()
    safety = SafetySystem(drive, sensors)

    try:
        while True:
            if safety.check_and_stop_if_needed():
                sleep(0.2)
                continue
            drive.forward(0.30)
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        drive.stop()


if __name__ == "__main__":
    main()
