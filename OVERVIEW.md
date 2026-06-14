Project Specification — NeuroRover Beta
Overview

NeuroRover V1 is a Raspberry Pi 4 based AI robot car using a Raspberry Pi Camera Module, four N20 DC gear motors with encoders, dual TB6612FNG motor drivers, VL53L1X ToF distance sensor, HC-SR04 ultrasonic sensor, MPU6050 IMU, PCA9685 servo driver, one SG90 servo, and 2S LiPo battery power.

Power Architecture
7.4V nominal 2S LiPo battery positive passes through emergency stop switch, then main power switch.
Switched battery rail feeds both TB6612FNG VM motor supplies and the 5V 5A buck converter input.
Buck converter output is 5V for Raspberry Pi 5V input, PCA9685 servo V+, HC-SR04 VCC, and module logic where required.
Raspberry Pi 3.3V rail supplies I2C sensor logic and PCA9685 VCC logic.
All grounds are common.

Logic and Interfaces
Raspberry Pi GPIO logic is 3.3V only.
I2C bus: GPIO2/SDA and GPIO3/SCL to VL53L1X, MPU6050, and PCA9685.
HC-SR04 TRIG from GPIO23; ECHO to GPIO24 through a 1k/2k divider.
Camera connects through the Raspberry Pi CSI camera port, not GPIO.

Motor Control
TB6612FNG #1 controls left motors: Motor A front-left, Motor B rear-left.
TB6612FNG #2 controls right motors: Motor A front-right, Motor B rear-right.
STBY is shared on GPIO25.
Motor control pins follow the user-provided GPIO mapping.

Safety Notes
Never connect 7.4V directly to the Raspberry Pi.
Never connect HC-SR04 ECHO directly to a Raspberry Pi GPIO pin.
All GND connections must be common.
Use thicker wiring/traces for battery and motor power.
Use jumper wires only for signal and sensor connections.
Emergency stop should physically cut motor/battery power.
