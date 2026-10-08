# NOT TESTED DO NOT SUBMIT PLEASE

motorB = ev3_motorB()
motorC = ev3_motorC()

sensor = ev3_colorSensor()
touch = ev3_touchSensor1()

def setForce(l,r):
    ev3_motorStop(motorB)
    ev3_motorStop(motorC)
    
    ev3_motorSetSpeed(motorB, l)
    ev3_motorSetSpeed(motorC, r)
    
    ev3_motorStart(motorB)
    ev3_motorStart(motorC)

while(not shouldExit):
    rfl = ev3_reflectedLightIntensity(sensor)
    
    if 75 < rfl and rfl <= 100:
        setForce(100, 0)
    elif 50 < rfl and rfl <= 75:
        setForce(75, 25)
    elif 25 < rfl and rfl <= 50:
        setForce(25, 75)
    else:
        setForce(0, 100)

    shouldExit = ev3_touchSensorPressed(touch)
    ev3_pause(1000)
    