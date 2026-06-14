# NeuroRover Beta

NeuroRover Beta is a Raspberry Pi 4 based AI robot car project.
The goal is to build a small self-driving robot that can use a camera, sensors, motor control, and later machine learning to drive safely.

This is not a real Level 5 autonomous car. It is a learning project for robotics, electronics, Python, computer vision, and AI.

## Features

* Raspberry Pi 4 as the main computer
* Raspberry Pi Camera Module for vision
* 4 N20 DC gear motors with encoders
* 2 TB6612FNG motor drivers
* VL53L1X ToF distance sensor
* HC-SR04 ultrasonic sensor
* MPU6050 IMU sensor
* PCA9685 servo driver
* SG90 servo motor
* 2S LiPo battery power system
* Emergency stop switch
* Main power switch
* Future support for OpenCV and machine learning

## Project Goals

The project will be built in versions:

### Version 1

Manual driving with keyboard or controller.

### Version 2

Obstacle detection and automatic stop.

### Version 3

Camera test and simple OpenCV vision.

### Version 4

Line following or basic autonomous driving.

### Version 5

Machine learning based driving using collected camera data.

### Version 6

Optional LLM control for voice/text commands.

## Hardware

Main parts:

* Raspberry Pi 4 Model B
* Raspberry Pi Camera Module
* 4x N20 DC gear motors with encoders
* 2x TB6612FNG motor drivers
* VL53L1X ToF distance sensor
* HC-SR04 ultrasonic sensor
* MPU6050 IMU
* PCA9685 servo driver
* SG90 servo
* 7.4V 2S LiPo battery
* 5V 5A buck converter
* Emergency stop switch
* Main power switch
* Jumper wires
* M2.5 and M3 screws
* Custom CAD chassis

## Power Architecture

The 7.4V 2S LiPo battery powers the robot.

Battery positive goes through:

1. Emergency stop switch
2. Main power switch

After the switches, the battery rail powers:

* TB6612FNG motor driver VM inputs
* 5V buck converter input

The buck converter outputs 5V for:

* Raspberry Pi
* PCA9685 servo power
* HC-SR04 VCC
* other 5V modules if required

The Raspberry Pi 3.3V rail powers:

* I2C sensor logic
* PCA9685 logic VCC

All GND connections must be common.

## Important Safety Notes

* Never connect 7.4V directly to the Raspberry Pi.
* Never connect HC-SR04 ECHO directly to Raspberry Pi GPIO.
* Use a voltage divider for HC-SR04 ECHO.
* All GND connections must be connected together.
* Use thicker wires for battery and motor power.
* Use jumper wires only for signal and sensor connections.
* Test motors with the robot lifted off the ground.
* Always keep the emergency stop switch reachable.
* LiPo batteries must be charged with a proper 2S LiPo balance charger.

## Wiring Overview

Basic system flow:

```text
Camera / Sensors → Raspberry Pi → Motor Drivers → Motors
```

Power flow:

```text
2S LiPo Battery → Emergency Stop → Power Switch → Motor Drivers
                                           ↓
                                     Buck Converter → Raspberry Pi
```

I2C bus:

```text
Raspberry Pi GPIO2 SDA → VL53L1X SDA, MPU6050 SDA, PCA9685 SDA
Raspberry Pi GPIO3 SCL → VL53L1X SCL, MPU6050 SCL, PCA9685 SCL
```

HC-SR04:

```text
TRIG → Raspberry Pi GPIO23
ECHO → Voltage divider → Raspberry Pi GPIO24
```

Camera:

```text
Raspberry Pi Camera Module → Raspberry Pi CSI camera port
```

## Software Plan

Suggested project structure:

```text
neurorover-v1/
├── README.md
├── docs/
├── cad/
├── kicad/
├── src/
│   ├── main.py
│   ├── motor.py
│   ├── sensors.py
│   ├── camera.py
│   ├── servo.py
│   ├── autopilot.py
│   └── config.py
├── data/
├── models/
└── requirements.txt
```

## Setup

Install basic packages on Raspberry Pi:

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-pip python3-opencv git
```

Install Python libraries:

```bash
pip install numpy opencv-python
```

More libraries will be added later depending on the sensors and AI model.

## Development Order

Recommended build order:

1. Build the CAD chassis.
2. Mount motors and wheels.
3. Set up battery, switch, emergency stop, and buck converter.
4. Test Raspberry Pi power.
5. Test camera.
6. Test one motor.
7. Test all motors.
8. Test distance sensor.
9. Add manual driving.
10. Add safety stop.
11. Add OpenCV camera vision.
12. Collect driving data.
13. Train a machine learning model.
14. Add optional LLM control.

## Machine Learning Idea

The first machine learning version will use imitation learning.

The robot stores:

```text
camera image + driving command
```

Example:

```text
image_001.jpg → forward
image_002.jpg → left
image_003.jpg → right
image_004.jpg → stop
```

A small model can then learn:

```text
camera image → driving decision
```

Training should be done on a PC or laptop.
The Raspberry Pi should only run the trained model.

## Status

Current project state:

* Hardware planning
* Wiring planning
* CAD chassis planning
* KiCad starter schematic planning

## License

This project is for learning and personal use.
A license can be added later.
