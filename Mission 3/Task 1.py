sensor = ev3_colorSensor()
touch = ev3_touchSensor1()
should_exit = False
while(not ev3_touchSensorPressed(touch)):
    rfl = ev3_reflectedLightIntensity(sensor)
    print(rfl)
    ev3_pause(1000)