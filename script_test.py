import odrive
from odrive.enums import *
from actuator import *

SN_L0 = '384D34783539'
SN_L1 = '383F34723539'

odrv0 = odrive.find_any(serial_number=SN_L0)
odrv1 = odrive.find_any(serial_number=SN_L1)

leftFinger0 = Actuator(odrv0, 0.96, 1, 45)
leftFinger1 = Actuator(odrv1, 0.97, 1, 45)

print(str(leftFinger0.encoder))
print(str(leftFinger1.encoder))
print(str(leftFinger0.motor_pos))
# print(str(odrv0))
# print(str(odrv1))

# print(str(odrv0.encoder_estimator1.pos_estimate))
# print(str(odrv1.encoder_estimator1.pos_estimate))

# while(True)
# odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
# odrv1.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

# 1. Attack point 1
# odrv0.axis0.controller.input_pos = 0.80
# odrv1.axis0.controller.input_pos = 1.09
# odrv0.axis0.controller.input_pos = 1.06
# odrv1.axis0.controller.input_pos = 0.99

# 2. Attack point 2
# odrv0.axis0.controller.input_pos = 0.80
# odrv1.axis0.controller.input_pos = 1.12
# odrv0.axis0.controller.input_pos = 0.93
# odrv1.axis0.controller.input_pos = 1.10

# 3. Attack point 3
# odrv0.axis0.controller.input_pos = 0.93
# odrv1.axis0.controller.input_pos = 1.03
# odrv0.axis0.controller.input_pos = 1.03
# odrv1.axis0.controller.input_pos = 1.0

# odrv0.axis0.requested_state = AXIS_STATE_IDLE
# odrv1.axis0.requested_state = AXIS_STATE_IDLE
