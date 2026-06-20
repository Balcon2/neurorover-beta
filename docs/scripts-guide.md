# Starter Scripts Guide

Recommended test order:

1. `src/motor.py`
2. `src/camera.py`
3. `src/sensors.py`
4. `src/servo.py`
5. `src/manual_control.py`
6. `src/autopilot.py`
7. `ml/collect_data.py`
8. `ml/train_model.py`
9. `ml/convert_tflite.py`

Safety:
- Test motors with wheels lifted.
- Keep emergency stop reachable.
- Never connect 7.4V directly to Raspberry Pi.
- HC-SR04 ECHO needs voltage divider before GPIO24.
- All GND must be common.
