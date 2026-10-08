# NOT TESTED DO NOT SUBMIT PLEASE

sensor = ev3_colorSensor()
touch = ev3_touchSensor1()
while(not shouldExit):
    rfl = ev3_reflectedLightIntensity(sensor)
    print(rfl)
    shouldExit = ev3_touchSensorPressed(touch)
    ev3_pause(1000)