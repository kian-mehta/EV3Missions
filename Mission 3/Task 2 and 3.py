motorB = ev3_motorB()
motorC = ev3_motorC()

sensor = ev3_colorSensor()
touch = ev3_touchSensor1()
scale = 2 # can set higher value but less accurate and more jerky. 0 < scale <= 4

def setForce(l,r):
    ev3_motorSetSpeed(motorB, l)
    ev3_motorSetSpeed(motorC, r)
    
    ev3_motorStart(motorB)
    ev3_motorStart(motorC)

while(not ev3_touchSensorPressed(touch)):
    rfl = ev3_reflectedLightIntensity(sensor)
    
    if rfl > 50:
        setForce(100*scale,-50*scale)
    else:
        setForce(-50*scale,100*scale)

    
ev3_motorStop(motorB)
ev3_motorStop(motorC)