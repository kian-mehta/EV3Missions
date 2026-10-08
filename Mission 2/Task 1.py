sensor = ev3_ultrasonicSensor()
while(True):
    rfl = ev3_reflectedLightIntensity(sensor)
    print(rfl)
    ev3_pause(1000)