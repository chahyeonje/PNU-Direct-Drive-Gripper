import odrive
from odrive.enums import *
from actuator import *

def Docalibration(motorDriverSerialNumber):
    serialNumber = motorDriverSerialNumber
    odrv = odrive.find_any(serial_number = serialNumber)
    odrv.clear_errors()
    odrv.axis0.requsted_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE