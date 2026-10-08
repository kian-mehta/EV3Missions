motorB = ev3_motorB()
motorC = ev3_motorC()

sensor = ev3_ultrasonicSensor()

threshold = 10
reverseDistance = 30

ev3_motorSetSpeed(motorB, 100)
ev3_motorSetSpeed(motorC, 100)

distance = ev3_ultrasonicSensorDistance(sensor)/10
while(distance > threshold):
    ev3_motorStart(motorB)
    ev3_motorStart(motorC)
    distance = ev3_ultrasonicSensorDistance(sensor)/10

ev3_motorStop(motorB)
ev3_motorStop(motorC)

def move_by(distance, dir):
    diameter = 5.6
    speed = 100
    time = 36*speed*distance/(math_pi*diameter)
    
    ev3_runForTime(motorC, time, speed*dir)
    ev3_runForTime(motorB, time, speed*dir)
    
    ev3_motorSetStopAction(motorB, 'brake')
    ev3_motorSetStopAction(motorC, 'brake')
    
    ev3_motorStart(motorB)
    ev3_motorStart(motorC)
    
    ev3_pause(time+100)
    
move_by(30, -1)