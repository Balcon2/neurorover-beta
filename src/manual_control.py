"""
Manual control.
Run: python src/manual_control.py
Keys: w/a/s/d, space, q
"""
from time import sleep

try:
    import keyboard
except Exception:
    keyboard = None

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
    print("Manual control: W/A/S/D, SPACE stop, Q quit")

    try:
        while True:
            if safety.check_and_stop_if_needed():
                sleep(0.1)
                continue

            if keyboard:
                if keyboard.is_pressed("w"):
                    drive.forward()
                elif keyboard.is_pressed("s"):
                    drive.backward()
                elif keyboard.is_pressed("a"):
                    drive.left()
                elif keyboard.is_pressed("d"):
                    drive.right()
                elif keyboard.is_pressed("space"):
                    drive.stop()
                elif keyboard.is_pressed("q"):
                    break
            else:
                key = input("w/a/s/d/space/q: ").strip().lower()
                if key == "w":
                    drive.forward()
                elif key == "s":
                    drive.backward()
                elif key == "a":
                    drive.left()
                elif key == "d":
                    drive.right()
                elif key in ["space", ""]:
                    drive.stop()
                elif key == "q":
                    break

            sleep(0.05)
    finally:
        drive.stop()


if __name__ == "__main__":
    main()
