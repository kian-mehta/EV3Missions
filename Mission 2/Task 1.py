sensor = ev3_ultrasonicSensor()
while(True):
    dist = ev3_ultrasonicSensorDistance(sensor)/10
    print(dist)
    ev3_pause(1000)